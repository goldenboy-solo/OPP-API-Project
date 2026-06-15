from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    hashed_password = Column(String(255), nullable=False)

    role = Column(String(20), default="member")

    created_at = Column(DateTime, default=datetime.utcnow)

    reviews = relationship(
        "Review",
        back_populates="user",
        cascade="all, delete"
    )

    borrow_records = relationship(
        "BorrowRecord",
        back_populates="user",
        cascade="all, delete"
    )


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    biography = Column(Text)

    books = relationship(
        "Book",
        back_populates="author",
        cascade="all, delete"
    )


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    isbn = Column(String(50), unique=True, nullable=False)

    publication_year = Column(Integer)

    copies_available = Column(Integer, default=1)

    created_at = Column(DateTime, default=datetime.utcnow)

    author_id = Column(
        Integer,
        ForeignKey("authors.id", ondelete="CASCADE")
    )

    author = relationship(
        "Author",
        back_populates="books"
    )

    reviews = relationship(
        "Review",
        back_populates="book",
        cascade="all, delete"
    )

    borrow_records = relationship(
        "BorrowRecord",
        back_populates="book",
        cascade="all, delete"
    )


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    rating = Column(Integer, nullable=False)

    comment = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    book_id = Column(
        Integer,
        ForeignKey("books.id", ondelete="CASCADE")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE")
    )

    book = relationship(
        "Book",
        back_populates="reviews"
    )

    user = relationship(
        "User",
        back_populates="reviews"
    )


class BorrowRecord(Base):
    __tablename__ = "borrow_records"

    id = Column(Integer, primary_key=True, index=True)

    borrow_date = Column(DateTime, default=datetime.utcnow)

    return_date = Column(DateTime, nullable=True)

    status = Column(String(20), default="borrowed")

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE")
    )

    book_id = Column(
        Integer,
        ForeignKey("books.id", ondelete="CASCADE")
    )

    user = relationship(
        "User",
        back_populates="borrow_records"
    )

    book = relationship(
        "Book",
        back_populates="borrow_records"
    )
