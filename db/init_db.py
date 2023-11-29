from db_connect import engine
from base import Base
from models.speciality import Speciality
from models.language import Language
from models.group import Group
from models.user import User

Base.metadata.create_all(bind=engine)