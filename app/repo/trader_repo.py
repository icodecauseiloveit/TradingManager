from sqlmodel import Session
from typing import Optional, List
from app.models.trader import Trader
from app.crud.trader_crud import get_trader_by_id, create_trader, delete_trader_by_id, get_all_traders_from_db, update_trader_in_db
from app.schemas.trader_schema import TraderUpdate

def get_trader(session: Session, trader_id: int) -> Optional[Trader]:
    return get_trader_by_id(session, trader_id)

def add_trader(session: Session, trader: Trader) -> Trader:
    return create_trader(session, trader)

def delete_trader(session: Session, trader_id: int) -> Optional[Trader]:
    return delete_trader_by_id(session, trader_id)

def get_all_traders(session: Session) -> List[Trader]:
    return get_all_traders_from_db(session)

def update_trader(session: Session, trader_id: int, trader_update: TraderUpdate) -> Optional[Trader]:
    return update_trader_in_db(session, trader_id, trader_update)
