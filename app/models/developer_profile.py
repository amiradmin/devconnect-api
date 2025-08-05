# app/models/developer_profile.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class DeveloperProfile(Base):
    __tablename__ = "developer_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    bio = Column(String, nullable=True)
    location = Column(String, nullable=True)
    github_url = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)

    user = relationship("User", back_populates="profile")
