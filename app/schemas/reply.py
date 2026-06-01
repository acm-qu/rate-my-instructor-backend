from datetime import datetime
from uuid import uuid4

from pydantic import UUID4, BaseModel, ConfigDict, Field, NonNegativeInt


class Reply(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    user_id: UUID4 = Field(default_factory=uuid4)
    comment_id: UUID4 = Field(default_factory=uuid4)

    content: str
    upvotes: NonNegativeInt = Field(default=0)
    flagged: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
        strict=True,
        json_schema_extra={
            "example": {
                "id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "user_id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "comment_id": "019e704e-09b1-749d-b7c2-231b581499a2",
                "content": "He explains the grading breakdown clearly and responds quickly during office hours.",
                "upvotes": 67,
                "flagged": False,
                "created_at": "2026-05-28 21:07:16.397239",
            }
        },
    )
