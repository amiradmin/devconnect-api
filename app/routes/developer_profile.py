from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.developer_profile import DeveloperProfileCreate, DeveloperProfileOut, DeveloperProfileUpdate
from app.models.developer_profile import DeveloperProfile
from app.models.user import User
from app.core.database import get_db
from app.core.auth import get_current_user

router = APIRouter(prefix="/profile", tags=["Developer Profile"])

@router.post("/", response_model=DeveloperProfileOut)
def create_profile(profile: DeveloperProfileCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    existing = db.query(DeveloperProfile).filter_by(user_id=user.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Profile already exists")

    dev_profile = DeveloperProfile(**profile.dict(), user_id=user.id)
    db.add(dev_profile)
    db.commit()
    db.refresh(dev_profile)
    return dev_profile

@router.get("/me", response_model=DeveloperProfileOut)
def get_own_profile(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    profile = db.query(DeveloperProfile).filter_by(user_id=user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.put("/me", response_model=DeveloperProfileOut)
def update_own_profile(data: DeveloperProfileUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    profile = db.query(DeveloperProfile).filter_by(user_id=user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(profile, key, value)
    db.commit()
    db.refresh(profile)
    return profile
