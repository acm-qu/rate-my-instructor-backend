from uuid import uuid7

from pydantic import (
    UUID7,
    BaseModel,
    ConfigDict,
    Field,
    NonNegativeFloat,
    NonNegativeInt,
)
from schemas.msc.regex import QUCourseCode


class Course(BaseModel):
    id: UUID7 = Field(default_factory=uuid7)

    code: str = Field(pattern=QUCourseCode)
    subject: str = Field(max_length=50)
    number_of_instructors: NonNegativeInt = Field(default=0)
    difficulty: NonNegativeFloat = Field(default=0, le=5)

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
        strict=True,
        json_schema_extra={
            "extra": {
                "id": "019e704e-09b1-749d-b7c2-231b581499a0",
                "code": "MATH213",
                "subject": "Mathematics",
                "metadata": {
                    "description": "Solving differential equations or something idk"
                },
                "number_of_instructors": 67,
                "difficulty": 3,
            }
        },
    )
