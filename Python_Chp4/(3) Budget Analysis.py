# (3)  BUDGET  ANALYSIS
# Michael Manzzella
# Oct 11 20:06

# Write a program that asks the user to enter the amount that he or she has budgeted for a month. A loop should then prompt
# the user to enter each of his or her expenses for the month and keep a running total. When the loop finishes, the program
# should display the amount that the user is over or under budget.

keep_going = 'y'
expenses_total = 0

# get budget
budget = float(input('Enter your budget: '))

#tally up expenses
while keep_going == 'y':
    expenses = float(input('Enter your expenses: '))
    expenses_total = expenses_total + expenses
    keep_going = input('Continue y or n : ')

# output over or under budget
# keep over and under positive
if budget - expenses_total > 0:
    print('Underbudget by ' , budget - expenses_total)
else:
    print('Overbudget by ', expenses_total - budget)
