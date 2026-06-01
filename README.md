# Credit Card Exploratory Data Analysis (EDA)

This repository contains a comprehensive, modular Python data analysis pipeline that explores customer spending behaviors, credit utilization habits, and repayment patterns in the banking industry. 

The project evaluates corporate credit limit policies, handles demographic edge-case filtering, and builds an interactive client search matrix.

## 📁 Repository Structure
* `Customer Acqusition.csv` - Raw customer profile data (Demographics, Income, Card Types, Limits).
* `spend.csv` - Raw historical transactional log data of customer spending.
* `Repayment.csv` - Raw historical repayment records.
* `data_cleaning.py` - Implements initial data handling logic, minor age imputation, and strategic credit limit caps.
* `credit_card_summaries.py` - Aggregates high-level business KPIs and computes monthly banking profit spreads.
* `credit_card_visualizations.py` - Generates chronological monthly spending seasonality graphs using Matplotlib.
* `dynamic_customer_search.py` - A production-ready command-line tool allowing dynamic querying of top clients based on user criteria.
* `requirements.txt` - Lists the external Python dependencies required to run the environment.

## 🛠️ Core Business Logic Implemented
1. **Demographic Filtering:** Auto-imputed invalid accounts for minor cardholders (Age < 18) using valid-adult mean metrics.
2. **Risk Management Constraints:** Enforced transaction caps where spending anomalies exceeding credit limits were dynamically scaled to 50% of the limit.
3. **Repayment Corrections:** Capped overflowing repayments to align precisely with strict account card ceilings.
4. **Profit Distribution Tracking:** Modeled monthly floating interest spreads assessing a 2.9% banking profit margin exclusively on net-positive repayment differentials.

## 🚀 How To Run The Project
1. Clone this repository to your local machine.
2. Install the necessary dependencies using the requirements file:
   ```bash
   pip install -r requirements.txt
