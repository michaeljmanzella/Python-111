# (12)  SOFTWARE SALES (page 134)
# 
# A software company sells a package that retails for $99. Quantity discounts are given according to the following table:
# 
# Quantity  Discount
# 10–19     10%
# 20–49     20%
# 50–99     30%
# 100 or more     40%
# 
# Write a program that asks the user to enter the number of packages purchased. The program should then display the
# amount of the discount (if any) and the total amount of the purchase after the discount.

PACKAGE_RETAIL = 99

#get amount of packages
packages = int(input('Enter the number of packages purchased: '))

#find discount
if packages >=10 and packages <= 19:
    discount = .10
elif packages >=20 and packages <=49:
    discount = .20
elif packages >=50 and packages <=99:
    discount = .30
elif packages >=100: 
    discount = .40
else: discount = 0

#calculate discount
discount = PACKAGE_RETAIL * packages * discount
total = (PACKAGE_RETAIL * packages) - (discount)

#print with two decimal points, comma, and no spaces
print('Discount = $',
      format(discount,',.2f'),
      sep='')
print('Total price = $',
      format(total,',.2f'),
      sep='')

# OUTPUT
# Enter the number of packages purchased: 100
# Discount = $3,960.00
# Total price = $5,940.00

