# Michael Manzella
# 01-OCT-20
# (14)  BODY MASS INDEX (page 134)
# 
# Write a program that calculates and displays a person’s body mass index (BMI). The BMI is often
# used to determine whether a person is overweight or underweight for his or her height. A person’s
# BMI is calculated with the following formula:
# 
# BMI = weight x 703/height^2
# 
# where weight is measured in pounds and height is measured in inches. The program should ask the
# user to enter his or her weight and height, then display the user’s BMI. The program should also
# display a message indicating whether the person has optimal weight, is underweight, or is
# overweight.
# A person’s weight is considered to be optimal if his or her BMI is between 18.5 and 25.
# If the BMI is less than 18.5, the person is considered to be underweight.
# If the BMI value is greater than 25, the person is considered to be overweight.

#get height and weight from user
weight = int(input('Enter weight: '))
height = int(input('Enter height: '))

#calculate BMI
bmi = weight*703//height**2

#classify BMI
if bmi >= 25:
    person = 'overweight'
elif bmi >=18.5 and bmi < 25:
    person = 'optimal'
else: person = 'underweight'

#print BMI and classification
print('You BMI is',bmi,'and you are',person)

# OUTPUT
# Enter weight: 210
# Enter height: 74
# You BMI is 26 and you are overweight
