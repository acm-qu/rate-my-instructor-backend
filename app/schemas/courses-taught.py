from uuid import uuid7

from pydantic import UUID7, BaseModel, Field


# Joint table since its a many-to-many relationship
class CoursesTaught(BaseModel):
    instructor_id: UUID7 = Field(default_factory=uuid7)
    course_id: UUID7 = Field(default_factory=uuid7)
