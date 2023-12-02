from sqlalchemy import Column, Integer, String
from db.base import Base

# stores all the rooms and places where courses are given

class Room(Base):
  __tablename__ = 'room'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"{self.name}"