from sqlalchemy import Column, Integer, String
from db.base import Base

# stores all the teacher Titles available for teachers

class TeacherTitle(Base):
  __tablename__ = 'teacherTitle'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)

  def __repr__(self):
    return f"{self.name}"