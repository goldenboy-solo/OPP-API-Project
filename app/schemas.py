from pydantic import BaseModel, EmailStr
from datetime import datetime


# ==========================
# TOKEN
# ==========================

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


# ==========================
# USER
# ==========================

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "member"


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ==========================
# AUTHOR
# ==========================

class AuthorCreate(BaseModel):
    name: str
    biography: str | None = None


class AuthorUpdate(BaseModel):
    name: str
    biography: str | None = None


class AuthorResponse(BaseModel):
    id: int
    name: str
    biography: str | None = None

    class Config:
        from_attributes = True


# ==========================
# BOOK
# ==========================

class BookCreate(BaseModel):
    title: str
    isbn: str
    publication_year: int
    copies_available: int
    author_id: int


class BookUpdate(BaseModel):
    title: str
    isbn: str
    publication_year: int
    copies_available: int
    author_id: int


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    publication_year: int
    copies_available: int
    author_id: int

    class Config:
        from_attributes = True


# ==========================
# REVIEW
# ==========================

class ReviewCreate(BaseModel):
    rating: int
    comment: str
    book_id: int


class ReviewUpdate(BaseModel):
    rating: int
    comment: str


class ReviewResponse(BaseModel):
    id: int
    rating: int
    comment: str
    user_id: int
    book_id: int

    class Config:
        from_attributes = True


# ==========================
# BORROW
# ==========================

class BorrowResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    status: str
    borrow_date: datetime
    return_date: datetime | None

    class Config:
        from_attributes = True