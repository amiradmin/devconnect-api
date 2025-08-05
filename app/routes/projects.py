# app/routes/projects.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.project import ProjectCreate, ProjectOut, ProjectUpdate
from app.models.project import Project
from app.models.user import User
from app.core.database import get_db
from app.core.auth import get_current_user

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectOut)
def create_project(project: ProjectCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    new_project = Project(**project.dict(), user_id=user.id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@router.get("/me", response_model=list[ProjectOut])
def get_own_projects(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(Project).filter_by(user_id=user.id).all()

@router.put("/{project_id}", response_model=ProjectOut)
def update_project(project_id: int, update: ProjectUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    project = db.query(Project).filter_by(id=project_id, user_id=user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    for key, value in update.dict(exclude_unset=True).items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    project = db.query(Project).filter_by(id=project_id, user_id=user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"message": "Project deleted"}
