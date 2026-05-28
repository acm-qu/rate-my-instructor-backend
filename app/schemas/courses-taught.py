from pydantic import BaseModel, Field, UUID7

from uuid import uuid7

# Joint table since its a many-to-many relationship
class CoursesTaught(BaseModel):
  instructor_id: UUID7 = Field(default_factory=uuid7)
  course_id: UUID7 = Field(default_factory=uuid7)
