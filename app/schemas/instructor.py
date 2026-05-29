from uuid import uuid7

from pydantic import (
    UUID7,
    BaseModel,
    ConfigDict,
    Field,
    NonNegativeFloat,
    NonNegativeInt,
    Optional,
)
from schemas.msc.metadata import InstructorMetadata


class Instructor(BaseModel):
    id: UUID7 = Field(default_factory=uuid7)

    name: str = Field(max_length=50)
    department: str = Field(max_length=100)
    metadata: Optional[InstructorMetadata] = Field(default=None)
    rating: NonNegativeFloat = Field(default=0, le=5)
    number_of_ratings: NonNegativeInt = Field(default=0)

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
        strict=True,
        json_schema_extra={
            "example": {
                "id": "019e704e-09b1-749d-b7c2-231b581499a0",
                "name": "Mohamed Mabrok",
                "department": "CAS - Mathematics & Statistics",
                "rating": 5,  # ofc
                "number_of_ratings": 67,
                "comments": [],
            }
        },
    )
