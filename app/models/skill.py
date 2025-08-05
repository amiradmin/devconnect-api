# app/models/skill.py
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

user_skills = Table(
    "user_skills",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("skill_id", Integer, ForeignKey("skills.id"))
)

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    users = relationship("User", secondary=user_skills, back_populates="skills")
