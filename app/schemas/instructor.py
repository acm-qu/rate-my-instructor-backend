from typing import Any

from pydantic import BaseModel, Field, Optional, NonNegativeInt, NonNegativeFloat, ConfigDict

from schemas.course import Course
from schemas.comment import Comment

class Instructor(BaseModel):
    id: NonNegativeInt

    name: str = Field(max_length=50)
    department: str = Field(max_length=100)
    metadata: Optional[dict[str, Any]] = Field(default=None)
    rating: Optional[NonNegativeFloat]
    number_of_ratings: NonNegativeInt = Field(default=0)

    courses_taught: list[Course]
    comments: list[Comment]

    model_config = ConfigDict(from_attributes=True, extra="forbid", strict=True)