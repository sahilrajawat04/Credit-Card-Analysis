import pandas as pd

# Load Cleaned Datasets
customer = pd.read_csv('customer_clean.csv')
spend = pd.read_csv('spend_clean.csv')
repay = pd.read_csv('repay_clean.csv')

# Merge clean states for tracking metrics
l_spend = pd.merge(customer, spend, on='Customer', how='inner')
l_repay = pd.merge(customer, repay, on='Customer', how='inner')

l_spend['Month'] = pd.to_datetime(l_spend['Month'])
l_repay['Month'] = pd.to_datetime(l_repay['Month'])

print("--- Q2(a): Distinct Customers ---")
print("Distinct Customers:", customer['Customer'].nunique())

print("\n--- Q2(b): Distinct Categories ---")
print("Distinct Product Categories:", l_spend['Product'].nunique())

print("\n--- Q2(c & d): Average Monthly Spend & Repayments (First 5) ---")
print("Average Monthly Spend:\n", l_spend.groupby(['Customer', l_spend['Month'].dt.to_period('M')])['Amount'].mean().head())
print("\nAverage Monthly Repay:\n", l_repay.groupby(['Customer', l_repay['Month'].dt.to_period('M')])['Amount'].mean().head())

print("\n--- Q2(e): Monthly Bank Profit ---")
total_spend = l_spend.groupby(['Customer', l_spend['Month'].dt.to_period('M')])['Amount'].sum()
total_repay = l_repay.groupby(['Customer', l_repay['Month'].dt.to_period('M')])['Amount'].sum()
monthly_diff = total_repay.sub(total_spend, fill_value=0)
bank_profit = monthly_diff.apply(lambda m: m * 0.029 if m > 0 else 0)
print(bank_profit.groupby('Month').sum().head())

print("\n--- Q2(f): Top 5 Product Types ---")
print(l_spend.groupby('Type')['Amount'].sum().sort_values(ascending=False).head(5))

print("\n--- Q2(g): Highest Spending City ---")
print(l_spend.groupby('City')['Amount'].sum().sort_values(ascending=False).head(1))

print("\n--- Q2(h): Highest Spending Age Group ---")
l_spend['Age_Group'] = pd.cut(l_spend['Age'], bins=[0, 18, 30, 50, 100], labels=['Minors', 'Youth', 'Middle-Aged', 'Seniors'])
print(l_spend.groupby('Age_Group', observed=False)['Amount'].sum().sort_values(ascending=False).head(1))

print("\n--- Q2(i): Top 10 Customers by Repayment ---")
print(l_repay.groupby('Customer')['Amount'].sum().sort_values(ascending=False).head(10))