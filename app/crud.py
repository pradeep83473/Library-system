from sqlalchemy.orm import Session
from app import models, schemas
from app.security import get_password_hash



def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)  # Hash the password before storing it
    db_user = models.User(email=user.email, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Book CRUD operations
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author=book.author, quantity=book.quantity)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

# Book Request CRUD operations
def create_book_request(db: Session, book_request: schemas.BookRequestCreate):
    db_book_request = models.BookRequest(
        user_id=book_request.user_id,
        book_id=book_request.book_id,
        start_date=book_request.start_date,
        end_date=book_request.end_date
    )
    db.add(db_book_request)
    db.commit()
    db.refresh(db_book_request)
    return db_book_request

def get_all_book_requests(db: Session):
    return db.query(models.BookRequest).all()

def approve_book_request(db: Session, book_request_id: int):
    db_request = db.query(models.BookRequest).filter(models.BookRequest.id == book_request_id).first()
    if db_request:
        db_request.status = 'approved'
        db.commit()
        db.refresh(db_request)
        return db_request
    return None
