"""
courseSession.py

This module defines the CourseSession model, which represents the scheduling details of a course session 
in the educational system. It includes information like the course, teacher, type of activity (lecture, lab, etc.), 
day and time of the session, location (room), and week parity (every week, even weeks only, etc.).

Attributes:
  - id (Integer): Primary key, uniquely identifying each course session.
  - courseId (Integer): Foreign key linking to the Course model.
  - teacherId (Integer): Foreign key linking to the Teacher model.
  - activityTypeId (Integer): Foreign key linking to the ActivityType model.
  - weekDayId (Integer): Foreign key linking to the WeekDay model.
  - sessionTimeId (Integer): Foreign key linking to the SessionSchedule model.
  - roomId (Integer): Foreign key linking to the Room model.
  - weekParityId (Integer): Optional foreign key linking to the WeekParity model. If null, the session occurs every week.

Relationships:
  - course, teacher, activityType, weekDay, sessionSchedule, room, weekParity: Establish relationships with respective models.

This model is vital for organizing the schedule and logistical aspects of course sessions, linking various aspects 
of academic scheduling in a cohesive structure.
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from .course import Course
from .teacher import Teacher
from .activityType import ActivityType
from .weekDay import WeekDay
from .sessionSchedule import SessionSchedule
from .room import Room
from .weekParity import WeekParity

class CourseSession(Base):
  __tablename__ = 'courseSession'

  id = Column(Integer, primary_key=True, autoincrement=True)
  courseId = Column(Integer, ForeignKey('course.id'), nullable=False)
  teacherId = Column(Integer, ForeignKey('teacher.id'), nullable=False)
  activityTypeId = Column(Integer, ForeignKey('activityType.id'), nullable=False)
  weekDayId = Column(Integer, ForeignKey('weekDay.id'), nullable=False)
  sessionTimeId = Column(Integer, ForeignKey('sessionSchedule.id'), nullable=False)
  roomId = Column(Integer, ForeignKey('room.id'), nullable=False)
  weekParityId = Column(Integer, ForeignKey('weekParity.id'))

  course = relationship("Course")
  teacher = relationship("Teacher")
  activityType = relationship("ActivityType")
  weekDay = relationship("WeekDay")
  sessionSchedule = relationship("SessionSchedule")
  room = relationship("Room")
  weekParity = relationship("WeekParity")

  def __repr__(self):
    return f"<CourseSession(id={self.id}, course={self.course.name}, teacher={self.teacher.name}, activityType={self.activityType.name})>"