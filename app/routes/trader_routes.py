from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.schemas.trader_schema import TraderCreate, TraderRead, TraderUpdate
from app.repo.trader_repo import get_trader, add_trader, delete_trader, get_all_traders, update_trader
from app.database import get_session
from app.models.trader import Trader

router = APIRouter()

@router.get("/traders/{trader_id}", response_model=TraderRead)
def read_trader(trader_id: int, session: Session = Depends(get_session)):
    db_trader = get_trader(session, trader_id)
    if db_trader is None:
        raise HTTPException(status_code=404, detail="Trader not found")
    return db_trader

@router.get("/list-traders/", response_model=List[TraderRead])
def list_traders(session: Session = Depends(get_session)):
    return get_all_traders(session)

@router.post("/create-trader/", response_model=TraderRead)
def create_trader(trader: TraderCreate, session: Session = Depends(get_session)):
    db_trader = add_trader(session, Trader(balance=trader.balance))
    return db_trader

@router.delete("/traders/{trader_id}", response_model=TraderRead)
def remove_trader(trader_id: int, session: Session = Depends(get_session)):
    db_trader = delete_trader(session, trader_id)
    if db_trader is None:
        raise HTTPException(status_code=404, detail="Trader not found")
    return db_trader

@router.put("/update-trader/{trader_id}", response_model=TraderRead)
def update_trader_route(trader_id: int, trader: TraderUpdate, session: Session = Depends(get_session)):
    db_trader = update_trader(session, trader_id, trader)
    if db_trader is None:
        raise HTTPException(status_code=404, detail="Trader not found")
    return db_trader
