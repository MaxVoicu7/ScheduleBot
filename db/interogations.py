from models.speciality import Speciality
from models.language import Language
from models.group import Group
from models.user import User

def get_specialities(session):
  return session.query(Speciality).all()


def get_speciality_by_id(session, speciality_id):
  return session.query(Speciality).get(speciality_id)


def get_languages(session):
  return session.query(Language).all()



def get_groups(session, speciality_id, semester, language_id):
  return session.query(Group).filter(
    Group.specialityId == speciality_id,
    Group.semester == semester,
    Group.languageId == language_id
  ).all()



def update_or_create_user(session, chat_id, group_id):
  user = session.query(User).filter(User.chatId == chat_id).first()

  if user:
    user.groupId = group_id
  else: 
    user = User(chatId=chat_id, groupId=group_id)
    session.add(user)

  session.commit()
  return user