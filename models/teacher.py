from sqlalchemy import Column, Integer, String
from db.base import Base

# stores all the teachers that activate at FCIM

class Teacher(Base):
  __tablename__ = 'teacher'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"{self.name}"