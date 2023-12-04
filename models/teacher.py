"""
teacher.py

This module defines the Teacher model, used to represent faculty members or teachers at FCIM. 
Each teacher is identified by their name, and this model allows for the association of teachers 
with courses, course sessions, and other academic activities.

Attributes:
  - id (Integer): Primary key, uniquely identifying each teacher.
  - name (String): The name of the teacher.

The Teacher model is vital in creating relationships between courses and the instructors who teach them, 
facilitating the management of course schedules and academic records.
"""

from sqlalchemy import Column, Integer, String
from db.base import Base

class Teacher(Base):
  __tablename__ = 'teacher'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"<Teacher(name={self.name})>"