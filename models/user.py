from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

from .group import Group

# stores all the users that interact with the bot and select their data

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, autoincrement=True)
  chatId = Column(String, nullable=False)
  groupId = Column(Integer, ForeignKey('studyGroup.id'), nullable=False)

  group = relationship("Group")

  def __repr__(self):
    return f"User = {self.chatId}"