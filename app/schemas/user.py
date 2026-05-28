from uuid import uuid7

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, Optional, EmailStr, UUID7

from schemas.regex import QUStudentEmail
from schemas.comment import Comment
from schemas.reply import Reply
from schemas.report import Report

class User(BaseModel):
    id: UUID7 = Field(default_factory=uuid7)

    email: EmailStr = Field(pattern=QUStudentEmail, min_length=19, max_length=19, default=None)
    metadata: Optional[dict[str, Any]] = Field(default=None)
    major: Optional[str]

    comments: list[Comment]
    replies: list[Reply]
    reports: list[Report]

    model_config = ConfigDict(extra="forbid", from_attributes=True, strict=True)