from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas, utils
from app.deps import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post('/register', response_model=schemas.Token)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, username=user.username)
    if existing:
        raise HTTPException(status_code=400, detail='Username already registered')
    new_user = crud.create_user(db, username=user.username, password=user.password)
    token = utils.create_access_token(subject=new_user.username)
    return {'access_token': token, 'token_type': 'bearer'}

@router.post('/login', response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not utils.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    token = utils.create_access_token(subject=user.username)
    return {'access_token': token, 'token_type': 'bearer'}
