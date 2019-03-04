balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


month = 1
for month in range(12):
    balance = balance - balance*monthlyPaymentRate
    balance +=  (balance * (annualInterestRate/12))
    print("Month", month + 1, "Remaining Balance:", f'{balance:.2f}')
    month += 1

print("Remaining balance:", f'{balance:.2f}')
