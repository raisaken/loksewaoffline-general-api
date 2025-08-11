import os
from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import auth, questions, quiz

# create tables (for simple dev). Use Alembic in production.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quiz API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(questions.router, prefix="/questions", tags=["questions"])
app.include_router(quiz.router, prefix="/quiz", tags=["quiz"])

@app.get("/")
def root():
    return {"status": "ok", "message": "Quiz API"}
