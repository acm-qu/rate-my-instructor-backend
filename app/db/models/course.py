from db.session import Base
from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship


class Course(Base):
    id = Column(UUID, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    subject = Column(String(50), nullable=True)
    metadata_ = Column("metadata", JSONB, nullable=True)
    difficulty = Column(Integer, nullable=True)
    number_of_instructors = Column(Integer, default=0)
    instructor_id = Column(
        UUID, ForeignKey("instructors.id", ondelete="SET NULL"), nullable=True
    )

    # Relationships
    instructor = relationship("Instructor", back_populates="courses_taught")
    comments = relationship("Comment", back_populates="course")
