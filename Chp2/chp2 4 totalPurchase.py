# Michael Manzella
# 08-Sep-20

# 4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

itemPrice = float(input('Enter price item: '))  # get item price
subtotal = itemPrice                            # add price to subtotal

itemPrice = float(input('Enter price item: '))
subtotal = subtotal + itemPrice

itemPrice = float(input('Enter price item: '))
subtotal = subtotal + itemPrice

itemPrice = float(input('Enter price item: '))
subtotal = subtotal + itemPrice

itemPrice = float(input('Enter price item: '))
subtotal = subtotal + itemPrice

tax = subtotal * .07
total = subtotal + (subtotal * .07)         # calculate the subtotal with tax

#print with two decimal places and comma seperator 
print('\tSubtotal = $',
    format(subtotal, ',.2f'),
    sep='')

print('\tTax = $',
    format(tax, ',.2f'),
    sep='')

print('\tTotal = $',
    format(total, ',.2f'),
    sep='')

# Output
# Enter price item: 500
# Enter price item: 500
# Enter price item: 500
# Enter price item: 500
# Enter price item: 500
# 	Subtotal = $2,500.00
# 	Tax = $175.00
# 	Total = $2,675.00

