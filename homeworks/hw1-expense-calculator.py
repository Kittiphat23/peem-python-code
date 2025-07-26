# Personal Finance Calculator
# Student : Kittiphat Thongphum 6730202041 Sec.831
# Date : 26/7/2568
# Purpose : Calculate monthly budget and savings

# Input
monthly_income = float(input("What is your monthly income (THB)?: "))
rent_cost = float(input("What is your monthly rent/housing cost?: "))
food_budget = int(input("What is your food budget monthly (THB)?: "))
transportation_cost = float(input("What is your monthly transportation expenses?: "))
entertainment_budget = int(input("Monthly entertainment budget?: "))
emergency_fund_percent = float(input("Percentage to save for emergency (e.g., 10.5)?: "))
investment_percent = float(input("Percentage to invest (e.g., 15.0)?: "))

# Calculate
Total_Fixed_Expenses = rent_cost + transportation_cost
Total_Variable_Expenses = food_budget + entertainment_budget
Total_Expenses = Total_Fixed_Expenses + Total_Variable_Expenses
Remaining_Income = monthly_income - Total_Expenses

Emergency_Fund_Amount = monthly_income * (emergency_fund_percent / 100)
Investment_Amount = monthly_income * (investment_percent / 100)
Available_for_Saving = Remaining_Income - Emergency_Fund_Amount - Investment_Amount
Expense_Ratio = (Total_Expenses / monthly_income) * 100

# Output
print("\n=== MONTHLY BUDGET REPORT ===")
print("Income:", f"{monthly_income:.2f}", "THB")
print("Fixed Expenses:", f"{Total_Fixed_Expenses:.2f}", "THB")
print("Variable Expenses:", f"{Total_Variable_Expenses:.2f}", "THB")
print("Total Expenses:", f"{Total_Expenses:.2f}", "THB")
print("Remaining:", f"{Remaining_Income:.2f}", "THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {Emergency_Fund_Amount:.2f} THB")
print(f"Investment ({investment_percent}%): {Investment_Amount:.2f} THB")
print("Available for Savings:", f"{Available_for_Saving:.2f}", "THB")

print("\n=== ANALYSIS ===")
print("Expense Ratio:", f"{Expense_Ratio:.2f}%",)