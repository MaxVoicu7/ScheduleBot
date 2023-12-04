"""
user.py

This module defines the User model, which represents users interacting with the Telegram bot. 
Each user is associated with a specific chat ID (unique to each Telegram user) and is linked 
to a group (as defined in the Group model), representing their affiliation or class within FCIM.

Attributes:
  - id (Integer): Primary key, uniquely identifying each user.
  - chatId (String): The Telegram chat ID of the user, used for bot communication.
  - groupId (Integer): Foreign key linking to the Group model, indicating the user's group affiliation.

Relationships:
  - group: Relationship to the Group model, providing details about the user's group.

The User model is crucial for personalizing interactions and responses of the Telegram bot, 
enabling it to provide relevant information and services based on the user's group and academic context.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from .group import Group

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, autoincrement=True)
  chatId = Column(String, nullable=False)
  groupId = Column(Integer, ForeignKey('studyGroup.id'), nullable=False)

  group = relationship("Group")

  def __repr__(self):
    return f"<User(chatId={self.chatId}, groupId={self.groupId})>"