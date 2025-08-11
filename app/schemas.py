from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class QuestionCreate(BaseModel):
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str

class QuestionOutPublic(BaseModel):
    id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    class Config:
        orm_mode = True

class QuestionOutAdmin(QuestionOutPublic):
    correct_answer: str

class AnswerIn(BaseModel):
    question_id: int
    answer: str

class QuizSubmission(BaseModel):
    answers: List[AnswerIn]

class QuizResult(BaseModel):
    total: int
    correct: int
    details: List[dict]
