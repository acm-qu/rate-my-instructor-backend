from sqlalchemy import ForeignKey, Column, Enum, Integer, Text, Boolean, DateTime, func
from sqlalchemy.orm import relationship

from app.schemas.msc.enums import ReportTargetType, ReportReason

from db.session import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    # Who submitted the report
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

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
    user = relationship("User", back_populates="reports")
    comment = relationship("Comment", back_populates="reports")
    reply = relationship("Reply", back_populates="reports")