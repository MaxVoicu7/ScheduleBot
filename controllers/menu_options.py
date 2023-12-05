"""
menu_options.py

This module in the 'controllers' folder provides utility functions for formatting and processing 
schedule-related data for the Telegram bot. These functions are used to generate user-friendly 
messages displaying course schedules, taking into account various factors like date, time, and week parity.

Functions included in this module:

- format_schedule(course_sessions):
  Formats a list of course sessions into a structured string for display. Each session's details, 
  including start and end times, room, activity type, and teacher, are neatly formatted. This function 
  is used for displaying daily schedules or specific schedule queries.

- find_next_day_with_pairs(session, group_id, start_date):
  Determines the next day starting from a given date ('start_date') when the specified group ('group_id') 
  has scheduled classes or sessions. It returns the date, the weekday, and the pairs (classes/sessions) 
  for that day. This function is useful for finding the next day with scheduled activities.

- check_today_schedule(session, group_id):
  Returns a string message with today's schedule for the specified group. It checks the current time 
  and filters out past classes, showing only upcoming or ongoing sessions for the day. This function 
  is essential for providing real-time schedule information to users.

- format_schedule_with_parity(course_sessions):
  Similar to `format_schedule`, but also includes information about the week parity (odd or even) 
  for each session. This is particularly useful for schedules that alternate on a bi-weekly basis.

These utility functions play a crucial role in the bot's ability to provide detailed and accurate 
schedule information, enhancing the overall user experience. They leverage the `date_helpers` module 
from `utils` for date-related calculations and use data fetched from the database via `db.interogations`.
"""


from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from utils.date_helpers import get_weekday, get_week_parity
from db.interogations import get_tomorrows_schedule



def format_schedule(course_sessions):
  """
  Formats a list of course sessions into a structured and readable string.

  This function takes a list of course session objects and formats them into a user-friendly text layout. 
  Each session's details are organized in a clear and concise manner, making it easy for users to 
  understand their schedule.

  Args:
    course_sessions (list): A list of course session objects to be formatted.

  Returns:
    str: A formatted string representing the schedule, where each line contains information about 
    a course session, including its time, location, type, instructor, and course name.

  The course sessions are first sorted by their start times. For each session, the function extracts 
  and formats the start and end times, room name, activity type, teacher's name, and course name. 
  These details are then compiled into individual lines of text, which are combined into a single 
  string with each session's information on a new line. The resulting string is suitable for display 
  in a message or other text-based interface.
  """

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



def find_next_day_with_pairs(session, group_id, start_date):
  """
  Finds the next date, starting from a given start date, when the specified group has scheduled classes or sessions.

  This function scans up to seven days from the 'start_date' to find a day when the specified group ('group_id') 
  has at least one scheduled class or session. It uses the group's schedule to determine this.

  Args:
    session (Session): The database session used to perform queries.
    group_id (int): The ID of the group for which the schedule is being queried.
    start_date (datetime.date): The date from which to start looking for the next day with scheduled pairs.

  Returns:
    tuple: A tuple containing the next date with scheduled pairs, the weekday of that date, 
    and the list of pairs (classes/sessions) scheduled for that day. If no pairs are found within 
    the next seven days, it returns (None, None, None).

  The function iterates through each day, starting from 'start_date', checks the group's schedule for that 
  day (considering the weekday and week parity), and returns the first date where classes or sessions 
  are scheduled. It leverages 'get_weekday' and 'get_week_parity' to determine the correct day and parity, 
  and 'get_tomorrows_schedule' to fetch the schedule for each day.
  """

  for i in range(7):
    current_date = start_date + timedelta(days=i)
    weekday = get_weekday(current_date)
    week_parity = get_week_parity(current_date)
    pairs = get_tomorrows_schedule(session, group_id, weekday, week_parity)
    if pairs:
      return current_date, weekday, pairs
  
  return None, None, None



def check_today_schedule(session: Session, group_id: int) -> str:
  """
  Retrieves and returns a formatted string of the scheduled classes or sessions for the current day.

  This function checks the schedule for the specified group ('group_id') and returns a formatted string 
  of all the classes or sessions that are scheduled for the current day, considering the current time. 
  It filters out any classes or sessions that have already ended.

  Args:
    session (Session): The database session used to perform queries.
    group_id (int): The ID of the group for which the schedule is being queried.

  Returns:
    str: A formatted string listing all the available pairs for the current day. If no pairs are available, 
    it returns a message indicating that there are no classes or sessions scheduled for the day.

  The function first determines the current weekday and week parity. It then fetches the day's schedule 
  using 'get_tomorrows_schedule' and filters the pairs to include only those that are yet to start or 
  currently ongoing. The available pairs are formatted into a readable string using 'format_schedule'. 
  This function is particularly useful for users who want to quickly check their schedule for the day.
  """

  current_time = datetime.now()
  current_weekday = get_weekday(current_time)
  week_parity = get_week_parity(current_time)

  pairs = get_tomorrows_schedule(session, group_id, current_weekday, week_parity)
  available_pairs = [pair for pair in pairs if (pair.sessionSchedule.startTime <= current_time.time() and pair.sessionSchedule.endTime > current_time.time()) or (pair.sessionSchedule.startTime >= current_time.time())]

  if available_pairs:
    schedule_message = format_schedule(available_pairs)
    return f"Perechile de astăzi:\n\n{schedule_message}"
  else:
    return "Nu sunt perechi disponibile pentru astăzi."
  


def format_schedule_with_parity(course_sessions):
  """
  Formats a list of course sessions into a structured and readable string, including week parity information.

  This function takes a list of course session objects, sorts them by their start times, and formats 
  them into a user-friendly text layout. Each session's details are organized in a clear and concise 
  manner, and the function also adds information about the week parity (odd or even) for each session.

  Args:
    course_sessions (list): A list of course session objects to be formatted.

  Returns:
    str: A formatted string representing the schedule, where each line contains detailed information 
    about a course session, including its time, location, type, instructor, course name, and week parity.

  The course sessions are first sorted by their start times. For each session, the function extracts 
  and formats the start and end times, room name, activity type, teacher's name, course name, and week 
  parity. These details are then compiled into individual lines of text, which are combined into a 
  single string with each session's information on a new line. The resulting string is suitable for 
  display in a message or other text-based interface and is particularly useful for schedules that 
  alternate on a bi-weekly basis.
  """

  sorted_sessions = sorted(course_sessions, key=lambda session: session.sessionSchedule.startTime)
  message_lines = []
    
  for index, session in enumerate(sorted_sessions, start=1):
    start_time = session.sessionSchedule.startTime.strftime("%H:%M")
    end_time = session.sessionSchedule.endTime.strftime("%H:%M")

    if session.weekParityId == 1:
      parity_text = " (săpt. pară)"
    elif session.weekParityId == 2:
      parity_text = " (săpt. impară)"
    else:
      parity_text = ""

    line = (f"<b>{index}. {start_time} -> {end_time}</b> în {session.room.name}{parity_text}\n"
            f"    {session.activityType.name} cu <i>{session.teacher.name}</i>\n"
            f"    <b>{session.course.name}</b>\n")
    message_lines.append(line)

  return "\n".join(message_lines)