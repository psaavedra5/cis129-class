print ('*************************************')

print ('My Coffee and Muffin Shop')
##Here is the presentention to the shop

Muffin = 4.00 
Coffee = 5.00
Cheesecake = 12.00
Chocomilk = 2.00
## Here is to declare the prices of the articles

print ('Number of coffees bought?')
number_coffees = int(input ())
print('Number of muffins bought ?')
number_muffins = int(input())
Print('Number of cheesecakes bought ?')
number_cheesecakes = int(input())
Print('Number of chocomilks bought ? ')
number_chocomilks = int(input())
## Here is asking the user how many of each item would it like 

print('*************************************')

Totalcoffes = number_coffees * Coffee
Totalmuffins = number_muffins * Muffin
Totalcheesecakes = number_cheesecakes * Cheesecake
Totalchocomilks = number_chocomilks * Chocomilk
##Here is each total individully with out taxes

Subtotal= (number_coffees * Coffee)+ (number_muffins*Muffin) + (number_cheesecakes * Cheesecake) + (number_chocomilks * Chocomilk )
## Here is the subtotal to calculate the tax out of that 

tax=0.06 * Subtotal
Total = tax + Subtotal
#Calculating the taxes of the things bought and the total due
print('*************************************')

print ('My Coffe and Muffin Shop Receipt')
display (number_coffees,'Coffee at $5 each:',Totalcoffes)
display (number_muffins,'Muffins at  $4 each',Totalmuffins)
display (number_cheesecakes, 'Cheesecake at $12 each:', Totalcheesecakes)
display (number_chocomilks, 'Chocomilk at $2 each:', Totalchocomilks)
display('6% tax:',tax)
print('-----------')
display('Total:',Total)
print('Thank you so much to play my gameee ... sorry mario64 fan, Thanks for your visit  :D ')

# Here is the e-receipt for what they buy
