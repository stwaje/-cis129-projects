# Sano Twaje
# 10/15/2024
"""This code will ask the user for the daily number of bottles collected over \
...: a week and return the total number of bottles collecte and they pay out. \
...: The program will keep going keep going until user says no. """

def main():

    # totalBottles = number of bottles at end of week
    # todayBottles = number of bottles for the day
    # counter = keeps track number of of days
    # totalPayout = amount paid after a week
    
    keepGoing = "y"
    
    # This function starts loop and keep going until user say no
    
    while keepGoing == "y":
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        printTotal(totalBottles, totalPayout)
        print(f"Do you want to enter another week's worth of data?")
        keepGoing = input("Enter y or n ")

# This function calculates number of bottles collected over a week

def getBottles():
    totalBottles = 0
    totalBottles = 0
    counter = 1

    while counter <= 7:
        todayBottles = int(input(f"Enter number of bottles returned for the day #{counter}: "))
        totalBottles = todayBottles + totalBottles
        counter = counter + 1
    return totalBottles

# This function caculate payout of the bottles collected

def calcPayout(totalBottles):
    PAYOUT_PER_BOTTLE = .10
    totalPayout = 0
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE
    return totalPayout

# This function prints total number of bottles collected and payout

def printTotal(totalBottles, totalPayout):
    print(f'\nThe total number of bottles collecteed is {totalBottles}')
    print(f'The total paid out is ${totalPayout:.1f}\n')

main()
    
    
        
    
            
            
            
