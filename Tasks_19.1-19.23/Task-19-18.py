# Create a dictionary with functions for various financial calculations (e.g., compound interest, loan payment, investment return). Write a function financial_calculator(operation, **kwargs) that uses this dictionary to perform the requested calculation.

import math

def compound_interest(principal, rate, times_compounded, years):
  return principal * (1 + rate / times_compounded) ** (times_compounded * years)

def loan_payment(principal, rate, months):
  if rate == 0:
    return principal / months
  return principal * (rate * (1 + rate) ** months) / ((1 + rate) ** months - 1)

def investment_return(principal, rate, years):
  return principal * (1 + rate * years)


financial_operations = {
  "compound_interest": compound_interest,
  "loan_payment": loan_payment,
  "investment_return": investment_return
}

def financial_calculator(operation, **kwargs):
  if operation in financial_operations:
    return financial_operations[operation](**kwargs)
  else:
    raise ValueError("Unknown financial operation")

result1 = financial_calculator("compound_interest", principal=1000, rate=0.05, times_compounded=4, years=5)
print(f"Compound Interest: {result1}")

result2 = financial_calculator("loan_payment", principal=10000, rate=0.005, months=24)
print(f"Loan Payment: {result2}")

result3 = financial_calculator("investment_return", principal=1000, rate=0.07, years=10)
print(f"Investment Return: {result3}")
