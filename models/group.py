from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

from .language import Language
from .speciality import Speciality

class Group(Base):
  __tablename__ = 'StudyGroup'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  languageId = Column(Integer, ForeignKey('language.id'))
  semester = Column(Integer)
  specialityId = Column(Integer, ForeignKey('speciality.id'))

  language = relationship("Language")
  speciality = relationship("Speciality")

  def __repr__(self):
    return f"Group = '{self.name}'"