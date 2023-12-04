"""
room.py

This module defines the Room model, used to represent different rooms or locations where courses 
are held within the FCIM campus. It stores essential details about each room, such as its name or identifier.

Attributes:
  - id (Integer): Primary key, uniquely identifying each room in the database.
  - name (String): The name or identifier of the room, which could be a room number, hall name, etc.

The Room model facilitates the management and scheduling of course sessions by providing a clear reference 
to the physical or virtual location where these sessions will take place.
"""

from sqlalchemy import Column, Integer, String
from db.base import Base

class Room(Base):
  __tablename__ = 'room'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"<Room(name={self.name})>"