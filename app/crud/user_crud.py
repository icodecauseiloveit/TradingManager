from sqlmodel import Session, select
from app.models.user import User
from typing import Optional, List
from fastapi import HTTPException
from app.schemas.user_schema import UserUpdate
from app.security import get_password_hash

def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
    return session.get(User, user_id)

def get_user_by_username(session: Session, username: str) -> Optional[User]:
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()

def get_user_by_email(session: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def create_user(session: Session, user: User) -> User:
    if get_user_by_username(session, user.username) or get_user_by_email(session, user.email):
        raise HTTPException(status_code=400, detail="Username or email already exists")
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user_by_id(session: Session, user_id: int) -> Optional[User]:
    user = get_user_by_id(session, user_id)
    if user:
        session.delete(user)
        session.commit()
    return user

def get_all_users_from_db(session: Session) -> List[User]:
    statement = select(User)
    return session.exec(statement).all()

def update_user_in_db(session: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    user = get_user_by_id(session, user_id)
    if user:
        if user_update.username:
            user.username = user_update.username
        if user_update.email:
            user.email = user_update.email
        if user_update.password:
            user.hashed_password = get_password_hash(user_update.password)
        session.add(user)
        session.commit()
        session.refresh(user)
    return user
