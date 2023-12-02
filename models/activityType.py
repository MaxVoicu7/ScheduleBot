from sqlalchemy import Column, Integer, String
from db.base import Base

# used to store different types of course activities like curs, seminar, laboratory

class ActivityType(Base):
  __tablename__ = 'activityType'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"{self.name}"