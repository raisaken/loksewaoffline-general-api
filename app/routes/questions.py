from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.deps import get_db, get_current_user

router = APIRouter()

@router.get('/', response_model=list[schemas.QuestionOutPublic])
def list_questions(db: Session = Depends(get_db)):
    qs = crud.get_all_questions(db)
    return qs

@router.post('/admin', response_model=schemas.QuestionOutAdmin)
def add_question(q: schemas.QuestionCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    # In real app, check user roles. Here any logged-in user can add questions for simplicity.
    new_q = crud.create_question(db, q)
    return new_q
