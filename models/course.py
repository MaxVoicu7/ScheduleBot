from sqlalchemy import Column, Integer, String
from db.base import Base

# used to store all the courses students have, like Baze de Date (Database), Programarea Orientata pe Obiect (OOP)

class Course(Base):
  __tablename__ = 'course'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"{self.name}"