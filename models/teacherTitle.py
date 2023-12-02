from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class TeacherTitle(Base):
  __tablename__ = 'teacherTitle'

  id = Column(Integer, primary_key=True)
  name = Column(String)

  def __repr__(self):
    return f"{self.name}"