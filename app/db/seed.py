# Running this script should seed the DB with fake data for testing purposes
import os
import json
import random
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
db = Session()

PHD_CONCENTRATIONS = [
    "Machine Learning", "Computer Networks", "Database Systems",
    "Software Engineering", "Algorithms & Complexity", "Numerical Analysis",
    "Quantum Computing", "Embedded Systems", "Bioinformatics", "Financial Modeling",
]

INSTRUCTORS = [
    {"name": "Ahmed Al-Mansouri",    "department": "Computer Science"},
    {"name": "Fatima Al-Zahrawi",   "department": "Mathematics"},
    {"name": "Khalid Al-Rashidi",   "department": "Electrical Engineering"},
    {"name": "Sara Al-Mutairi",     "department": "Business Administration"},
    {"name": "Omar Al-Farsi",       "department": "Physics"},
    {"name": "Nora Al-Shehri",      "department": "Information Systems"},
    {"name": "Mohammed Al-Balushi", "department": "Computer Science"},
    {"name": "Layla Al-Harbi",      "department": "Chemistry"},
    {"name": "Yousef Al-Tamimi",    "department": "Civil Engineering"},
    {"name": "Aisha Al-Qassimi",    "department": "Biology"},
    {"name": "Tariq Al-Otaibi",     "department": "Economics"},
    {"name": "Maryam Al-Sulaiti",   "department": "Mathematics"},
    {"name": "Hassan Al-Emadi",     "department": "Computer Science"},
    {"name": "Reem Al-Kuwari",      "department": "Business Administration"},
    {"name": "Saeed Al-Nuaimi",     "department": "Electrical Engineering"},
]

COURSES = [
    {"code": "CMPS101", "subject": "Introduction to Programming"},
    {"code": "CMPS201", "subject": "Data Structures"},
    {"code": "CMPS301", "subject": "Algorithms"},
    {"code": "CMPS351", "subject": "Database Management Systems"},
    {"code": "CMPS401", "subject": "Operating Systems"},
    {"code": "CMPS450", "subject": "Machine Learning"},
    {"code": "CMPS460", "subject": "Computer Networks"},
    {"code": "MATH101", "subject": "Calculus I"},
    {"code": "MATH201", "subject": "Calculus II"},
    {"code": "MATH301", "subject": "Linear Algebra"},
    {"code": "MATH401", "subject": "Numerical Methods"},
    {"code": "PHYS101", "subject": "Physics I"},
    {"code": "PHYS201", "subject": "Physics II"},
    {"code": "ECON201", "subject": "Microeconomics"},
    {"code": "ECON301", "subject": "Macroeconomics"},
    {"code": "BUSN201", "subject": "Principles of Management"},
    {"code": "BUSN301", "subject": "Marketing"},
    {"code": "BUSN401", "subject": "Strategic Management"},
    {"code": "ELEC301", "subject": "Circuit Analysis"},
    {"code": "ELEC401", "subject": "Digital Signal Processing"},
    {"code": "INFO201", "subject": "Systems Analysis"},
    {"code": "INFO301", "subject": "Software Engineering"},
    {"code": "CHEM101", "subject": "General Chemistry"},
    {"code": "BIO101",  "subject": "Introduction to Biology"},
]

USERS = [
    {"email": "s-202100001@qu.edu.qa", "major": "CS-COMPUTER SCIENCE",         "status": "junior",    "college": "College of Computer Science & Engineering"},
    {"email": "s-202100002@qu.edu.qa", "major": "MATH-APPLIED MATHEMATICS",    "status": "senior",    "college": "College of Arts & Sciences"},
    {"email": "s-202100003@qu.edu.qa", "major": "EE-ELECTRICAL ENGINEERING",   "status": "sophomore", "college": "College of Engineering"},
    {"email": "s-202100004@qu.edu.qa", "major": "BUS-BUSINESS ADMINISTRATION", "status": "freshman",  "college": "College of Business & Economics"},
    {"email": "s-202100005@qu.edu.qa", "major": "CS-SOFTWARE ENGINEERING",     "status": "senior",    "college": "College of Computer Science & Engineering"},
    {"email": "s-202100006@qu.edu.qa", "major": "IS-INFORMATION SYSTEMS",      "status": "junior",    "college": "College of Computer Science & Engineering"},
    {"email": "s-202100007@qu.edu.qa", "major": "PHYS-PHYSICS",                "status": "sophomore", "college": "College of Arts & Sciences"},
    {"email": "s-202100008@qu.edu.qa", "major": "ECON-ECONOMICS",              "status": "senior",    "college": "College of Business & Economics"},
    {"email": "s-202100009@qu.edu.qa", "major": "CHEM-CHEMISTRY",              "status": "freshman",  "college": "College of Arts & Sciences"},
    {"email": "s-202100010@qu.edu.qa", "major": "BIO-BIOLOGY",                 "status": "junior",    "college": "College of Arts & Sciences"},
    {"email": "s-202100011@qu.edu.qa", "major": "CE-CIVIL ENGINEERING",        "status": "senior",    "college": "College of Engineering"},
    {"email": "s-202100012@qu.edu.qa", "major": "CS-COMPUTER SCIENCE",         "status": "graduate",  "college": "College of Computer Science & Engineering"},
    {"email": "s-202100013@qu.edu.qa", "major": "MATH-PURE MATHEMATICS",       "status": "junior",    "college": "College of Arts & Sciences"},
    {"email": "s-202100014@qu.edu.qa", "major": "BUS-BUSINESS ADMINISTRATION", "status": "sophomore", "college": "College of Business & Economics"},
    {"email": "s-202100015@qu.edu.qa", "major": "IS-INFORMATION SYSTEMS",      "status": "senior",    "college": "College of Computer Science & Engineering"},
]

POSITIVE_COMMENTS = [
    "One of the best professors I've had at QU. Explains concepts clearly and is always willing to help during office hours.",
    "Absolutely loved this course. The professor makes even the hardest topics feel manageable. Highly recommend.",
    "Very organized and fair grader. The assignments are challenging but you learn a lot from them.",
    "Incredibly knowledgeable. The lectures are engaging and the material is well-structured.",
    "Great professor! Makes the class interesting with real-world examples. Always available on Teams.",
    "Exams are fair if you attend lectures. Notes are detailed and the professor answers every question patiently.",
    "Best course I've taken this semester. The professor genuinely cares about student success.",
    "Very helpful and approachable. The workload is manageable and the grading is transparent.",
    "Loved the teaching style. Mixed theory with practice perfectly. Will take another course with this professor.",
    "Clear expectations from day one. No surprises on exams. Exactly what you studied is what you get tested on.",
]

MIXED_COMMENTS = [
    "The content is interesting but the pace is fast. Make sure to do the readings before each lecture.",
    "Good professor overall but office hours are limited. Would appreciate more availability.",
    "Midterm was harder than expected but the final was fair. The curve helped a lot.",
    "Teaching style takes getting used to but the material is solid. Attend all lectures.",
    "The course material is great but some slides could be clearer. Recommend supplementing with YouTube.",
    "Assignments are a lot of work but you do learn. Don't leave things to the last minute.",
    "Not the most engaging lectures but the content is important and tested directly. Stay focused.",
    "Grading can be strict but fair. Partial credit is given if your logic is correct.",
    "Some topics felt rushed near the end of the semester. Ask questions during class.",
    "The professor knows the material very well but sometimes assumes too much prior knowledge.",
]

NEGATIVE_COMMENTS = [
    "Very hard grader. Exam questions come from topics barely covered in class. Expected much better.",
    "Attendance is mandatory but lectures add little value beyond the textbook. Frustrating.",
    "The syllabus kept changing throughout the semester which made planning very difficult.",
    "Little feedback on assignments. Hard to improve when you don't know what you did wrong.",
    "Office hours were rarely held and emails took days to get a response. Needs improvement.",
    "Exams were way harder than anything practiced in class. Did not feel prepared.",
    "The course content is good but the delivery is dry. Hard to stay engaged in long lectures.",
]

REPLY_TEXTS = [
    "Totally agree with this review!",
    "Had the same experience, very accurate.",
    "I disagree, I found the professor quite helpful.",
    "This is fair. The workload is heavy but worth it.",
    "Thanks for the honest review, helped me decide.",
    "Same here, the midterm caught everyone off guard.",
    "The professor improved a lot in the second half of the semester.",
    "100% accurate. Prepare well in advance for exams.",
    "I had a different experience but I can see where you're coming from.",
    "Great review, exactly what I needed to know before enrolling.",
]

REPORT_DESCRIPTIONS = [
    "This looks like spam and should be reviewed.",
    "The language here is inappropriate for the platform.",
    "I think this is misleading and needs moderation.",
    "This comment feels hostile and should be checked.",
    "The content appears unrelated to the instructor discussion.",
]

def seed_users():
    print("Seeding users...")
    user_ids = []
    for u in USERS:
        metadata = json.dumps({
            "year_of_study": u["status"],
            "college": u["college"],
        })
        result = db.execute(
            text("""
                INSERT INTO users (email, metadata, major)
                VALUES (:email, CAST(:metadata AS JSONB), :major)
                ON CONFLICT (email) DO UPDATE SET major = EXCLUDED.major
                RETURNING id
            """),
            {"email": u["email"], "metadata": metadata, "major": u["major"]}
        )
        user_ids.append(result.fetchone()[0])
    db.commit()
    print(f"  OK  {len(user_ids)} users inserted.")
    return user_ids


def seed_instructors():
    print("Seeding instructors...")
    instructor_ids = []
    for inst in INSTRUCTORS:
        metadata = json.dumps({
            "phd_concentration": random.choice(PHD_CONCENTRATIONS),
            "office": f"Building {random.randint(1, 20)}, Room {random.randint(100, 499)}",
            "email": inst["name"].lower().replace(" ", ".") + "@qu.edu.qa",
        })
        result = db.execute(
            text("""
                INSERT INTO instructors (name, department, metadata, rating, number_of_ratings)
                VALUES (:name, :dept, CAST(:metadata AS JSONB), :rating, :num)
                RETURNING id
            """),
            {
                "name":    inst["name"],
                "dept":    inst["department"],
                "metadata": metadata,
                "rating":  round(random.uniform(2.5, 5.0), 1),
                "num":     random.randint(10, 150),
            }
        )
        instructor_ids.append(result.fetchone()[0])
    db.commit()
    print(f"  OK  {len(instructor_ids)} instructors inserted.")
    return instructor_ids


def seed_courses(instructor_ids):
    print("Seeding courses...")
    course_ids = []
    for c in COURSES:
        metadata = json.dumps({
            "credits":  random.choice([2, 3, 4]),
            "semester": random.choice(["Fall 2024", "Spring 2025", "Fall 2025"]),
        })
        result = db.execute(
            text("""
                INSERT INTO courses (code, subject, metadata, number_of_instructors, instructor_id)
                VALUES (:code, :subject, CAST(:metadata AS JSONB), :num_inst, :inst_id)
                ON CONFLICT (code) DO UPDATE SET subject = EXCLUDED.subject
                RETURNING id
            """),
            {
                "code":      c["code"],
                "subject":   c["subject"],
                "metadata":  metadata,
                "num_inst":  random.randint(1, 4),
                "inst_id":   random.choice(instructor_ids),
            }
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
            content   = random.choice(all_comments)
            rating    = round(random.uniform(1.5, 5.0), 1)
            course_id = random.choice(course_ids) if random.random() > 0.2 else None
            result = db.execute(
                text("""
                    INSERT INTO comments (user_id, instructor_id, course_id, content, rating, upvotes, flagged)
                    VALUES (:uid, :iid, :cid, :content, :rating, :upvotes, :flagged)
                    RETURNING id
                """),
                {
                    "uid":     user_id,
                    "iid":     inst_id,
                    "cid":     course_id,
                    "content": content,
                    "rating":  rating,
                    "upvotes":   random.randint(0, 40),
                    "flagged": random.random() < 0.05,
                }
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
                        "uid":     user_id,
                        "cid":     comment_id,
                        "content": random.choice(REPLY_TEXTS),
                        "upvotes":   random.randint(0, 15),
                        "flagged": random.random() < 0.03,
                    }
                )
                reply_count += 1
    db.commit()
    print(f"  OK  {reply_count} replies inserted.")


def seed_reports(user_ids):
    print("Seeding reports...")
    comment_ids = [row[0] for row in db.execute(text("SELECT id FROM comments")).fetchall()]
    reply_ids = [row[0] for row in db.execute(text("SELECT id FROM replies")).fetchall()]

    report_count = 0

    if comment_ids:
        for comment_id in random.sample(comment_ids, min(len(comment_ids), random.randint(8, 18))):
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
                    "reason": random.choice(["SPAM", "INAPPROPRIATE", "HARASSMENT", "MISINFORMATION", "OTHER"]),
                    "description": random.choice(REPORT_DESCRIPTIONS),
                    "is_reviewed": random.random() < 0.35,
                }
            )
            report_count += 1

    if reply_ids:
        for reply_id in random.sample(reply_ids, min(len(reply_ids), random.randint(5, 12))):
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
                    "reason": random.choice(["SPAM", "INAPPROPRIATE", "HARASSMENT", "MISINFORMATION", "OTHER"]),
                    "description": random.choice(REPORT_DESCRIPTIONS),
                    "is_reviewed": random.random() < 0.35,
                }
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
        user_ids       = seed_users()
        instructor_ids = seed_instructors()
        course_ids     = seed_courses(instructor_ids)
        comment_ids    = seed_comments(user_ids, instructor_ids, course_ids)
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