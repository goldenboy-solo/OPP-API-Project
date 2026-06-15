from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app import schemas

from app.auth import (
    get_current_user, hash_password
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def admin_only(current_user):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user


# ==========================
# GET ALL USERS
# ==========================

@router.get(
    "/",
    response_model=list[schemas.UserResponse]
)
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    admin_only(current_user)

    users = db.query(models.User).all()

    return users


# ==========================
# GET USER BY ID
# ==========================

@router.get(
    "/{user_id}",
    response_model=schemas.UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    admin_only(current_user)

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# ==========================
# DELETE USER
# ==========================
@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            403,
            "Admin only"
        )

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            404,
            "User not found"
        )

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}

@router.post("/")
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            403,
            "Admin only"
        )

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}