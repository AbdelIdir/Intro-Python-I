"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:


 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.



 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# userType = input("Please type something: ")
# userType = ""  for when user inputs nothing

# GeneralUserInput = userType.split(" ")

# print(int(GeneralUserInput[2]), int(GeneralUserInput[3]))
# print(GeneralUserInput)

# themonth = GeneralUserInput[2]
# themonth = sys.argv[1]

now = datetime.now()
# print(now.strftime("%m"))

currentMonth = now.strftime("%m")
currentYear = now.strftime("%Y")

# - If the user specifies two arguments, assume they passed in
# both the month and the year. Render the calendar for that   <<<< DONE
# month and year.

c = calendar.TextCalendar(calendar.MONDAY)
# stuff = c.formatmonth(int(themonth), int(theyear))

stuff2 = c.formatmonth(int(currentYear), int(currentMonth))

# - If the user specifies one argument, assume they passed in a
#   month and render the calendar for that month of the current year.   <<<<<


def calendarPro(year= sys.argv[1:2][0] , month=sys.argv[2:3][0]):

    stuff3 = c.formatmonth(int(month), int(year))
    print(stuff3)

# print(sys.argv[1:2])
# ['12']


calendarPro(currentYear, currentMonth if len(sys.argv) < 2 else False)


# print(sys.argv[1:2][0], sys.argv[2:3])
