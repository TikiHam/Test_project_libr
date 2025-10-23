from SQLAlchemy import Column, Integer, String
from SQLAlchemy.orm import declarative_base
from passlib import CryptContext

Base = declarative_base()
pwd_context = CryptContext(shcems=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer)