from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Author(Base):

    __tablename__ = "author"

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    # Relationships
    books = relationship("Book", back_populates="author")

class Book(Base):

    __tablename__ = "book"

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    # Relationships
    author = relationship("Author", back_populates="books")

