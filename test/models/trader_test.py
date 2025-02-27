import pytest
from sqlmodel import Session, SQLModel, create_engine
from app.models.trader import Trader

# Create a test database in memory
@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_trader(session):
    trader = Trader(balance=1000.0)
    session.add(trader)
    session.commit()
    session.refresh(trader)
    assert trader.id is not None
    assert trader.balance == 1000.0

def test_update_trader(session):
    trader = Trader(balance=1000.0)
    session.add(trader)
    session.commit()
    session.refresh(trader)
    trader.balance = 2000.0
    session.add(trader)
    session.commit()
    session.refresh(trader)
    assert trader.balance == 2000.0

def test_delete_trader(session):
    trader = Trader(balance=1000.0)
    session.add(trader)
    session.commit()
    session.refresh(trader)
    session.delete(trader)
    session.commit()
    assert session.get(Trader, trader.id) is None
