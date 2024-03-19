from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


SQLALCHEMY_DATABASE_URL = 'sqlite:///main.db'

SECRET_KEY = 'somesecretkey'
ALGORITHM = 'HS256'
EXPIRE_TIME = 30


engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")