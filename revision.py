import random
import math

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
    accountingRateOfReturn = round((avgOpProfit/avgInvestment) * 100, 2)

    usersAnswer = float(input("Input Answer -> ")) # Let the user input the answer 

    print(isAnswerCorrect(usersAnswer, accountingRateOfReturn))
    
    #Show answers here
    print ("Avg Operating Profit: £", avgOpProfit)
    print ("Avg Investment: £", avgInvestment)
    print (round(accountingRateOfReturn, 2))

def NetPresentValue():
    cashFlows = []
    discountRate = random.randint(5, 15) / 100
    initInvestment = random.randint(20, 40) * 1000
    amountOfCashFlows = random.randint(3,5)
    print ("Initial Investment: £", initInvestment)
    print (discountRate)
    
    npv = 0 - initInvestment
    print ("NPV after initial investment: £", npv)

    for year in range (amountOfCashFlows): # Loops through the amount of cash flowing years
        cashFlows.append(random.randint(11, 18) * 1000) # Append a random cash flow
        print ("Year ", year+1, ": ", cashFlows[year]) # Print the cash flows
        npv += cashFlows[year] / math.pow(1+discountRate, year+1)

    usersAnswer = float(input("Input Answer -> ")) # Let the user input the answer 
    print(isAnswerCorrect(usersAnswer, npv))

    #Show answer here
    print (round(npv, 2))

def isAnswerCorrect(usersAnswer, answer):
    if usersAnswer == round(answer, 2): # Check if its correct
        return "Correct!"
    else:
        return "Incorrect :("

NetPresentValue()