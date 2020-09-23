# Michael Manzella
# 08-Sep-20

#Sales Tax

#Write a program that will ask the user to enter the amount of a purchase.
#The program should then compute the state and county sales tax. Assume the
#state sales tax is 5 percent and the county sales tax is 2.5 percent. The
#program should display the amount of the purchase, the state sales tax,
#the county sales tax, the total sales tax, and the total of the sale
#(which is the sum of the amount of purchase plus the total sales tax).

#Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

STATE_TAX_PERCENT = .05
COUNTY_TAX_PERCENT = .025

purchase = float(input('Enter the purchase price: '))

stateTax = purchase * STATE_TAX_PERCENT
#print with two decimal places and comma seperator 
print('State sales Tax = \t$',
    format(stateTax, ',.2f'),
    sep='')

countyTax = purchase * COUNTY_TAX_PERCENT
print('County sales Tax = \t$',
    format(countyTax, ',.2f'),
    sep='')

totalSalesTax = stateTax + countyTax
print('Total Sales Tax = \t$',
    format(totalSalesTax, ',.2f'),
    sep='')

totalSales = purchase + totalSalesTax
print('Total Sales = \t\t$',
    format(totalSales, ',.2f'),
    sep='')

# Output
# Enter the purchase price: 1
# State sales Tax = 	$0.05
# County sales Tax = 	$0.03
# Total Sales Tax = 	$0.08
# Total Sales = 		$1.07




