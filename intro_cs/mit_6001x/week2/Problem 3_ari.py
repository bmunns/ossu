originalBalance = 4773
balance = originalBalance
annualInterestRate = 0.2

low = 0
high = balance * ((1 + annualInterestRate/12)**12)/12
month = 1
guess = (low + high)/2

while True:
    balance = originalBalance
    guess = (low + high)/2
    month = 1
    while month < 13:
        balance = balance - guess
        balance +=  (balance * (annualInterestRate/12))
        month += 1

    if -0.01 < balance < 0:
        break
    if balance > 0:
        low = guess
    else:
        high = guess


print("Lowest Payment:", f'{guess:2.0f}')
