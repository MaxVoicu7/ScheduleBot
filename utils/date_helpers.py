"""
date_helpers.py

This module in the `utils` folder contains utility functions related to date and time management, 
specifically tailored for the needs of your application. These functions facilitate the handling 
of common date-related tasks, such as determining the day of the week and calculating week parity.

Functions included in this module:

- get_weekday(date): Takes a `datetime.date` object and returns the corresponding weekday in Romanian. 
  This function is useful for applications or interfaces that require display of dates in a user-friendly format.

- get_week_parity(current_date): Determines whether the current week, based on the given date, is odd or even. 
  This function is particularly useful for scheduling tasks or events that depend on the parity of the week. 
  It calculates the number of weeks passed since a predefined start date and returns either "impară" (odd) 
  or "pară" (even) accordingly.

The utility functions in this module are designed to support various features of the application, 
especially those involving scheduling and time management. Their implementation reflects specific 
requirements such as the start date of the academic year and the localization of weekdays into Romanian.
"""

from datetime import date



def get_weekday(date):
  """
  Converts a given date to its corresponding weekday name in Romanian.

  Args:
    date (datetime.date): The date for which the weekday is to be determined.

  Returns:
    str: The name of the weekday in Romanian.

  This function takes a `datetime.date` object and converts it to the name of the weekday. It then 
  translates this name from English to Romanian using a predefined dictionary. This is particularly 
  useful for applications that require the display of dates in a user-friendly and localized format.

  If the weekday name is not found in the dictionary, the original English name is returned.
  """

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



def get_week_parity(current_date):
  """
  Determines the parity (odd or even) of the current week based on a given date.

  Args:
    current_date (datetime.datetime or datetime.date): The date for which the week parity is to be determined.

  Returns:
    str: "impară" if the week is odd, or "pară" if the week is even.

  This function calculates the number of weeks that have passed since a predefined start date (e.g., 
  the start of an academic year or a specific event) and determines if the current week is odd or even. 
  It is particularly useful for scheduling and organizing events that occur on a bi-weekly basis.

  The week parity is determined by calculating the difference in weeks between the current date and 
  the start date (September 4, 2023). The function then checks if this difference is divisible by 2 
  to ascertain whether the week is odd or even.
  """

  start_date = date(2023, 9, 4) 
  current_date = current_date.date()
  delta = current_date - start_date
  weeks_passed = delta.days // 7

  return "impară" if weeks_passed % 2 == 0 else "pară"