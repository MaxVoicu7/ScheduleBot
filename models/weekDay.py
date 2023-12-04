"""
weekDay.py

This module defines the WeekDay model, which represents the days of the week. 
This basic but essential model is used in scheduling and organizing academic and administrative activities 
throughout the week.

Attributes:
  - id (Integer): Primary key, uniquely identifying each day of the week.
  - day (String): The name of the day (e.g., Monday, Tuesday, etc.).

The WeekDay model is instrumental in structuring and planning the weekly academic schedule, allowing for 
the assignment of classes, meetings, and other activities to specific days of the week.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base

class WeekDay(Base):
  __tablename__ = 'weekDay'

  id = Column(Integer, primary_key=True, autoincrement=True)
  day = Column(String, nullable=False)

  def __repr__(self):
    return f"<WeekDay(day={self.day})>"