from pydantic import BaseModel, HttpUrl
from typing import Optional

class DeveloperProfileBase(BaseModel):
    bio: Optional[str] = None
    location: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    linkedin_url: Optional[HttpUrl] = None

class DeveloperProfileCreate(DeveloperProfileBase):
    pass

class DeveloperProfileUpdate(DeveloperProfileBase):
    pass

class DeveloperProfileOut(DeveloperProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
