from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    metadata_ = Column("metadata", JSONB, nullable=True)
    major = Column(String(100), nullable=True)

    # Relationships
    comments = relationship("Comment", back_populates="user")
    replies = relationship("Reply", back_populates="user")
    reports = relationship("Report", back_populates="reporter")