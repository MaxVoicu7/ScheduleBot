from sqlalchemy import Column, Integer, String
from db.base import Base

class Speciality(Base):
  __tablename__ = 'speciality'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  semesters = Column(Integer)
  abbreviation = Column(String)

  def __repr__(self):
    return f"<Speciality(name='{self.name}', abbreviation='{self.abbreviation}')>"
