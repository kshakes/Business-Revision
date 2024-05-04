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

def partnershipAccounting():
    # capA = Capital Account interest rate
    capAInterestRate = random.randint(5,10) / 100
    #Salaries [0] = A, [1] = B, [2] = C
    salaries = [random.randint(10,50) * 1000, random.randint(30,60) * 1000, random.randint(30, 80) * 1000]
    #Profit Share
    profitShare = [random.randint(1,5),random.randint(1,5),random.randint(1,5)]
    #Interest rate on drawings
    drawingInterestRate = random.randint(5,15) / 100

    #Drawing Amount
    drawingAmount = [random.randint(50,80) * 1000, random.randint(40,80) * 1000, random.randint(30,80) * 1000]

    #Current Accounts
    currentAccountBalances = [random.randint(20,50) * 1000, random.randint(10,30) * 1000, random.randint(20,40) * 1000]

    #Capital Account Balances
    capitalAccountBalances = [random.randint(50,100) * 1000, random.randint(60,100) * 1000, random.randint(50,90) * 1000]

    #Net Profit
    netProfit = random.randint(150,250) * 1000

    #Step 1, Net Profit Adjustments to find share of profit
    print ("Net Profit: £", netProfit)
    print ("Capital Account Interest Rate: ", capAInterestRate, "%")
    print ("Salaries: ", salaries)
    print ("Profit sharing ratio: ", profitShare)
    print ("Drawing interest rate: ", drawingInterestRate, "%")
    print ("Drawing Amount: ", drawingAmount)
    print ("Current Accounts: ", currentAccountBalances)
    print ("Capital Accounts: ", capitalAccountBalances)

    shareOfProfit = []

    netProfitAdj = netProfit + (sum(drawingAmount) * drawingInterestRate) - sum(salaries) - (sum(capitalAccountBalances) * capAInterestRate)

    shareOfProfit.append(netProfitAdj * (profitShare[0] / sum(profitShare)))
    shareOfProfit.append(netProfitAdj * (profitShare[1] / sum(profitShare)))
    shareOfProfit.append(netProfitAdj * (profitShare[2] / sum(profitShare)))

    for i in shareOfProfit:
        print ("£", i)
    
    #Profit and Loss Appropriation Account:
    for index, partner in enumerate(shareOfProfit):
        partner = partner - (drawingAmount[index] * drawingInterestRate) + salaries[index] + (capitalAccountBalances[index] * capAInterestRate)
        shareOfProfit[index] = partner
    print (shareOfProfit)

    #Partner Current Account:
    for index, partner in enumerate(currentAccountBalances):
        partner = partner + shareOfProfit[index] - drawingAmount[index]
        currentAccountBalances[index] = partner
    print (currentAccountBalances)

partnershipAccounting()