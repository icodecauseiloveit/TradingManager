import pytest
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import user_routes
from app.database import create_db_and_tables

def run_tests():
    pytest.main(["-v", "test", "--disable-warnings"])

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    run_tests()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_routes.router)


# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# uvicorn app.main:app --reload

# curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{"username": "newuser", "email": "newuser@example.com", "password": "securepassword"}'