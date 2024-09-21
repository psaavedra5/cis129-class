print ('*************************************')

print ('My Coffee and Muffin Shop')
##Here is the presentention to the shop

Muffin = 4.00 
Coffee = 5.00

# Declare()   ##Save for the two new items 
# Declare()
## Here is to declare the variable to use in the program
print ('Number of coffees bought?')
number_coffees = int(input ())
print('Number of muffins bought ?')
number_muffins = int(input())
	# Print('Number of cheesecakes bought ?')
	# input(number_cheesecakes)
	# Print('Number of chocomilks bought ? ')
	# input (number_chocomilks)
## Here is asking the user how many of each item would it like 

print('*************************************')

Totalcoffes= number_coffees * Coffee
Totalmuffins= number_muffins * Muffin
#Totalcheesecakes=
#Totalchocomilks=
##Here is each total individully with out taxes

Subtotal= (number_coffees * Coffee)+(number_muffins*Muffin)
#Subtotal= (number_cheesecakes * Cheesecake) + (number_chocomilks * Chocomilk )
## Here is the subtotal to calculate the tax out of that 

tax=0.06 * Subtotal
Total = tax + Subtotal
#Calculating the taxes of the things bought and the total due
print('*************************************')

print ('My Coffe and Muffin Shop Receipt')
display (number_coffees,'Coffee at $5 each:',Totalcoffes)
display (number_muffins,'Muffins at  $4 each',Totalmuffins)
display('6% tax:',tax)
print('-----------')
display('Total:',Total)

# Here is the e-receipt for what they buy
