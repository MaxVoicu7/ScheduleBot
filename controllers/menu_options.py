from datetime import datetime, timedelta, date
from sqlalchemy import or_
from sqlalchemy.orm import Session
from models.user import User
from models.courseSession import CourseSession
from models.pair import Pair
from models.weekDay import WeekDay
from models.course import Course
from models.teacher import Teacher
from models.room import Room
from models.sessionSchedule import SessionSchedule
from models.weekParity import WeekParity


# based on chat_id parameter we get from the database the groupId
def get_user_group_id(session: Session, chat_id: str) -> int:
  user = session.query(User).filter(User.chatId == chat_id).first()
  return user.groupId if user else None



# returns the weekday based on the date
def get_weekday(date):
  weekday = date.strftime("%A")

  english_to_romanian = {
    "Monday": "Luni",
    "Tuesday": "Marti",
    "Wednesday": "Miercuri",
    "Thursday": "Joi",
    "Friday": "Vineri",
    "Saturday": "Sambata",
    "Sunday": "Duminica"
  }

  return english_to_romanian.get(weekday, weekday)




# check if the current week is even or odd
def get_week_parity(current_date):
  start_date = date(2023, 9, 4) 
  current_date = current_date.date()
  delta = current_date - start_date
  weeks_passed = delta.days // 7

  return "impară" if weeks_passed % 2 == 0 else "pară"



# join the tables neccessary to extract a pair and all info related to it based on a groupId, weekday and weekParity
def get_tomorrows_schedule(session: Session, group_id: int, weekday: str, week_parity: str):
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



# edit the pairs into a string to be displayed
def format_schedule(course_sessions):
  sorted_sessions = sorted(course_sessions, key=lambda session: session.sessionSchedule.startTime)

  message_lines = []
    
  for index, session in enumerate(sorted_sessions, start=1):
    start_time = session.sessionSchedule.startTime.strftime("%H:%M")
    end_time = session.sessionSchedule.endTime.strftime("%H:%M")

    line = (f"<b>{index}. {start_time} -> {end_time}</b> în {session.room.name}\n"
            f"    {session.activityType.name} cu <i>{session.teacher.name}</i>\n"
            f"    <b>{session.course.name}</b>\n")
    message_lines.append(line)

  return "\n".join(message_lines)



# finds the next day in which the groud with the group_id has pairs
def find_next_day_with_pairs(session, group_id, start_date):
  for i in range(7):
    current_date = start_date + timedelta(days=i)
    weekday = get_weekday(current_date)
    week_parity = get_week_parity(current_date)
    pairs = get_tomorrows_schedule(session, group_id, weekday, week_parity)
    if pairs:
      return current_date, weekday, pairs
  
  return None, None, None



