# (13)  SHIPPING CHARGES (page 134)
# 
# The Fast Freight Shipping Company charges the following rates:
# 
# Weight of Package                         Rate per Pound
# 2 pounds or less                          $1.50
# Over 2 pounds but not more than 6 pounds   $3.00
# Over 6 pounds but not more than 10 pounds $4.00
# Over 10 pounds                        $4.75
# 
# Write a program that asks the user to enter the weight of a package then displays the shipping charges.

#get weight from user
weight = int(input('Enter weight:'))

#find shipping rates
if weight >= 10:
    rate = 4.75
elif weight >= 6 and weight < 10:
    rate = 4.00
elif weight >= 2 and weight < 6:
    rate = 4.00
else: rate = 1.50

#print charges formatted for money
print('Shipping Charges = $',
    format(rate,',.2f'),
    sep='')

# Enter weight:100
# Shipping Charges = $4.75