from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str
    quantity: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class BookRequestBase(BaseModel):
    user_id: int
    book_id: int
    start_date: date
    end_date: date

class BookRequestCreate(BookRequestBase):
    pass

class BookRequest(BookRequestBase):
    id: int
    status: str

    class Config:
        orm_mode = True
