# sqlite:///./quiz.db
# This code sets up the database connection and session management for a FastAPI application using SQLAlchemy
# It uses a settings module to retrieve the database URL and configures the engine, session, and base model.
# Uncomment the following lines if you are using SQLite and need to allow multiple threads to access the database.
# from sqlalchemy import create_engine
# import os
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./quiz.db")
#     SECRET_KEY: str = os.getenv("SECRET_KEY", "change_this_for_dev")
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

# settings = Settings()


import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Quiz App"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/postgres")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

settings = Settings()
