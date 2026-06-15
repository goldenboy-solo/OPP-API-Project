from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post(
    "/",
    response_model=schemas.ReviewResponse,
    status_code=status.HTTP_201_CREATED
)
def create_review(
    review: schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    book = (
        db.query(models.Book)
        .filter(models.Book.id == review.book_id)
        .first()
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    new_review = models.Review(
        rating=review.rating,
        comment=review.comment,
        book_id=review.book_id,
        user_id=current_user.id
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review


@router.get("/", response_model=list[schemas.ReviewResponse])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(models.Review).all()


@router.get("/{review_id}", response_model=schemas.ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):

    review = (
        db.query(models.Review)
        .filter(models.Review.id == review_id)
        .first()
    )

    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review


@router.put("/{review_id}", response_model=schemas.ReviewResponse)
def update_review(
    review_id: int,
    review: schemas.ReviewUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    existing_review = (
        db.query(models.Review)
        .filter(models.Review.id == review_id)
        .first()
    )

    if not existing_review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    existing_review.rating = review.rating
    existing_review.comment = review.comment

    db.commit()
    db.refresh(existing_review)

    return existing_review


@router.delete("/{review_id}")
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    review = (
        db.query(models.Review)
        .filter(models.Review.id == review_id)
        .first()
    )

    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    db.delete(review)
    db.commit()

    return {"message": "Review deleted successfully"}