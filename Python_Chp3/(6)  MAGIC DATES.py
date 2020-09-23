# (6)  MAGIC DATES (page 132)
# 
# The date June 10, 1960, is special because when it is written in the following format,
# the month times the day equals the year:
# 
# 6/10/60
# 
# Design a program that asks the user to enter a month (in numeric form), a day, and a
# two-digit year. The program should then determine whether the month times the day equals
# the year. If so, it should display a message saying the date is magic. Otherwise, it
# should display a message saying the date is not magic.

month = int(input('Enter the month: '))
day = int(input('Enter the day: '))
year = int(input('Enter the year: '))

if year == month*day:
    print('The date is magic')
else:
    print('The date is not magic')

# output
# Enter the month: 6
# Enter the day: 10
# Enter the year: 60
# The date is magic