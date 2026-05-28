from pydantic import BaseModel, Field, Optional, NonNegativeInt, NonNegativeFloat, model_validator, ConfigDict

from datetime import datetime

from schemas.user import User
from schemas.reply import Reply
from schemas.report import Report
from schemas.course import Course
from schemas.instructor import Instructor

class Comment(BaseModel):
    id: NonNegativeInt
    user_id: NonNegativeInt
    instructor_id: NonNegativeInt
    course_id: NonNegativeInt

    content: str
    rating: NonNegativeFloat
    upvotes: NonNegativeInt = Field(default=0)
    flagged: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)

    user: User
    instructor: Optional[Instructor]
    course: Optional[Course]
    replies: list[Reply]
    reports: list[Report]

    @model_validator(mode="after")
    def check_comment(self):
        if not self.instructor and not self.course:
            return ValueError("The comment should strictly be on either an instructor or a course")
        return self
    
    model_config = ConfigDict(from_attributes=True, strict=True, extra="forbid")