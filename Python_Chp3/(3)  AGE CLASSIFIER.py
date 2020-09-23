# Michael Manzella
# 17-Sep-20
#
# (3)  AGE CLASSIFIER (page 132)
# 
# Write a program that asks the user to enter a person’s age. The program should display a message indicating whether
# the person is an infant, a child, a teenager, or an adult. Following are the guidelines:
# 
# If the person is 1 year old or less, he or she is an infant.
# 
# If the person is older than 1 year, but younger than 13 years, he or she is a child.
# 
# If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# 
# If the person is at least 20 years old, he or she is an adult.

adult = False
teenager = False
child = False

#get age from user
age = int(input('Enter your age: '))

#compare
if age >= 20:
    adult = True 
elif age >= 13 and age <= 20:
    teenager = True 
elif age > 1 and age < 13:
    child = True 

#print
if adult:
    print('You are an adult.')
elif teenager:
    print('You are a teenager.')
elif child:
    print('You are a child.')
else:
    print('You are an infant.')

# Output
# Enter your age: 1
# You are an infant

