from sqlalchemy import Column, Integer, String
from db.base import Base

# stores if a week is even or not for courses that are given only on even weeks

class WeekParity(Base):
  __tablename__ = 'weekParity'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"{self.name}"