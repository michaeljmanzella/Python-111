# (11)  WEIGHT LOSS
# Michael Manzzella
# Oct 11 20:06

# If a moderately active person cuts their calorie intake by 500 calories a day, they can typically lose about 4 pounds a
# month. Write a program that lets the user enter their starting weight, then creates and displays a table showing what their
# expected weight will be at the end of each month for the next 6 months if they stay on this diet.

# get weight
weight = int(input('Enter weight: '))

print('Month\tWeight')
for num in range(6):
    weight = weight - 4
    print(num+1,'\t',weight)
    

