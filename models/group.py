"""
group.py

This module defines the Group model, representing student groups in the CIM Faculty. Each group is associated with 
a specific language of instruction and a speciality.

Attributes:
  - id (Integer): Primary key, uniquely identifying each study group.
  - name (String): The name of the study group.
  - languageId (Integer): Foreign key linking to the Language model, indicating the language of instruction.
  - semester (Integer): The current semester of the study group.
  - specialityId (Integer): Foreign key linking to the Speciality model, indicating the group's speciality.

Relationships:
  - language: Relationship to the Language model, providing details about the language of instruction.
  - speciality: Relationship to the Speciality model, providing details about the group's speciality.

This model is essential for organizing students into groups based on their language and speciality, 
facilitating the management of courses and schedules in the faculty.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from .language import Language
from .speciality import Speciality

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
    return f"<Group(name={self.name}, language={self.language.name}, speciality={self.speciality.name}, semester={self.semester})>"