from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base

# stores all days of a week

class WeekDay(Base):
  __tablename__ = 'weekDay'

  id = Column(Integer, primary_key=True, autoincrement=True)
  day = Column(String, nullable=False)

  def __repr__(self):
    return f"{self.day}"