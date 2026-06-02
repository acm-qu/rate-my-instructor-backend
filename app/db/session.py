import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Connection pool (pool_size = concurrent connections, max_overflow = extra allowed)
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    echo=False,  # debug set to True
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls):
        """
        Convert PascalCase to snake_case name
        """
        res = ""
        if len(cls.__name__) == 0:
            return ""
        res = str.lower(cls.__name__[0])
        for char in cls.__name__[1:]:
            if char == str.upper(char):
                res += "_" + str.lower(char)
            else:
                res += char
        if res.endswith("y"):
            return res[:-1] + "ies"
        return res + "s"


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
