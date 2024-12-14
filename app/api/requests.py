from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.security import get_current_user
from .. import models

router = APIRouter()

@router.post("/create_book/")
def create_book_request(book_request: schemas.BookRequestCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_book_request(db=db, book_request=book_request)

@router.get("/get_all_book/")
def get_all_book_requests(db: Session = Depends(get_db)):
    return crud.get_all_book_requests(db=db)

@router.put("/{book_request_id}/approve/")
def approve_book_request(book_request_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.approve_book_request(db=db, book_request_id=book_request_id)
