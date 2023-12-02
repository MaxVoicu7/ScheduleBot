from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

from .language import Language
from .speciality import Speciality

# stores all the active groups of CIM Faculty

class Group(Base):
  __tablename__ = 'studyGroup'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  languageId = Column(Integer, ForeignKey('language.id'), nullable=False)
  semester = Column(Integer, nullable=False)
  specialityId = Column(Integer, ForeignKey('speciality.id'), nullable=False)

  language = relationship("Language")
  speciality = relationship("Speciality")

  def __repr__(self):
    return f"{self.name}"