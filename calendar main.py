import calendar

# GETTING THE LIST OF NAMES OF DAYS IN A WEEK
week_header = calendar.weekheader(3)
print(week_header)
print(" ")

# GETTING THE FIRST WEEK DAY IN INDEX FORM (according to      calendar module,the first weekday is monday)
week_day = calendar.firstweekday()
print(week_day)
print(" ")

# GETTING THE FULL CALENDAR OF THAT MONTH 
calendar_month = calendar.month(1947, 8, 3)
print(calendar_month)
print(" ")

# GETTING THE FULL CALENDAR OF MONTH in MATRIX FORM
month_calendar = calendar.monthcalendar(2006,10)
print(month_calendar)
print(" ")

# GETTING THE WHOLE CALENDAR OF A YEAR
year = calendar.calendar(2020,2)
print(year)
print(" ")

# CHECK WHETHER A YEAR IS LEAP OR NOT
leap_check = calendar.isleap(2020)
print(leap_check)
print(" ")

# Calculating number of leapdays in between years
# remenber the first number which here is 2020 is inclusive
# whereas the second number is exclusive
no_of_leapdays = calendar.leapdays(2020,2022)
print(no_of_leapdays)
print(" ")