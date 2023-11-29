from sqlalchemy import Column, Integer, String
from db.base import Base

class Language(Base):
  __tablename__ = 'language'

  id = Column(Integer, primary_key=True)
  name = Column(String)

  def __repr__(self):
    return f"{self.name}"
