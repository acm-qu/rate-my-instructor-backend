from pydantic import BaseModel, Field, Optional, NonNegativeInt, model_validator, ConfigDict

from schemas.enums import ReportTargetType, ReportReason

from datetime import datetime

from schemas.user import User
from schemas.comment import Comment
from schemas.reply import Reply

class Report(BaseModel):
    id: NonNegativeInt

    user_id: NonNegativeInt
    target_type: ReportTargetType
    comment_id: NonNegativeInt
    reply_id: NonNegativeInt

    reason: ReportReason = Field(default=ReportReason.OTHER)
    content: str
    is_reviewed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)

    user: User
    comment: Optional[Comment]
    reply: Optional[Reply]

    @model_validator(mode="after")
    def check_report(self):
        if not self.comment and not self.reply:
            return ValueError("The report should have a comment or a reply attached")
        return self
    
    model_config = ConfigDict(from_attributes=True, stric=True, extra="forbid")