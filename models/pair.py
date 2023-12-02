from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

from .group import Group
from .courseSession import CourseSession

# stores all the pairs available, that connect groups and courseSessions

class Pair(Base):
  __tablename__ = 'pair'

  id = Column(Integer, primary_key=True, autoincrement=True)
  groupId = Column(Integer, ForeignKey('studyGroup.id'), nullable=False)
  courseSessionId = Column(Integer, ForeignKey('courseSession.id'), nullable=False)

  group = relationship("Group")
  courseSession = relationship("CourseSession")

  def __repr__(self):
    return f"{self.groupId}"