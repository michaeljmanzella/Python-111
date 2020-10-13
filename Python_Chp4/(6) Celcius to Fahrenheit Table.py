# (6)  CELSIUS TO FAHRENHEIT TABLE
# Michael Manzzella
# Oct 11 20:06

# Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents. The
# formula for converting a temperature from Celsius to Fahrenheit is
# 
# F=95C+32
# where F is the Fahrenheit temperature, and C is the Celsius temperature. Your program must use a loop to display the
# table.

print('Celsius\tFahrenheit')
for num in range(21):
    print(num,'\t',(9/5)*num+32)




