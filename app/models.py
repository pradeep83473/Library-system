from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)

    book_requests = relationship("BookRequest", back_populates="user")
    borrow_history = relationship("BookBorrowHistory", back_populates="user")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    quantity = Column(Integer)

    book_requests = relationship("BookRequest", back_populates="book")
    borrow_history = relationship("BookBorrowHistory", back_populates="book")

class BookRequest(Base):
    __tablename__ = 'book_requests'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String, default='pending')

    user = relationship("User", back_populates="book_requests")
    book = relationship("Book", back_populates="book_requests")

class BookBorrowHistory(Base):
    __tablename__ = 'book_borrow_history'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    start_date = Column(Date)
    end_date = Column(Date)

    user = relationship("User", back_populates="borrow_history")
    book = relationship("Book", back_populates="borrow_history")
