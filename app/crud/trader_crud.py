from sqlmodel import Session, select
from app.models.trader import Trader
from typing import Optional, List
from fastapi import HTTPException
from app.schemas.trader_schema import TraderUpdate

def get_trader_by_id(session: Session, trader_id: int) -> Optional[Trader]:
    return session.get(Trader, trader_id)

def create_trader(session: Session, trader: Trader) -> Trader:
    session.add(trader)
    session.commit()
    session.refresh(trader)
    return trader

def delete_trader_by_id(session: Session, trader_id: int) -> Optional[Trader]:
    trader = get_trader_by_id(session, trader_id)
    if trader:
        session.delete(trader)
        session.commit()
    return trader

def get_all_traders_from_db(session: Session) -> List[Trader]:
    statement = select(Trader)
    return session.exec(statement).all()

def update_trader_in_db(session: Session, trader_id: int, trader_update: TraderUpdate) -> Optional[Trader]:
    trader = get_trader_by_id(session, trader_id)
    if trader:
        if trader_update.balance is not None:
            trader.balance = trader_update.balance
        session.add(trader)
        session.commit()
        session.refresh(trader)
    return trader
