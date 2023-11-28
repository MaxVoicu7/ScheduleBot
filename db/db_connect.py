from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE_URL = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)