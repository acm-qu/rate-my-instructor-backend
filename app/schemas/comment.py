from datetime import datetime
from uuid import uuid7

from pydantic import (
    UUID7,
    BaseModel,
    ConfigDict,
    Field,
    NonNegativeFloat,
    NonNegativeInt,
    Optional,
    model_validator,
)


class Comment(BaseModel):
    id: UUID7 = Field(default_factory=uuid7)
    user_id: UUID7 = Field(default_factory=uuid7)
    instructor_id: Optional[UUID7] = Field(default_factory=None)
    course_id: Optional[UUID7] = Field(default_factory=None)

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
