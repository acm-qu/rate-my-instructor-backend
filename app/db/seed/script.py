# Running this script should seed the DB with fake data for testing purposes
import os
import json
import random
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.db.seed.constants import (
    USERS,
    INSTRUCTORS,
    PHD_CONCENTRATIONS,
    COURSES,
    POSITIVE_COMMENTS,
    MIXED_COMMENTS,
    NEGATIVE_COMMENTS,
    REPLY_TEXTS,
    REPORT_DESCRIPTIONS,
)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
db = Session()


def seed_users():
    print("Seeding users...")
    user_ids = []
    for u in USERS:
        metadata = json.dumps(
            {
                "year_of_study": u["status"],
                "college": u["college"],
            }
        )
        result = db.execute(
            text("""
                INSERT INTO users (email, metadata, major)
                VALUES (:email, CAST(:metadata AS JSONB), :major)
                ON CONFLICT (email) DO UPDATE SET major = EXCLUDED.major
                RETURNING id
            """),
            {"email": u["email"], "metadata": metadata, "major": u["major"]},
        )
        user_ids.append(result.fetchone()[0])
    db.commit()
    print(f"  OK  {len(user_ids)} users inserted.")
    return user_ids


def seed_instructors():
    print("Seeding instructors...")
    instructor_ids = []
    for inst in INSTRUCTORS:
        metadata = json.dumps(
            {
                "phd_concentration": random.choice(PHD_CONCENTRATIONS),
                "office": f"Building {random.randint(1, 20)}, Room {random.randint(100, 499)}",
                "email": inst["name"].lower().replace(" ", ".") + "@qu.edu.qa",
            }
        )
        result = db.execute(
            text("""
                INSERT INTO instructors (name, department, metadata, rating, number_of_ratings)
                VALUES (:name, :dept, CAST(:metadata AS JSONB), :rating, :num)
                RETURNING id
            """),
            {
                "name": inst["name"],
                "dept": inst["department"],
                "metadata": metadata,
                "rating": round(random.uniform(2.5, 5.0), 1),
                "num": random.randint(10, 150),
            },
        )
        instructor_ids.append(result.fetchone()[0])
    db.commit()
    print(f"  OK  {len(instructor_ids)} instructors inserted.")
    return instructor_ids


def seed_courses(instructor_ids):
    print("Seeding courses...")
    course_ids = []
    for c in COURSES:
        metadata = json.dumps(
            {
                "credits": random.choice([2, 3, 4]),
                "semester": random.choice(["Fall 2024", "Spring 2025", "Fall 2025"]),
            }
        )
        result = db.execute(
            text("""
                INSERT INTO courses (code, subject, metadata, number_of_instructors, instructor_id)
                VALUES (:code, :subject, CAST(:metadata AS JSONB), :num_inst, :inst_id)
                ON CONFLICT (code) DO UPDATE SET subject = EXCLUDED.subject
                RETURNING id
            """),
            {
                "code": c["code"],
                "subject": c["subject"],
                "metadata": metadata,
                "num_inst": random.randint(1, 4),
                "inst_id": random.choice(instructor_ids),
            },
        )
        course_ids.append(result.fetchone()[0])
    db.commit()
    print(f"  OK  {len(course_ids)} courses inserted.")
    return course_ids


def seed_comments(user_ids, instructor_ids, course_ids):
    print("Seeding comments...")
    comment_ids = []
    all_comments = POSITIVE_COMMENTS + MIXED_COMMENTS + NEGATIVE_COMMENTS

    for inst_id in instructor_ids:
        num_comments = random.randint(3, 6)
        used_users = random.sample(user_ids, min(num_comments, len(user_ids)))
        for user_id in used_users:
            content = random.choice(all_comments)
            rating = round(random.uniform(1.5, 5.0), 1)
            course_id = random.choice(course_ids) if random.random() > 0.2 else None
            result = db.execute(
                text("""
                    INSERT INTO comments (user_id, instructor_id, course_id, content, rating, upvotes, flagged)
                    VALUES (:uid, :iid, :cid, :content, :rating, :upvotes, :flagged)
                    RETURNING id
                """),
                {
                    "uid": user_id,
                    "iid": inst_id,
                    "cid": course_id,
                    "content": content,
                    "rating": rating,
                    "upvotes": random.randint(0, 40),
                    "flagged": random.random() < 0.05,
                },
            )
            comment_ids.append(result.fetchone()[0])
    db.commit()
    print(f"  OK  {len(comment_ids)} comments inserted.")
    return comment_ids


def seed_replies(user_ids, comment_ids):
    print("Seeding replies...")
    reply_count = 0
    for comment_id in comment_ids:
        if random.random() < 0.6:
            num_replies = random.randint(1, 3)
            repliers = random.sample(user_ids, min(num_replies, len(user_ids)))
            for user_id in repliers:
                db.execute(
                    text("""
                        INSERT INTO replies (user_id, comment_id, content, upvotes, flagged)
                        VALUES (:uid, :cid, :content, :upvotes, :flagged)
                    """),
                    {
                        "uid": user_id,
                        "cid": comment_id,
                        "content": random.choice(REPLY_TEXTS),
                        "upvotes": random.randint(0, 15),
                        "flagged": random.random() < 0.03,
                    },
                )
                reply_count += 1
    db.commit()
    print(f"  OK  {reply_count} replies inserted.")


def seed_reports(user_ids):
    print("Seeding reports...")
    comment_ids = [
        row[0] for row in db.execute(text("SELECT id FROM comments")).fetchall()
    ]
    reply_ids = [
        row[0] for row in db.execute(text("SELECT id FROM replies")).fetchall()
    ]

    report_count = 0

    if comment_ids:
        for comment_id in random.sample(
            comment_ids, min(len(comment_ids), random.randint(8, 18))
        ):
            reporter_id = random.choice(user_ids)
            db.execute(
                text("""
                    INSERT INTO reports (
                        reporter_id, target_type, comment_id, reply_id,
                        reason, description, is_reviewed
                    )
                    VALUES (:reporter_id, :target_type, :comment_id, NULL, :reason, :description, :is_reviewed)
                """),
                {
                    "reporter_id": reporter_id,
                    "target_type": "COMMENT",
                    "comment_id": comment_id,
                    "reason": random.choice(
                        [
                            "SPAM",
                            "INAPPROPRIATE",
                            "HARASSMENT",
                            "MISINFORMATION",
                            "OTHER",
                        ]
                    ),
                    "description": random.choice(REPORT_DESCRIPTIONS),
                    "is_reviewed": random.random() < 0.35,
                },
            )
            report_count += 1

    if reply_ids:
        for reply_id in random.sample(
            reply_ids, min(len(reply_ids), random.randint(5, 12))
        ):
            reporter_id = random.choice(user_ids)
            db.execute(
                text("""
                    INSERT INTO reports (
                        reporter_id, target_type, comment_id, reply_id,
                        reason, description, is_reviewed
                    )
                    VALUES (:reporter_id, :target_type, NULL, :reply_id, :reason, :description, :is_reviewed)
                """),
                {
                    "reporter_id": reporter_id,
                    "target_type": "REPLY",
                    "reply_id": reply_id,
                    "reason": random.choice(
                        [
                            "SPAM",
                            "INAPPROPRIATE",
                            "HARASSMENT",
                            "MISINFORMATION",
                            "OTHER",
                        ]
                    ),
                    "description": random.choice(REPORT_DESCRIPTIONS),
                    "is_reviewed": random.random() < 0.35,
                },
            )
            report_count += 1

    db.commit()
    print(f"  OK  {report_count} reports inserted.")


def print_summary():
    print("\nDatabase Summary:")
    for table in ["users", "instructors", "courses", "comments", "replies"]:
        count = db.execute(text(f"SELECT COUNT(*) FROM {table}")).fetchone()[0]
        print(f"  {table:<15} {count} rows")


def main():
    try:
        user_ids = seed_users()
        instructor_ids = seed_instructors()
        course_ids = seed_courses(instructor_ids)
        comment_ids = seed_comments(user_ids, instructor_ids, course_ids)
        seed_replies(user_ids, comment_ids)
        seed_reports(user_ids)
        print_summary()
        print("\nSeeding complete!\n")
    except Exception as e:
        db.rollback()
        print(f"\nError during seeding: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
