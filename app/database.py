# sqlite database setup
# This code sets up the database connection and session management for a FastAPI application using SQLAlchemy
# It uses a settings module to retrieve the database URL and configures the engine, session, and base model.
# Uncomment the following lines if you are using SQLite and need to allow multiple threads to access the database.
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from app.config import settings

# connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
# engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()