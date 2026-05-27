from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from db.session import Base

class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department = Column(String(100), nullable=True)
    metadata_ = Column("metadata", JSONB, nullable=True)
    rating = Column(Float, nullable=True)
    number_of_ratings = Column(Integer, default=0)

    # Relationships
    courses_taught = relationship("Course", back_populates="instructor")
    comments = relationship("Comment", back_populates="instructor")