# (8)  SUM OF NUMBERS
# Michael Manzzella
# Oct 11 20:06

# Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative
# number to signal the end of the series. After all the positive numbers have been entered, the program should display their
# sum.

total = 0
num = 0

print('Enter a negative number to escape')

while num >= 0:
    if num >= 0:
        total = total + num
        num = int(input('Enter a positve number: '))
    
print('Sum = ',total)