import pandas as pd

#Load Raw Datasets
customer = pd.read_csv('Customer Acqusition.csv')
spend = pd.read_csv('spend.csv')
repay = pd.read_csv('Repayment.csv')

#RULE A: Fix Minors (Ages < 18) ---
mean_age = customer.loc[customer['Age'] >= 18, 'Age'].mean()
customer.loc[customer['Age'] < 18, 'Age'] = mean_age

#Merge to bring customer card limits into transaction datasets
spend_merged = pd.merge(spend, customer[['Customer', 'Limit']], on='Customer', how='inner')
repay_merged = pd.merge(repay, customer[['Customer', 'Limit']], on='Customer', how='inner')

#RULE B: Cap Spend
spend_merged.loc[spend_merged['Amount'] > spend_merged['Limit'], 'Amount'] = spend_merged['Limit'] * 0.5

#RULE C: Cap Repayment 
repay_merged.loc[repay_merged['Amount'] > repay_merged['Limit'], 'Amount'] = repay_merged['Limit']

# Drop the helper 'Limit' column before saving to keep files standard
spend_clean = spend_merged.drop(columns=['Limit'])
repay_clean = repay_merged.drop(columns=['Limit'])

# Save Cleaned DataFrames to new files
customer.to_csv('customer_clean.csv', index=False)
spend_clean.to_csv('spend_clean.csv', index=False)
repay_clean.to_csv('repay_clean.csv', index=False)

print("Step 1 Complete: All datasets cleaned and saved as 'clean' CSV targets successfully!")