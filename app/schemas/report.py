from datetime import datetime
from uuid import uuid7

from pydantic import UUID7, BaseModel, ConfigDict, Field, Optional, model_validator
from schemas.msc.enums import ReportReason, ReportTargetType


class Report(BaseModel):
    id: UUID7 = Field(default_factory=uuid7)

    user_id: UUID7 = Field(default_factory=uuid7)
    comment_id: Optional[UUID7] = Field(default_factory=None)
    reply_id: Optional[UUID7] = Field(default_factory=None)

    target_type: ReportTargetType
    reason: ReportReason = Field(default=ReportReason.OTHER)
    content: str
    is_reviewed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)

    @model_validator(mode="after")
    def check_report(self):
        if not self.comment_id and not self.reply_id:
            return ValueError("The report should have a comment or a reply attached")
        return self

    model_config = ConfigDict(
        from_attributes=True,
        stric=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "user_id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "comment_id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "reply_id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "target_type": ReportTargetType.COMMENT,
                "reason": ReportReason.INAPPROPRIATE,
                "content": "This comment doesnt glaze mohamed mabrok enough.",
                "is_reviewed": False,
                "created_at": "2026-05-28 21:07:16.397239",
            }
        },
    )
