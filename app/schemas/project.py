from pydantic import BaseModel, HttpUrl
from typing import Optional

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    link: Optional[HttpUrl] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
