from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

from .group import Group

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  chatId = Column(String)
  groupId = Column(Integer, ForeignKey('StudyGroup.id'))

  group = relationship("Group")

  def __repr__(self):
    return f"User = {self.chatId}"