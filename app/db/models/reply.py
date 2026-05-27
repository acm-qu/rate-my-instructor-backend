from sqlalchemy import ForeignKey, Column, Integer, Text, Boolean, DateTime, func
from sqlalchemy.orm import relationship

from db.session import Base

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