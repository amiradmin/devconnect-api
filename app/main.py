from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user

app = FastAPI(title="DevConnect API", version="1.0.0")

# Auto-create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to DevConnect API"}
