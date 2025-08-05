# app/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    profile = relationship("DeveloperProfile", back_populates="user", uselist=False)
    skills = relationship("Skill", secondary="user_skills", back_populates="users")
    projects = relationship("Project", back_populates="user", cascade="all, delete")
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Integer, default=1)
