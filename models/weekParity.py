"""
weekParity.py

This module defines the WeekParity model, used to differentiate between even and odd weeks for 
the scheduling of courses. This model is particularly useful for courses or sessions that 
are planned to occur bi-weekly, either in even or odd weeks.

Attributes:
  - id (Integer): Primary key, uniquely identifying the week parity.
  - name (String): The designation of the week parity (e.g., 'Even', 'Odd').

The WeekParity model aids in the organization of the academic schedule, especially for managing 
courses with alternating weekly sessions, ensuring accurate and efficient planning.
"""

from sqlalchemy import Column, Integer, String
from db.base import Base

class WeekParity(Base):
  __tablename__ = 'weekParity'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"<WeekParity(name={self.name})>"