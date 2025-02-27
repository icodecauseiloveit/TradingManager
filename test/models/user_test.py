import pytest
from sqlmodel import Session, SQLModel, create_engine
from app.models.user import User

# Create a test database in memory
@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_user(session):
    user = User(username="testuser", email="testuser@example.com", hashed_password="hashedpassword")
    session.add(user)
    session.commit()
    session.refresh(user)
    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"

def test_unique_username(session):
    user1 = User(username="testuser", email="testuser1@example.com", hashed_password="hashedpassword1")
    user2 = User(username="testuser", email="testuser2@example.com", hashed_password="hashedpassword2")
    session.add(user1)
    session.commit()
    with pytest.raises(Exception):
        session.add(user2)
        session.commit()

def test_unique_email(session):
    user1 = User(username="testuser1", email="testuser@example.com", hashed_password="hashedpassword1")
    user2 = User(username="testuser2", email="testuser@example.com", hashed_password="hashedpassword2")
    session.add(user1)
    session.commit()
    with pytest.raises(Exception):
        session.add(user2)
        session.commit()