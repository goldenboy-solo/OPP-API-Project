from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from datetime import datetime
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app import schemas

from app.auth import get_current_user

import asyncio

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


def admin_or_librarian(current_user):
    if current_user.role not in ["admin", "librarian"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin or Librarian access required"
        )

    return current_user


# ==========================
# CREATE BOOK
# ==========================

@router.post(
    "/",
    response_model=schemas.BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    admin_or_librarian(current_user)

    author = (
        db.query(models.Author)
        .filter(models.Author.id == book.author_id)
        .first()
    )

    if not author:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )

    new_book = models.Book(
        title=book.title,
        isbn=book.isbn,
        publication_year=book.publication_year,
        copies_available=book.copies_available,
        author_id=book.author_id
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


# ==========================
# GET ALL BOOKS
# ==========================

@router.get(
    "/",
    response_model=list[schemas.BookResponse]
)
def get_books(
    db: Session = Depends(get_db)
):
    books = db.query(models.Book).all()
    return books


# ==========================
# GET BOOK BY ID
# ==========================

@router.get(
    "/{book_id}",
    response_model=schemas.BookResponse
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .first()
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


# ==========================
# UPDATE BOOK
# ==========================

@router.put(
    "/{book_id}",
    response_model=schemas.BookResponse
)
def update_book(
    book_id: int,
    book: schemas.BookUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    admin_or_librarian(current_user)

    existing_book = (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .first()
    )

    if not existing_book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    existing_book.title = book.title
    existing_book.isbn = book.isbn
    existing_book.publication_year = book.publication_year
    existing_book.copies_available = book.copies_available
    existing_book.author_id = book.author_id

    db.commit()
    db.refresh(existing_book)

    return existing_book


# ==========================
# DELETE BOOK
# ==========================

@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    admin_or_librarian(current_user)

    book = (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .first()
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)
    db.commit()

    return None


# ==========================
# SEARCH BOOKS (ASYNC)
# ==========================

@router.get("/search")
async def search_books(
    title: str,
    db: Session = Depends(get_db)
):
    await asyncio.sleep(1)

    books = (
        db.query(models.Book)
        .filter(
            models.Book.title.ilike(f"%{title}%")
        )
        .all()
    )

    return books


@router.post("/borrow/{book_id}")
def borrow_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    if current_user.role not in ["admin", "librarian"]:
        raise HTTPException(
            status_code=403,
            detail="Only librarians and admins can borrow books"
        )

    book = (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .first()
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    if book.copies_available <= 0:
        raise HTTPException(
            status_code=400,
            detail="No copies available"
        )

    borrow_record = models.BorrowRecord(
        user_id=current_user.id,
        book_id=book.id,
        status="borrowed"
    )

    book.copies_available -= 1

    db.add(borrow_record)
    db.commit()

    return {
        "message": "Book borrowed successfully"
    }


@router.post("/return/{book_id}")
def return_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    borrow_record = (
        db.query(models.BorrowRecord)
        .filter(
            models.BorrowRecord.book_id == book_id,
            models.BorrowRecord.status == "borrowed"
        )
        .first()
    )

    if not borrow_record:
        raise HTTPException(
            status_code=404,
            detail="Borrow record not found"
        )

    borrow_record.status = "returned"
    borrow_record.return_date = datetime.utcnow()

    book = (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .first()
    )

    if book:
        book.copies_available += 1

    db.commit()

    return {
        "message": "Book returned successfully"
    }