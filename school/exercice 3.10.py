ANNUAL_RATE = .12
MONTHLY_RATE = ANNUAL_RATE / 12

purchasePrice = float(input("Enter the purchase price: "))

monthlyPayment = .05 * (purchasePrice -(.10 * purchasePrice))
month = 1
balance = purchasePrice
print("Month Starting Balance Internet to pay Principal to Pay Payment ending Balance")
while balance > 0:
  if monthlyPayment > balance:
      monthlyPayment = balance
      interest = 0
  else:
    interest = balance * MONTHLY_RATE
  principal = monthlyPayment _ interest
  remaining = balance _ monthlyPayment
  print("%2d%15.2f%15.2f%17.2f%17.2f" % \ 
        (month, balance, interest, principal, monthlyPayment, remaining))
    balance = remaining
    month += 1
    