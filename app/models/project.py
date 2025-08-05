# app/models/project.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    link = Column(String, nullable=True)

    user = relationship("User", back_populates="projects")
