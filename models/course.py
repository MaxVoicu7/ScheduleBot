"""
course.py

This module defines the Course model, representing various courses offered to students, such as 'Databases', 
'Object-Oriented Programming', etc., in the database using SQLAlchemy ORM.

Attributes:
  - id (Integer): The primary key, which uniquely identifies each course.
  - name (String): A string field to store the name of the course.

The Course model creates a table named 'course' in the database, where 'id' is an autoincremented primary 
key and 'name' is a required field.
"""

from sqlalchemy import Column, Integer, String
from db.base import Base

class Course(Base):
  __tablename__ = 'course'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"<Course(name={self.name})>"