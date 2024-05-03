import random

def calculateARR():
    cashFlows = []

    amountOfCashFlows = random.randint(1,4)

    for years in range (amountOfCashFlows): # Loops through the amount of cash flowing years
        cashFlows.append(random.randint(1, 7) * 1000) # Append a random cash flow
    
    print (cashFlows)

calculateARR()
