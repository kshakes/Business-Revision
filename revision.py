import random

def calculateARR():
    cashFlows = []

    initInvestment = random.randint(8, 15) * 1000 # Generate a random initial investment
    amountOfCashFlows = random.randint(3,5) # Generate a random amount of cash flowing years
    print ("Initial Investment: £", initInvestment)

    for year in range (amountOfCashFlows): # Loops through the amount of cash flowing years
        cashFlows.append(random.randint(2, 7) * 1000) # Append a random cash flow
        print ("Year ", year+1, ": ", cashFlows[year]) # Print the cash flows

    profit = (sum(cashFlows) - initInvestment)
    avgOpProfit = profit / len(cashFlows) # Worked out by dividing profit by amount of years

    avgInvestment = initInvestment / 2
    accountingRateOfReturn = (avgOpProfit/avgInvestment) * 100

    usersAnswer = float(input("Input Answer -> ")) # Let the user input the answer 

    if usersAnswer == round(accountingRateOfReturn, 2): # Check if its correct
        print ("Correct!")
    else:
        print ("Incorrect :(")
    
    #Show answers here
    print ("Avg Operating Profit: £", avgOpProfit)
    print ("Avg Investment: £", avgInvestment)
    print (round(accountingRateOfReturn, 2))

calculateARR()