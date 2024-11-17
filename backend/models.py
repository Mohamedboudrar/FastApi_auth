# backend/models.py
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(255), unique=True, index=True)
    name = Column(String(255), unique=True, index=True)  # Add a length to String
    hashed_password = Column(String(255))  # Add a length to String
