from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app import schemas

from app.auth import get_current_user

router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)


def admin_or_librarian(current_user):

    if current_user.role not in ["admin", "librarian"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin or Librarian access required"
        )

    return current_user


# ==========================
# CREATE AUTHOR
# ==========================

@router.post(
    "/",
    response_model=schemas.AuthorResponse,
    status_code=status.HTTP_201_CREATED
)
def create_author(
    author: schemas.AuthorCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    admin_or_librarian(current_user)

    new_author = models.Author(
        name=author.name,
        biography=author.biography
    )

    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    return new_author


# ==========================
# GET ALL AUTHORS
# ==========================

@router.get(
    "/",
    response_model=list[schemas.AuthorResponse]
)
def get_authors(
    db: Session = Depends(get_db)
):

    authors = db.query(models.Author).all()

    return authors


# ==========================
# GET AUTHOR BY ID
# ==========================

@router.get(
    "/{author_id}",
    response_model=schemas.AuthorResponse
)
def get_author(
    author_id: int,
    db: Session = Depends(get_db)
):

    author = (
        db.query(models.Author)
        .filter(models.Author.id == author_id)
        .first()
    )

    if not author:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )

    return author


# ==========================
# UPDATE AUTHOR
# ==========================

@router.put(
    "/{author_id}",
    response_model=schemas.AuthorResponse
)
def update_author(
    author_id: int,
    author: schemas.AuthorUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    admin_or_librarian(current_user)

    existing_author = (
        db.query(models.Author)
        .filter(models.Author.id == author_id)
        .first()
    )

    if not existing_author:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )

    existing_author.name = author.name
    existing_author.biography = author.biography

    db.commit()
    db.refresh(existing_author)

    return existing_author


# ==========================
# DELETE AUTHOR
# ==========================

@router.delete(
    "/{author_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_author(
    author_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    admin_or_librarian(current_user)

    author = (
        db.query(models.Author)
        .filter(models.Author.id == author_id)
        .first()
    )

    if not author:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )

    db.delete(author)
    db.commit()

    return None