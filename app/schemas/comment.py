from datetime import datetime
from uuid import uuid4

from pydantic import (
    UUID4,
    BaseModel,
    ConfigDict,
    Field,
    NonNegativeFloat,
    NonNegativeInt,
    model_validator,
)
from typing import Optional

class Comment(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    user_id: UUID4 = Field(default_factory=uuid4)
    instructor_id: Optional[UUID4] = Field(default=None)
    course_id: Optional[UUID4] = Field(default=None)

    content: str
    rating: NonNegativeFloat
    upvotes: NonNegativeInt = Field(default=0)
    flagged: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)

    @model_validator(mode="after")
    def check_comment(self):
        if not self.instructor_id and not self.course_id:
            raise ValueError(
                "The comment should strictly be on either an instructor or a course"
            )
        return self

    model_config = ConfigDict(
        from_attributes=True,
        strict=True,
        extra="forbid",
        json_schema_extra={
            "example": {
                "id": "019e704e-09b1-749d-b7c2-231b581499a0",
                "user_id": "019e704e-09b1-749d-b7c2-231b581499a0",
                "instructor_id": "019e704e-09b1-749d-b7c2-231b581499a0",
                "content": "Simply the goat",
                "rating": 5,
                "upvotes": 67,
                "flagged": False,
                "created_at": "2026-05-28 21:07:16.397239",
            }
        },
    )
