from fastapi import FastAPI
from app.api import users, books, requests
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(requests.router, prefix="/requests", tags=["Requests"])
