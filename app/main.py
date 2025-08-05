from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import developer_profile, skills, projects
from app.routes import auth


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(developer_profile.router)
app.include_router(skills.router)
app.include_router(projects.router)
app.include_router(auth.router)

# @app.on_event("startup")
# def on_startup():
#     create_tables()