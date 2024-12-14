from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from .. import models
from app.security import get_current_user

router = APIRouter()

@router.post("/create_book/")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_book(db=db, book=book)

@router.get("/get_book/")
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)
