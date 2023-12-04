"""
pair.py

This module defines the Pair model, representing the associations between student groups and 
course sessions in the FCIM system. Each instance of Pair connects a specific group with a 
particular course session, enabling the organization and scheduling of classes for different groups.

Attributes:
  - id (Integer): Primary key, uniquely identifying each pairing.
  - groupId (Integer): Foreign key linking to the Group model, representing the student group.
  - courseSessionId (Integer): Foreign key linking to the CourseSession model, representing the scheduled course session.

Relationships:
  - group: Relationship to the Group model, providing details about the student group.
  - courseSession: Relationship to the CourseSession model, providing details about the course session.

This model is essential for managing the timetable and class schedules, ensuring that each student group 
is associated with the correct course sessions.
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from .group import Group
from .courseSession import CourseSession

class Pair(Base):
  __tablename__ = 'pair'

  id = Column(Integer, primary_key=True, autoincrement=True)
  groupId = Column(Integer, ForeignKey('studyGroup.id'), nullable=False)
  courseSessionId = Column(Integer, ForeignKey('courseSession.id'), nullable=False)

  group = relationship("Group")
  courseSession = relationship("CourseSession")

  def __repr__(self):
    return f"<Pair(groupId={self.groupId}, courseSessionId={self.courseSessionId})>"