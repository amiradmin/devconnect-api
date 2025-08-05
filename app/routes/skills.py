# app/routes/skills.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.skill import SkillCreate, SkillOut
from app.models.skill import Skill
from app.models.user import User
from app.core.database import get_db
from app.core.auth import get_current_user

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.get("/", response_model=list[SkillOut])
def list_skills(db: Session = Depends(get_db)):
    return db.query(Skill).all()

@router.post("/", response_model=SkillOut)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    db_skill = db.query(Skill).filter_by(name=skill.name).first()
    if db_skill:
        return db_skill
    new_skill = Skill(name=skill.name)
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

@router.post("/add/{skill_id}")
def add_skill_to_user(skill_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    if skill in user.skills:
        raise HTTPException(status_code=400, detail="Skill already added")
    user.skills.append(skill)
    db.commit()
    return {"message": "Skill added"}

@router.delete("/remove/{skill_id}")
def remove_skill_from_user(skill_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill or skill not in user.skills:
        raise HTTPException(status_code=404, detail="Skill not associated with user")
    user.skills.remove(skill)
    db.commit()
    return {"message": "Skill removed"}
