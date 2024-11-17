# backend/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from models import Base, User
from database import engine, get_db
from schemas import UserCreate, UserOut, LoginRequest
from auth import verify_password, get_password_hash, create_access_token
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

origins = [
    "http://localhost:5173",  # allow your frontend app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # allows all headers
)



# Create database tables
Base.metadata.create_all(bind=engine)

@app.post("/signup", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password, name=user.name )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@app.post("/login")
def login_for_access_token(login_request: LoginRequest, db: Session = Depends(get_db)):
    # Extract username (email) and password from the JSON request body
    user = db.query(User).filter(User.email == login_request.username).first()
    
    if not user or not verify_password(login_request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}