import random
import math
from prettytable import PrettyTable 

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
    if usersAnswer == answer: # Check if its correct
        return "Correct!"
    else:
        return "Incorrect :("

def partnershipAccounting():
    # capA = Capital Account interest rate
    capAInterestRate = round(random.randint(5,10) / 100, 1)
    #Salaries [0] = A, [1] = B, [2] = C
    salaries = [random.randint(10,50) * 1000, random.randint(30,60) * 1000, random.randint(30, 80) * 1000]
    #Profit Share
    profitShare = [random.randint(1,5),random.randint(1,5),random.randint(1,5)]
    #Interest rate on drawings
    drawingInterestRate = round(random.randint(5,15) / 100, 1)

    #Drawing Amount
    drawingAmount = [random.randint(50,80) * 1000, random.randint(40,80) * 1000, random.randint(30,80) * 1000]

    #Current Accounts
    currentAccountBalances = [random.randint(20,50) * 1000, random.randint(10,30) * 1000, random.randint(20,40) * 1000]

    #Capital Account Balances
    capitalAccountBalances = [random.randint(50,100) * 1000, random.randint(60,100) * 1000, random.randint(50,90) * 1000]

    #Net Profit
    netProfit = random.randint(150,250) * 1000

    #Introduce the question
    print ("A, B, C are in partnership and their agreements include:\ni. Interest at ", capAInterestRate * 100, "% charged on capital accounts\nii. No interest on current accounts\niii. A recieves a salary of £",salaries[0], "\niv. B recieves a salary of £", salaries[1], "\nv. C recieves a salary of £", salaries[2], "vi. Profit sharing is ", profitShare[0], ":", profitShare[1], ":", profitShare[2], "\nvii. Interest on drawings was charged at ", drawingInterestRate*100, "% per annum")
    print ("During the year, A made drawings of £", drawingAmount[0], ", B made drawings of £", drawingAmount[1], ", C made drawings of £", drawingAmount[2], ". Assume these are all made on 1/1/2023")
    print ("A, B, and C's current accounts at 31/12/2022 were £", currentAccountBalances[0], ", £", currentAccountBalances[1], ", £", currentAccountBalances[2], " respectively")
    print ("A, B, and C's capital accounts at 31/12/2022 were £", capitalAccountBalances[0], ", £", capitalAccountBalances[1], ", £", capitalAccountBalances[2], " respectively")
    print ("Net Profit before interest and salaries was  £", netProfit)
    print ("\n\nRequired:-\na. Profit and loss appropration account for the year ended 31/12/2023\nb. Partners current accounts as at 31/12/2023\nGive your final answer of the partners current acounts separated by commas. For example -> 10,000, 20,000, 30,000")

    usersAnswer = input("Answer -> ")

    #Step 1, Net Profit Adjustments to find share of profit
    shareOfProfit = [] # Create an array to append the partners share of profits

    netProfitAdj = netProfit + (sum(drawingAmount) * drawingInterestRate) - sum(salaries) - (sum(capitalAccountBalances) * capAInterestRate) # Calculating net profit adjustments by adding the interest on drawings and taking away salaries and interest on capital

    shareOfProfit.append(round(netProfitAdj * (profitShare[0] / sum(profitShare)), 2))
    shareOfProfit.append(round(netProfitAdj * (profitShare[1] / sum(profitShare)), 2))
    shareOfProfit.append(round(netProfitAdj * (profitShare[2] / sum(profitShare)), 2))

    NetProfitTable = PrettyTable(["Net Profit Adjustments", "£"])
    NetProfitTable.add_row(["Net Profit", netProfit])
    NetProfitTable.add_row(["Drawing Interest", ""])  # Add an empty string for the second column
    NetProfitTable.add_row(["A", drawingAmount[0] * drawingInterestRate])
    NetProfitTable.add_row(["B", drawingAmount[1] * drawingInterestRate])
    NetProfitTable.add_row(["C", drawingAmount[2] * drawingInterestRate])
    NetProfitTable.add_row(["", netProfit + (sum(drawingAmount) * drawingInterestRate)])
    NetProfitTable.add_row(["Salary", ""])
    NetProfitTable.add_row(["A", salaries[0]])
    NetProfitTable.add_row(["B", salaries[1]])
    NetProfitTable.add_row(["C", salaries[2]])
    NetProfitTable.add_row(["Interest on Capital", ""])
    NetProfitTable.add_row(["A", capitalAccountBalances[0] * capAInterestRate])
    NetProfitTable.add_row(["B", capitalAccountBalances[1] * capAInterestRate])
    NetProfitTable.add_row(["C", capitalAccountBalances[2] * capAInterestRate])
    NetProfitTable.add_row(["", netProfit + (sum(drawingAmount) * drawingInterestRate) - sum(salaries) - sum(capitalAccountBalances) * capAInterestRate])
    NetProfitTable.add_row(["Share of Capital", ""])
    NetProfitTable.add_row(["A", shareOfProfit[0]])
    NetProfitTable.add_row(["B", shareOfProfit[1]])
    NetProfitTable.add_row(["C", shareOfProfit[2]])

    #Profit and Loss Appropriation Account:
    for index, partner in enumerate(shareOfProfit):
        partner = partner - (drawingAmount[index] * drawingInterestRate) + salaries[index] + (capitalAccountBalances[index] * capAInterestRate)
        shareOfProfit[index] = partner
    print ("Share of Profit:\nA -> £", shareOfProfit[0], "\nB -> £", shareOfProfit[1], "\nC -> £", shareOfProfit[2])

    partnerCurrentAccountTable = PrettyTable(["", "A", "B", "C"])
    partnerCurrentAccountTable.add_row(["Current Account 31/12/22", currentAccountBalances[0], currentAccountBalances[1], currentAccountBalances[2]])
    partnerCurrentAccountTable.add_row(["PnL From Appropriation", shareOfProfit[0], shareOfProfit[1], shareOfProfit[2]])
    partnerCurrentAccountTable.add_row(["Drawings", drawingAmount[0], drawingAmount[1], drawingAmount[2]])

    #Partner Current Account:
    for index, partner in enumerate(currentAccountBalances):
        partner = partner + shareOfProfit[index] - drawingAmount[index]
        currentAccountBalances[index] = partner
    print ("Current Accounts:\nA -> £", currentAccountBalances[0], "\nB -> £", currentAccountBalances[1], "\nC -> £", currentAccountBalances[2])

    answer = "{:,.0f}, {:,.0f}, {:,.0f}".format(currentAccountBalances[0], currentAccountBalances[1], currentAccountBalances[2])

    pNlAppropriationAcc = PrettyTable(["", "A", "B", "C"])
    pNlAppropriationAcc.add_row(["Balance on Profits", shareOfProfit[0], shareOfProfit[1], shareOfProfit[2]])
    pNlAppropriationAcc.add_row(["Interest on Capital", capitalAccountBalances[0] * capAInterestRate, capitalAccountBalances[1] * capAInterestRate, capitalAccountBalances[2] * capAInterestRate])
    pNlAppropriationAcc.add_row(["Salary", salaries[0], salaries[1], salaries[2]])
    pNlAppropriationAcc.add_row(["Drawing Interest", drawingAmount[0] * drawingInterestRate, drawingAmount[1] * drawingInterestRate, drawingAmount[2] * drawingInterestRate])
    pNlAppropriationAcc.add_row(["Total Proft/Loss", shareOfProfit[0], shareOfProfit[1], shareOfProfit[2]])

    #CurrentAccountBalance changes after line 131, so this line is added to reflect the total after taking drawings away
    partnerCurrentAccountTable.add_row(["Current Account at 31/12/23", currentAccountBalances[0], currentAccountBalances[1], currentAccountBalances[2]])

    print ("Answer -> ", answer)

    print(isAnswerCorrect(usersAnswer, str(answer)))

    print (NetProfitTable)
    print (pNlAppropriationAcc)
    print (partnerCurrentAccountTable)

partnershipAccounting()