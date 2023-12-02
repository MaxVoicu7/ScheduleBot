from sqlalchemy import Column, Integer, String
from db.base import Base

# stores the languages in which courses are given inside FCIM 
class Language(Base):
  __tablename__ = 'language'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"{self.name}"
