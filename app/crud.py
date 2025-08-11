from sqlalchemy.orm import Session
from app import models, schemas
from app.utils import get_password_hash

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str, password: str):
    hashed = get_password_hash(password)
    user = models.User(username=username, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_question(db: Session, q: schemas.QuestionCreate):
    question = models.Question(**q.dict())
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def get_all_questions(db: Session):
    return db.query(models.Question).all()

def get_question_by_id(db: Session, qid: int):
    return db.query(models.Question).filter(models.Question.id == qid).first()
