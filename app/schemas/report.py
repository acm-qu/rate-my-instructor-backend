from datetime import datetime
from uuid import uuid4

from pydantic import UUID4, BaseModel, ConfigDict, Field, model_validator
from schemas.msc.enums import ReportReason, ReportTargetType
from typing import Optional


class Report(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)

    user_id: UUID4 = Field(default_factory=uuid4)
    comment_id: Optional[UUID4] = Field(default=None)
    reply_id: Optional[UUID4] = Field(default=None)

    target_type: ReportTargetType
    reason: ReportReason = Field(default=ReportReason.OTHER)
    description: str
    is_reviewed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)

    @model_validator(mode="after")
    def check_report(self):
        if not self.comment_id and not self.reply_id:
            raise ValueError("The report should have a comment or a reply attached")
        return self

    model_config = ConfigDict(
        from_attributes=True,
        strict=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "user_id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "comment_id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "reply_id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "target_type": ReportTargetType.COMMENT,
                "reason": ReportReason.INAPPROPRIATE,
                "description": "This comment doesnt glaze mohamed mabrok enough.",
                "is_reviewed": False,
                "created_at": "2026-05-28 21:07:16.397239",
            }
        },
    )
