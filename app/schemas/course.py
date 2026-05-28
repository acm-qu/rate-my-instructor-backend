from typing import Any

from pydantic import BaseModel, Field, NonNegativeInt, ConfigDict

from schemas.regex import QUCourseCode
from schemas.instructor import Instructor
from schemas.comment import Comment

class Course(BaseModel):
    id: NonNegativeInt
    instructor_id: NonNegativeInt

    code: str = Field(pattern=QUCourseCode)
    subject: str = Field(lt=50)
    metadata: dict[str, Any]
    number_of_instructors: NonNegativeInt = Field(default=0)

    instructors: list[Instructor]
    comments: list[Comment]

    model_config = ConfigDict(from_attributes=True, extra="forbid", strict=True)