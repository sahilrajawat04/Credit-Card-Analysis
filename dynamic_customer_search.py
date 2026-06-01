import pandas as pd

# Load Cleaned Datasets
customer = pd.read_csv('customer_clean.csv')
repay = pd.read_csv('repay_clean.csv')

l_repay = pd.merge(customer, repay, on='Customer', how='inner')
l_repay['Month'] = pd.to_datetime(l_repay['Month'])

def get_top_10_customers(product_type, time_period):
    """
    Finds the top 10 customers for each city in terms of their repayment amount
    by card product and segment period parameters.
    """
    df = l_repay.copy()
    
    # Filter card segment
    df = df[df['Product'].str.upper() == product_type.upper()]
    
    # Isolate period index flags
    if time_period.lower() == 'yearly':
        df['Period'] = df['Month'].dt.year
    elif time_period.lower() == 'monthly':
        df['Period'] = df['Month'].dt.to_period('M')
    else:
        print("Invalid period format selected. Use 'yearly' or 'monthly'.")
        return None
        
    return df.groupby(['Period', 'City', 'Customer', 'Product'])['Amount'].sum().sort_values(ascending=False).head(10)

# Interactive Client Program Engine
print("\n--- Credit Card Client Search Portal ---")
prod_input = input("Enter product type (Gold/Silver/Platinum): ")
period_input = input("Enter time period (yearly/monthly): ")

print(f"\nTop 10 Customers Summary for {prod_input.upper()} ({period_input.upper()}):")
print(get_top_10_customers(prod_input, period_input))