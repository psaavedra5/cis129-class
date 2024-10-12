## Here is a program for module 5 lab, is related with the documentation
## counting bottles and praticing the loops      by  Juan Pedro Saavedra

totalBottles = 0
todayBottles = 0
totalPayout = 0
payout_perBottle = 0.1
counter = 1
accumulator= 1
keepGoing = 'y'
##Declearing the variables of the program (more info in doc.)

while keepGoing == 'y' :

    totalBottles = 0
    todayBottles = 0
    totalPayout = 0
    counter = 1
    ##Here is declaring the variable inside the loop of re-runs program

    while counter <= 7 :
        
        print("Enter number of bottles returned for day #", counter, ":")
        todayBottles = int(input())
        ## here asking the user for the amount of bottle returned in one day

        totalBottles= totalBottles + todayBottles
        counter = counter + 1
        ## Here ends the loop for the week

    totalPayout= payout_perBottle * totalBottles
    ## here is calculating the total payout of the week 

    print('Here is the total bottles for the week:  ',totalBottles)
    print('Here is the total payout for the week: ', totalPayout)
    ## Here is to display the amount of bottles and the payout

    accumulator= accumulator + 1
    ## this accumulator it looks like is extra but is here (IT Works !!DONT TOUCH!!)

    print("Do you want to enter another week's worth of data? ")
    keepGoing= input('Enter y or n')
    ## Here is asking the user if wants to end the program

print('Thanks for using the program have a great life user ... ')
## AND HERE ENDS THE PROGRAM
    
