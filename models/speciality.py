"""
speciality.py

This module defines the Speciality model, representing the various academic specialities 
available at FCIM. Each speciality is characterized by its name, the total number of 
semesters required for completion, and a unique abbreviation.

Attributes:
  - id (Integer): Primary key, uniquely identifying each speciality.
  - name (String): The full name of the speciality.
  - semesters (Integer): The total number of semesters required to complete the speciality.
  - abbreviation (String): A short, unique abbreviation for the speciality.

The Speciality model is essential for categorizing students and organizing academic programs, 
courses, and schedules according to different fields of study.
"""

from sqlalchemy import Column, Integer, String
from db.base import Base

class Speciality(Base):
  __tablename__ = 'speciality'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  semesters = Column(Integer, nullable=False)
  abbreviation = Column(String, nullable=False)

  def __repr__(self):
    return f"<Speciality(name={self.name}, semesters={self.semesters}, abbreviation={self.abbreviation})>"
