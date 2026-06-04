from uuid import uuid7

from db.session import Base
from sqlalchemy import UUID, Column, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(UUID, primary_key=True, index=True)

    username = Column(String(255), unique=True, nullable=False, default=lambda: "qu-student-"+str(uuid7())[:4])
    email = Column(String(255), unique=True, nullable=False)
    metadata_ = Column("metadata", JSONB, nullable=True)
    major = Column(String(100), nullable=True)

    # Relationships
    comments = relationship("Comment", back_populates="user")
    replies = relationship("Reply", back_populates="user")
    reports = relationship("Report", back_populates="user")
