from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean, DateTime, func, Enum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from db.session import Base
from db.models.enums import ReportReason, ReportTargetType

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    metadata_ = Column("metadata", JSONB, nullable=True)
    major = Column(String(100), nullable=True)

    # Relationships
    comments = relationship("Comment", back_populates="user")
    replies = relationship("Reply", back_populates="user")
    reports = relationship("Report", back_populates="reporter")

class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department = Column(String(100), nullable=True)
    metadata_ = Column("metadata", JSONB, nullable=True)
    rating = Column(Float, nullable=True)
    number_of_ratings = Column(Integer, default=0)

    # Relationships
    courses_taught = relationship("Course", back_populates="instructor")
    comments = relationship("Comment", back_populates="instructor")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    subject = Column(String(50), nullable=True)
    metadata_ = Column("metadata", JSONB, nullable=True)
    number_of_instructors = Column(Integer, default=0)
    instructor_id = Column(Integer, ForeignKey("instructors.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    instructor = relationship("Instructor", back_populates="courses_taught")
    comments = relationship("Comment", back_populates="course")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    instructor_id = Column(Integer, ForeignKey("instructors.id", ondelete="CASCADE"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="SET NULL"), nullable=True)
    content = Column(Text, nullable=False)
    rating = Column(Float, nullable=False)
    upvotes = Column(Integer, default=0)
    flagged = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="comments")
    instructor = relationship("Instructor", back_populates="comments")
    course = relationship("Course", back_populates="comments")
    replies = relationship("Reply", back_populates="comment")
    reports = relationship("Report", back_populates="comment")

class Reply(Base):
    __tablename__ = "replies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    comment_id = Column(Integer, ForeignKey("comments.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    upvotes = Column(Integer, default=0)
    flagged = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="replies")
    comment = relationship("Comment", back_populates="replies")
    reports = relationship("Report", back_populates="reply")

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    # Who submitted the report
    reporter_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # What is being reported
    target_type = Column(Enum(ReportTargetType, name="report_target_type"), nullable=False)
    comment_id = Column(Integer, ForeignKey("comments.id", ondelete="CASCADE"), nullable=True)
    reply_id = Column(Integer, ForeignKey("replies.id", ondelete="CASCADE"), nullable=True)

    # Report details
    reason = Column(Enum(ReportReason, name="report_reason"), nullable=False, default=ReportReason.OTHER)
    description = Column(Text, nullable=True)
    is_reviewed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    reporter = relationship("User", back_populates="reports")
    comment = relationship("Comment", back_populates="reports")
    reply = relationship("Reply", back_populates="reports")