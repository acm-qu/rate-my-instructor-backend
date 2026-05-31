from db.session import Base
from sqlalchemy import UUID, Boolean, Column, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import relationship


class Reply(Base):
    id = Column(UUID, primary_key=True, index=True)
    user_id = Column(
        UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    comment_id = Column(
        UUID, ForeignKey("comments.id", ondelete="CASCADE"), nullable=False
    )
    content = Column(Text, nullable=False)
    upvotes = Column(Integer, default=0)
    flagged = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="replies")
    comment = relationship("Comment", back_populates="replies")
    reports = relationship("Report", back_populates="reply")
