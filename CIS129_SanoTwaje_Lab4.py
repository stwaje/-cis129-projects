# Module 4 Lab-4
# Sano Twaje
# 10/10/2024
# This program calculates the store bonus and employee bonus of a retail company

# The main function
def main():
    # declare local variables
    # monthlySales = monthly sales amount
    # storeAmount = store bonus amount
    # empAmount = employee bonus amount
    # salesIncrease = percent of sales increase
    # call to getsSales(monthlySales)
    # call to getIncrease(salesIncrease)
    # call to calcStoreBonus(storeAmount)
    # call to calcEmpBonus(empAmount)
    # call to printBonus(storeAmount, empAmount)

# This function get the monthly sales
    def getSales(prompt):
        monthlySales = float(input('Enter montly sales: '))
        return monthlySales()
                 
# This function gets the percent in sales
    def getIncrease(prompt):
        salesIncrease = float(input('Enter sales increase: '))
        salesIncrease = salesIncrease / 100
        return salesIncrease()

# This function determines the storeAmount bonus
    def calcStoreBonus(monthlySales):
        if monthlySales >= 111000:
            storeAmount = 6000
        elif monthlySales >= 100000:
            storeAmount = 5000
        elif monthlySales >= 90000:
            storeAmount = 4000
        elif monthlySales >= 80000:
            storeAmount =3000
        else:
            storeAmount = 0
        return monthlySales()

# This function deteremins the empAmount bonus
    def calcEmpBonus(empAmount):
        if salesIncrease >= .05:
            empAmount = 75
        elif salesIncrease >= .04:
            empAmount = 50
        elif salesIncrease >= .03:
            empAmount = 40
        else:
            empAmount = 0
        return empAmount() 

# This function prints the bonus information
    def printBonus(storeAmount, empAmount):
        print("The store bonus amount is $", storeAmount)
        print("The employee bonus amount is $", empAmount)
        if (storeAmount == 6000) and (empAmount == 75):
            print('Congrats! You have reached the highest bonus amounts possible! ')

# calls main
main()


