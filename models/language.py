"""
language.py

This module defines the Language model, which is used to store the languages in which courses are offered 
at FCIM. This model is a key component in managing multilingual course offerings.

Attributes:
  - id (Integer): Primary key, uniquely identifying each language in the database.
  - name (String): The name of the language.

The Language model allows for the association of courses, teachers, and student groups with specific languages, 
enabling a diverse and inclusive educational environment.
"""

from sqlalchemy import Column, Integer, String
from db.base import Base

class Language(Base):
  __tablename__ = 'language'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"<Language(name={self.name})>"
