import locale
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.user import User
from models.courseSession import CourseSession
from models.pair import Pair
from models.weekDay import WeekDay
from models.course import Course
from models.teacher import Teacher
from models.room import Room
from models.sessionSchedule import SessionSchedule

def get_user_group_id(session: Session, chat_id: str) -> int:
  user = session.query(User).filter(User.chatId == chat_id).first()
  return user.groupId if user else None


locale.setlocale(locale.LC_TIME, 'ro_RO')

def get_tomorrows_weekday():
  tomorrow = datetime.now() + timedelta(days=5)
  return tomorrow.strftime("%A")



def get_tomorrows_schedule(session: Session, group_id: int, weekday: str):
    # Interogarea include acum join-uri către toate tabelele relevante
    pairs = (
        session.query(CourseSession)
        .join(Pair, CourseSession.id == Pair.courseSessionId)
        .join(Course, CourseSession.courseId == Course.id)
        .join(Teacher, CourseSession.teacherId == Teacher.id)
        .join(Room, CourseSession.roomId == Room.id)
        .join(SessionSchedule, CourseSession.sessionTimeId == SessionSchedule.id)
        .join(WeekDay, CourseSession.weekDayId == WeekDay.id)
        .filter(Pair.groupId == group_id, WeekDay.day == weekday)
        .all()
    )

    return pairs


def format_schedule(pairs):
  message_lines = []
  
  for pair in pairs:
    line = f"{pair.course.name} cu {pair.teacher.name}, la sala {pair.room.name}, de la {pair.sessionSchedule.startTime} până la {pair.sessionSchedule.endTime}"
    message_lines.append(line)
  
  return "\n".join(message_lines)