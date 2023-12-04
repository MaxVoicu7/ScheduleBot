"""
activityType.py

This module defines the ActivityType model, which represents different types of course activities 
(such as lectures, seminars, and laboratories) in the database using SQLAlchemy ORM.

Attributes:
  - id (Integer): The primary key, which uniquely identifies each activity type.
  - name (String): A string field to store the name of the activity type, like 'lecture', 'seminar', etc.

The ActivityType model is used to create a table named 'activityType' in the database, with 'id' as an 
autoincremented primary key and 'name' as a non-nullable field.
"""

from sqlalchemy import Column, Integer, String
from db.base import Base

class ActivityType(Base):
  __tablename__ = 'activityType'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"<ActivityType(name={self.name})>"