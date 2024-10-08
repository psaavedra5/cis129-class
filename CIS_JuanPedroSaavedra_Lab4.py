## This code is for a class Module 4, and is to calculate the bonus
## that will recive an employee and the store                 by Juan Pedro Saavedra

##########################*************#################

monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount= 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = 'insert the monthly sales' # prompt will be a string literal
##Declearing local variables

monthlySales= float(input(prompt))

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
			
elif monthlySales >= 90000:
    storeAmount = 4000
		
elif monthlySales >= 80000:
    storeAmount = 3000
		
else :
    storeAmount = 0
## Here i am calculatnig the storeAmount bonus that will recive for the sales


salesIncrease = float(input('What is the increasing percentage in sales? ' ))
salesIncrease = salesIncrease / 100

# The previous lines collects the percentage increase and transforms them into decimal

if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0

##Those are the if statemantes to calculate the individual bonus for each employe

# This code prints the bonus information
print('The store bonus amount is $',storeAmount)
print('The employee bonus amount is $',empAmount)

if (storeAmount == 6000 ) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')


##THis is the end of the program  :D
