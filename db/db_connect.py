"""
db_connect.py

This module establishes the connection to the MySQL database using SQLAlchemy. 
It sets up the database engine and sessionmaker for interacting with the database.

The database URL and credentials are retrieved from environment variables for security.

Exceptions are handled to ensure a graceful degradation in case of connection issues.
"""

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from config.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

# Constructing the Database URL for connection
DATABASE_URL = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Creating the database engine with the specified URL
try:
  engine = create_engine(DATABASE_URL)
except exc.SQLAlchemyError as e:
  print(f"Error connecting to the database: {e}")
  raise

# Creating a sessionmaker, bound to the engine, for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)