
balance = 999999
annualInterestRate = 0.18
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12

# Problem 1:

for i in range(1, 13):
    
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate

print("Remaining balance: " + "{0:.2f}".format(balance))

# Problem 2:

minimumFixedMonthlyPayment = 10

while balance > 0:
    testBalance = balance

    for i in range(12):
    
        monthlyUnpaidBalance = testBalance - minimumFixedMonthlyPayment
        testBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
    
    if testBalance > 0:
        # testBalance = balance
        minimumFixedMonthlyPayment = minimumFixedMonthlyPayment + 10
        # print("Payment bumped to " + str(minimumFixedMonthlyPayment))
    else:
        balance = 0
        print("Lowest Payment: " + str(minimumFixedMonthlyPayment))

# Problem 3:

monthlyPaymentLowerBound = balance/12
monthlyPaymentUpperBound = balance * pow((1 + monthlyInterestRate), 12) / 12
testBalance = balance
epsilon = 0.01
testEpsilon = 1

guess = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
    
while abs(testBalance) > epsilon:
    testBalance = balance

    for i in range(12):
        monthlyUnpaidBalance = testBalance - guess
        testBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate

    if testBalance > epsilon:
        monthlyPaymentLowerBound = guess
        
    else:
        monthlyPaymentUpperBound = guess
        
    guess = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2

print("{0:.2f}".format(guess))
