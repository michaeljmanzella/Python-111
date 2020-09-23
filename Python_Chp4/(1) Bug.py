# (1) Bug Collector
# A bug collector collects bugs every day for five days. Write a program that keeps a running total of the number of bugs
# collected during the five days. The loop should ask for the number of bugs collected for each day, and when the loop is
# finished, the program should display the total number of bugs collected.

# loop five times
# display day and ask how many bugs collected
# add to bug total
# 
# display total bugs  collected

total = 0

for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
 print('Enter bugs for',day,':', end=' ')
 bugs = int(input(''))
 total = total + bugs
 
print(total,'Bugs collected this week')

# Enter bugs for Monday : 1
# Enter bugs for Tuesday : 1
# Enter bugs for Wednesday : 1
# Enter bugs for Thursday : 1
# Enter bugs for Friday : 1
# 5 Bugs collected this week