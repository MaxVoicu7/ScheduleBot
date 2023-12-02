from sqlalchemy import Column, Integer, Time
from db.base import Base

# stores all the time intervals for a pair, like 8:00 -> 9:30

class SessionSchedule(Base):
  __tablename__ = 'sessionSchedule'

  id = Column(Integer, primary_key=True, autoincrement=True)
  startTime = Column(Time, nullable=False)
  endTime = Column(Time, nullable=False)

  def __repr__(self):
    return f"{self.start_time} -> {self.end_time}"