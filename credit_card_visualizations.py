import pandas as pd
import matplotlib.pyplot as plt

# Load Cleaned Datasets
customer = pd.read_csv('customer_clean.csv')
spend = pd.read_csv('spend_clean.csv')

l_spend = pd.merge(customer, spend, on='Customer', how='inner')
l_spend['Month'] = pd.to_datetime(l_spend['Month'])

#Q4(c): Seasonality Spend Line Chart ---
l_spend['Month_Num'] = l_spend['Month'].dt.month
seasonality = l_spend.groupby('Month_Num')['Amount'].sum()

# Map chronological indices to names
month_names = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 
               7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

plt.figure(figsize=(10, 5))
plt.plot([month_names[m] for m in seasonality.index], seasonality.values, marker='o', color='darkorange', linewidth=2)
plt.title('Monthly Spending Seasonality Patterns (Clean Data)')
plt.xlabel('Month')
plt.ylabel('Total Aggregated Spend')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()