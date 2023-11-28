from db_connect import engine
from base import Base
from models.speciality import Speciality

Base.metadata.create_all(bind=engine)
