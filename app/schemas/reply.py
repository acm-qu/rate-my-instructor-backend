from pydantic import BaseModel, Field, NonNegativeInt, ConfigDict

from datetime import datetime

from schemas.user import User
from schemas.comment import Comment
from schemas.report import Report

class Reply(BaseModel):
    id: NonNegativeInt
    user_id: NonNegativeInt
    comment_id: NonNegativeInt
    content: str
    upvotes: NonNegativeInt = Field(default=0)
    flagged: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)

    user: User
    comment: Comment
    reports: list[Report]

    model_config = ConfigDict(from_attributes=True, extra="forbid", strict=True)