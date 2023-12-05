"""
interogations.py

This module, located in the 'db' folder, contains a collection of functions for querying the database. 
These functions are used throughout the application to retrieve information from the database, 
specifically related to the academic scheduling and user data for the Telegram bot.

Functions included in this module:

- get_specialities(session): Fetches all specialities from the database.
- get_speciality_by_id(session, speciality_id): Retrieves a specific speciality by its ID.
- get_languages(session): Fetches all languages available in the academic system.
- get_groups(session, speciality_id, semester, language_id): Retrieves groups based on specified criteria like speciality, semester, and language.
- update_or_create_user(session, chat_id, group_id): Updates an existing user's group ID or creates a new user record in the database.
- get_user_group_id(session, chat_id): Fetches the group ID associated with a specific user, identified by their chat ID.
- get_tomorrows_schedule(session, group_id, weekday, week_parity): Retrieves the schedule for a specific group for the next day, considering the weekday and week parity.
- get_week_schedule(session, group_id): Fetches the entire week's schedule for a specific group.

Each function in this module is designed to interact with the database using SQLAlchemy ORM, abstracting 
the complexities of direct database queries. The functions provide a clear and Pythonic way of accessing 
data, making it easier to manage the information flow in the application, especially for schedule management 
and user-related operations. This module is a critical component of the application's backend infrastructure, 
facilitating seamless data retrieval for the Telegram bot's functionalities.
"""


from sqlalchemy import or_
from models.speciality import Speciality
from models.language import Language
from models.group import Group
from models.user import User
from models.courseSession import CourseSession
from models.course import Course
from models.pair import Pair
from models.room import Room
from models.teacher import Teacher
from models.weekParity import WeekParity
from models.weekDay import WeekDay
from models.sessionSchedule import SessionSchedule



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



def get_user_group_id(session, chat_id: str) -> int:
  user = session.query(User).filter(User.chatId == chat_id).first()
  return user.groupId if user else None



def get_tomorrows_schedule(session, group_id: int, weekday: str, week_parity: str):
  pairs = (
    session.query(CourseSession)
      .join(Pair, CourseSession.id == Pair.courseSessionId)
      .join(Course, CourseSession.courseId == Course.id)
      .join(Teacher, CourseSession.teacherId == Teacher.id)
      .join(Room, CourseSession.roomId == Room.id)
      .join(SessionSchedule, CourseSession.sessionTimeId == SessionSchedule.id)
      .join(WeekDay, CourseSession.weekDayId == WeekDay.id)
      .join(WeekParity, CourseSession.weekParityId == WeekParity.id, isouter=True)
      .filter(
        Pair.groupId == group_id,
        WeekDay.day == weekday,

        or_(
          CourseSession.weekParityId == None,
          WeekParity.name == week_parity
        )
      )
      .all()
    )

  return pairs



def get_week_schedule(session, group_id: int):
  week_schedule = {}

  for weekday in ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]:
    pairs = (
      session.query(CourseSession)
      .join(Pair, CourseSession.id == Pair.courseSessionId)
      .join(Course, CourseSession.courseId == Course.id)
      .join(Teacher, CourseSession.teacherId == Teacher.id)
      .join(Room, CourseSession.roomId == Room.id)
      .join(SessionSchedule, CourseSession.sessionTimeId == SessionSchedule.id)
      .join(WeekDay, CourseSession.weekDayId == WeekDay.id)
      .filter(
        Pair.groupId == group_id,
        WeekDay.day == weekday
      ).all()
    )

    if pairs:
      week_schedule[weekday] = pairs

  return week_schedule