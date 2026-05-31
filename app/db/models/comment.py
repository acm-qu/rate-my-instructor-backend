from db.session import Base
from sqlalchemy import (
    UUID,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Text,
    func,
)
from sqlalchemy.orm import relationship


class Comment(Base):
    id = Column(UUID, primary_key=True, index=True)
    user_id = Column(
        UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    instructor_id = Column(
        UUID, ForeignKey("instructors.id", ondelete="CASCADE"), nullable=False
    )
    course_id = Column(
        UUID, ForeignKey("courses.id", ondelete="CASCADE"), nullable=True
    )
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
