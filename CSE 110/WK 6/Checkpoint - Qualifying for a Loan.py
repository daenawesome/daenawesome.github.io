def loan_decision(loan_size, credit_history, income, down_payment):
  decision = False
  if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
      decision = True
    elif credit_history >= 7 or income >= 7:
      if down_payment >= 5:
        decision = True
  else:
    if credit_history < 4:
      decision = False
    elif income >= 7 or down_payment >= 7:
      decision = True
    elif income >= 4 and down_payment >= 4:
      decision = True
  return decision

loan_size = int(input("Enter a loan size (1-10): "))
credit_history = int(input("Enter a credit history (1-10): "))
income = int(input("Enter an income (1-10): "))
down_payment = int(input("Enter a down payment (1-10): "))

decision = loan_decision(loan_size, credit_history, income, down_payment)
if decision:
  print("Yes, we will loan you the money.")
else:
  print("No, we will not loan you the money.")
