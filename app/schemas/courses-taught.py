from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


# Joint table since its a many-to-many relationship
class CoursesTaught(BaseModel):
    instructor_id: UUID4 = Field(default_factory=uuid4)
    course_id: UUID4 = Field(default_factory=uuid4)
