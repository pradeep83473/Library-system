from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

# Basic Auth setup
security = HTTPBasic()

# Static username and password (hard-coded for simplicity)
STATIC_USERNAME = "admin"
STATIC_PASSWORD = "password123"

# Create a password context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Hash a password using bcrypt
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password
    """
    return pwd_context.verify(plain_password, hashed_password)

def authenticate(credentials: HTTPBasicCredentials):
    """
    Authenticate the user with a static username and password.
    """
    if credentials.username != STATIC_USERNAME or credentials.password != STATIC_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    """
    This function can be used as a dependency to extract the current user based on 
    the basic authentication credentials.
    """
    authenticate(credentials)  # Authenticate the user
    
    # If authentication succeeds, return the username (you can replace this with your user logic)
    return {"username": credentials.username}
