"""
sessionSchedule.py

This module defines the SessionSchedule model, which represents time intervals for academic 
sessions or classes. Each instance of SessionSchedule specifies a start and end time, 
denoting the duration of a particular class or session.

Attributes:
  - id (Integer): Primary key, uniquely identifying each session schedule in the database.
  - startTime (Time): The start time of the academic session.
  - endTime (Time): The end time of the academic session.

This model is crucial for planning and organizing the daily schedule of classes, allowing for 
a clear and structured timetable to be established for students and faculty.
"""

from sqlalchemy import Column, Integer, Time
from db.base import Base

class SessionSchedule(Base):
  __tablename__ = 'sessionSchedule'

  id = Column(Integer, primary_key=True, autoincrement=True)
  startTime = Column(Time, nullable=False)
  endTime = Column(Time, nullable=False)

  def __repr__(self):
    return f"<SessionSchedule(start_time={self.startTime}, end_time={self.endTime})>"