# Library Management System

This is a simple **Library Management System** built using **FastAPI** and **SQLAlchemy** with SQLite as the database. It allows librarians (admin) to manage users, book requests, and borrow histories, and allows regular users to request books and view their borrow history.

## Features

- **Librarian (Admin) Features**:
  - Create new library users (with email and password).
  - View all book borrow requests.
  - Approve or deny book borrow requests.
  - View a user's book borrow history.

- **Library User Features**:
  - Request a book to borrow for specific dates.
  - View personal book borrow history.

- **Book Borrowing Rules**:
  - A book cannot be borrowed by more than one user during the same period (unless there are multiple copies of the same book).
  - The system ensures role-based access control with `admin` and `user` roles for the library users.

- **Basic Authentication**: API endpoints are protected using basic authentication.

## Tech Stack

- **FastAPI**: For building the web API.
- **SQLAlchemy**: For ORM and database interactions.
- **SQLite**: As the database engine.
- **Pydantic**: For data validation and serialization.
- **Uvicorn**: For serving the FastAPI application.

## Installation

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

