from typing import TypedDict

from schemas.msc.enums import Level


class InstructorMetadata(TypedDict):
    concentration: str
    linkedin: str


class UserMetadata(TypedDict):
    bio: str
    level: Level


class CourseMetadata(TypedDict):
    description: str
