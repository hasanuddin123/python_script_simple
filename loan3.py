
#Declare variables
monthlypayment = 0  
loanamount = 0
interestrate = 0
numberofpayments = 0  
loandurationinyears = 0
#payments
loanamount = raw_input("How much money will you borrow? ")

interestrate = raw_input("What is the interest rate on the loan? ")

loandurationinyears = raw_input("How many years will it take you to pay off the loan? ")

#Convert the strings into floating numbers so we can use them in the  formula
loandurationinyears = float(loandurationinyears)
loanamount = float(loanamount)
interestrate = float(interestrate)

#Since payments are once per month, number of payments is number of years for the loan

numberofpayments = loandurationinyears*12

#calculate the monthly payment based on the formula

monthlypayment = loanamount * interestrate * (1+ interestrate) * numberofpayments / ((1 + interestrate) * numberofpayments -1)

#Result to the program

print("Your monthly payment will be " + str(monthlypayment))
