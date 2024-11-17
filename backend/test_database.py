# test_database.py
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import User
from auth import get_password_hash

Base.metadata.create_all(bind=engine)

# Create a test session
db: Session = next(get_db())

# Add a new user manually
try:
    new_user = User(email="testuser@example.com", hashed_password=get_password_hash("password123"))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print("User created successfully:", new_user.email)
except Exception as e:
    print("Error creating user:", e)
finally:
    db.close()
