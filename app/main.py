from fastapi import FastAPI

app = FastAPI(title="DevConnect API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Welcome to DevConnect API"}
