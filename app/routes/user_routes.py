from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.schemas.user_schema import UserCreate, UserRead, UserUpdate
from app.repo.user_repo import get_user, add_user, delete_user, get_all_users, update_user
from app.database import get_session
from app.models.user import User
from app.security import get_password_hash

router = APIRouter()

@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session)):
    db_user = get_user(session, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/list-users/", response_model=List[UserRead])
def list_users(session: Session = Depends(get_session)):
    return get_all_users(session)

@router.post("/create-user/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    hashed_password = get_password_hash(user.password)
    db_user = add_user(session, User(username=user.username, email=user.email, hashed_password=hashed_password))
    return db_user

@router.delete("/users/{user_id}", response_model=UserRead)
def remove_user(user_id: int, session: Session = Depends(get_session)):
    db_user = delete_user(session, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/del-all-users/", response_model=List[UserRead])
def delete_all_users(session: Session = Depends(get_session)):
    db_users = get_all_users(session)
    for user in db_users:
        delete_user(session, user.id)
    return db_users

@router.put("/update-user/{user_id}", response_model=UserRead)
def update_user_route(user_id: int, user: UserUpdate, session: Session = Depends(get_session)):
    db_user = update_user(session, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
