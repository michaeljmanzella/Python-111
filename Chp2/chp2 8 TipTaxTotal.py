# Michael Manzella
# 08-Sep-20

# 8. Tip, Tax, and Total

# Write a program that calculates the total amount of a meal purchased
# at a restaurant. The program should ask the user to enter the charge
# for the food, then calculate the amounts of a 18 percent tip and 7
# percent sales tax. Display each of these amounts and the total.

SALES_TAX = .07
TIP = .18

purchasePrice = float(input('Enter the charge for food: '))

#calculate sales tax
salesTaxTotal = purchasePrice * SALES_TAX
print('Sales Tax = \t$',
    format(salesTaxTotal, ',.2f'),
    sep='')

#calculate just the tip 
tipTotal = purchasePrice * TIP
print('Tip = \t\t$',
    format(tipTotal, ',.2f'),
    sep='')

#calculate total purchase price
total = purchasePrice + salesTaxTotal + tipTotal
print('Total Sales = \t$',
    format(total, ',.2f'),
    sep='')

# Output
# Enter the charge for food: 1
# Sales Tax = 	$0.07
# Tip = 		$0.18
# Total Sales = 	$1.25