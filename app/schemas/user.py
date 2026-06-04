from uuid import uuid7

from pydantic import UUID7, BaseModel, ConfigDict, EmailStr, Field
from schemas.msc.enums import Level
from schemas.msc.regex import QUStudentEmail, Username


class User(BaseModel):
    id: UUID7 = Field(default_factory=uuid7)

    username: str = Field(pattern=Username, max_length=30)
    email: EmailStr = Field(
        pattern=QUStudentEmail, min_length=19, max_length=19, default=None
    )
    major: str | None

    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        strict=True,
        json_schema_extra={
            "example": {
                "id": "019e704e-09b1-749d-b7c2-231b581499a0",
                "username": "Character_Development",
                "email": "aa2318467@qu.edu.qa",
                "metadata": {"bio": "I hate java", "level": Level.SOPHOMORE},
                "major": "B.Sc. Applied Mathematics",
            }
        },
    )
