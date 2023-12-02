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

# used to store a course Session, indicating the course itself, day and time, place, teacher,
# if it goes every week or only in even weeks

class CourseSession(Base):
  __tablename__ = 'courseSession'

  id = Column(Integer, primary_key=True, autoincrement=True)
  courseId = Column(Integer, ForeignKey('course.id'), nullable=False)
  teacherId = Column(Integer, ForeignKey('teacher.id'), nullable=False)
  activityTypeId = Column(Integer, ForeignKey('activityType.id'), nullable=False)
  weekDayId = Column(Integer, ForeignKey('weekDay.id'), nullable=False)
  sessionTimeId = Column(Integer, ForeignKey('sessionSchedule.id'), nullable=False)
  roomId = Column(Integer, ForeignKey('room.id'), nullable=False)
  # if weekParity is null, then course goes every week
  weekParityId = Column(Integer, ForeignKey('weekParity.id'))

  course = relationship("Course")
  teacher = relationship("Teacher")
  activityType = relationship("ActivityType")
  weekDay = relationship("WeekDay")
  sessionSchedule = relationship("SessionSchedule")
  room = relationship("Room")
  weekParity = relationship("WeekParity")

  def __repr__(self):
    return f"User = {self.id}"