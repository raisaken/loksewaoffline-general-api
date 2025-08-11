from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.deps import get_db

router = APIRouter()

@router.get('/take', response_model=list[schemas.QuestionOutPublic])
def take_quiz(db: Session = Depends(get_db)):
    # For small datasets return all; in production select subset/randomize
    return crud.get_all_questions(db)

@router.post('/submit', response_model=schemas.QuizResult)
def submit_quiz(submission: schemas.QuizSubmission, db: Session = Depends(get_db)):
    total = 0
    correct = 0
    details = []
    for ans in submission.answers:
        q = crud.get_question_by_id(db, ans.question_id)
        if not q:
            raise HTTPException(status_code=400, detail=f"Question id {ans.question_id} not found")
        total += 1
        is_correct = (ans.answer.strip().upper() == q.correct_answer.strip().upper())
        if is_correct:
            correct += 1
        details.append({"question_id": q.id, "your_answer": ans.answer, "correct_answer": q.correct_answer, "correct": is_correct})
    return {"total": total, "correct": correct, "details": details}
