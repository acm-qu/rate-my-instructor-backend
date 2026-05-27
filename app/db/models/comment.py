from sqlalchemy import ForeignKey, Column, Integer, Text, Float, Boolean, DateTime, func
from sqlalchemy.orm import relationship

from db.session import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    instructor_id = Column(Integer, ForeignKey("instructors.id", ondelete="CASCADE"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=True)
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