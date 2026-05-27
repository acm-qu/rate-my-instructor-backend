from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from db.session import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    subject = Column(String(50), nullable=True)
    metadata_ = Column("metadata", JSONB, nullable=True)
    number_of_instructors = Column(Integer, default=0)
    instructor_id = Column(Integer, ForeignKey("instructors.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    instructor = relationship("Instructor", back_populates="courses_taught")
    comments = relationship("Comment", back_populates="course")