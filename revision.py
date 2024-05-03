import random

def calculateARR():
    cashFlows = []

    initInvestment = random.randint(8, 15) * 1000
    amountOfCashFlows = random.randint(3,5)
    print ("Initial Investment: £", initInvestment)

    for year in range (amountOfCashFlows): # Loops through the amount of cash flowing years
        cashFlows.append(random.randint(2, 7) * 1000) # Append a random cash flow
        print ("Year ", year+1, ": ", cashFlows[year])

    profit = (sum(cashFlows) - initInvestment)
    avgOpProfit = profit / len(cashFlows)

    print ("Avg Operating Profit: £", avgOpProfit)
    avgInvestment = initInvestment / 2
    print ("Avg Investment: £", avgInvestment)

    accountingRateOfReturn = (avgOpProfit/avgInvestment) * 100

    print (round(accountingRateOfReturn,2 ))

calculateARR()
