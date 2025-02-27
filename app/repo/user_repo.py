from sqlmodel import Session
from typing import Optional, List
from app.models.user import User
from app.crud.user_crud import get_user_by_id, get_user_by_username, get_user_by_email, create_user, delete_user_by_id, get_all_users_from_db, update_user_in_db
from app.schemas.user_schema import UserUpdate

def get_user(session: Session, user_id: int) -> Optional[User]:
    return get_user_by_id(session, user_id)

def get_user_by_name(session: Session, username: str) -> Optional[User]:
    return get_user_by_username(session, username)

def get_user_by_email(session: Session, email: str) -> Optional[User]:
    return get_user_by_email(session, email)

def add_user(session: Session, user: User) -> User:
    return create_user(session, user)

def delete_user(session: Session, user_id: int) -> Optional[User]:
    return delete_user_by_id(session, user_id)

def get_all_users(session: Session) -> List[User]:
    return get_all_users_from_db(session)

def update_user(session: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    return update_user_in_db(session, user_id, user_update)
