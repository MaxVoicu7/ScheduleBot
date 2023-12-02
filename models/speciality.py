from sqlalchemy import Column, Integer, String
from db.base import Base

# stores all the specialities available in FCIM

class Speciality(Base):
  __tablename__ = 'speciality'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  semesters = Column(Integer, nullable=False)
  abbreviation = Column(String, nullable=False)

  def __repr__(self):
    return f"Speciality = '{self.name}'"
