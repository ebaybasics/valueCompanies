import pandas as pd
from io import StringIO

# ----------------- Data to be ranked ------------------ #
def per_share(dataframe_goes_here):
    # Normalize each useful column
    useful_columns = ['EPS', 'EPS Diluted', 'Cash Flow Per Share', 'Free Cash Flow Per Share', 'Dividend Per Share', 'Cash Per Share', 'Debt Per Share', 'Net Cash Per Share', 'Sales Per Share', 'Operating Income Per Share', 'Equity Per Share', 'Tangible Equity Per Share']
    for col in useful_columns:
        dataframe_goes_here[col] = pd.to_numeric(dataframe_goes_here[col], errors='coerce')
    # Assuming `data` is your DataFrame and `useful_columns` is the list of column names
    numeric_columns = [col for col in useful_columns if pd.api.types.is_numeric_dtype(dataframe_goes_here[col])]

    # Perform the normalization only on numeric columns
    normalized_data = dataframe_goes_here[numeric_columns].div(dataframe_goes_here[numeric_columns].max())
    # Replace spaces in the column names with underscores
    normalized_data.columns = normalized_data.columns.str.replace(' ', '_')

    # Assign weights to each column
    weights = {
            'EPS': 9,
            'EPS Diluted': 8,
            'Cash Flow Per Share': 7,
            'Free Cash Flow Per Share': 9,
            'Dividend Per Share': 6,
            'Cash Per Share': 0,
            'Debt Per Share': 0,
            'Net Cash Per Share': 5,
            'Sales Per Share': 7,
            'Operating Income Per Share': 8,
            'Equity Per Share': 6,
            'Tangible Equity Per Share': 5,

    }

    weights = normalize_weights(weights)

    # Convert the weights dictionary to a pandas Series
    weights_series = pd.Series(weights)

    # Calculate the score for each company
    scores = normalized_data.mul(weights_series).sum(axis=1)

    # Add the scores to the data and sort by score
    dataframe_goes_here['Score'] = scores
    sorted_data = dataframe_goes_here.sort_values('Score', ascending=False)

    # Print the sorted data
    return sorted_data[['Ticker', 'Company', 'Score']]


def growth(dataframe):
    useful_columns = ['Sustainable Growth Rate', 'Sales QoQ Chg.', 'Eps QoQ Chg.', 'Sales Growth Next Year',
                      'EPS Next Year Chg (Est.%)', '5-Year EPS Growth Estimate', 'Sales 1-Year Chg (%)',
                      'Sales 3-Year Avg (%)', 'Sales 5-Year Avg (%)', 'Sales 10-Year Avg (%)', 'EPS 1-Year Chg (%)',
                      'EPS 3-Year Avg (%)', 'EPS 5-Year Avg (%)', 'EPS 10-Year Avg (%)']

    for col in useful_columns:
        dataframe[col] = pd.to_numeric(dataframe[col].astype(str).str.strip('%'), errors='coerce')

    numeric_columns = [col for col in useful_columns if pd.api.types.is_numeric_dtype(dataframe[col])]

    normalized_data = dataframe[numeric_columns].div(dataframe[numeric_columns].max())
    normalized_data.columns = normalized_data.columns.str.replace(' ', '_').str.replace('%', 'pct')

    weights = {
        'Sustainable_Growth_Rate': 9,
        'Sales_QoQ_Chg.': 7,
        'Eps_QoQ_Chg.': 6,
        'Sales_Growth_Next_Year': 8,
        'EPS_Next_Year_Chg_(Est.)': 8,
        '5‑Year_EPS_Growth_Estimate': 8,
        'Sales_1‑Year_Chg_(pct)': 7,
        'Sales_3‑Year_Avg_(pct)': 7,
        'Sales_5‑Year_Avg_(pct)': 8,
        'Sales_10‑Year_Avg_(pct)': 8,
        'EPS_1‑Year_Chg_(pct)': 6,
        'EPS_3‑Year_Avg_(pct)': 6,
        'EPS_5‑Year_Avg_(pct)': 7,
        'EPS_10‑Year_Avg_(pct)': 7
        }
    weights = normalize_weights(weights)

    weights_series = pd.Series(weights)
    scores = normalized_data.mul(weights_series).sum(axis=1)

    dataframe['Score'] = scores
    sorted_data = dataframe.sort_values('Score', ascending=False)

    return sorted_data[['Ticker', 'Company', 'Score']]

def financial_health(dataframe):
    useful_columns = [
        'Morningstar Financial Health Grade',
        'Solvency Ratio',
        'Financial Safety Industry Decile',
        'Piotroski F Score',
        'Beneish M-Score',
        'Altman Z-Score',
        'Sloan Ratio',
        'Cash Per Share',
        'Debt Per Share',
        'Net Cash Per Share',
        'Net Cash as a % of Market Cap',
        'Debt / Equity',
        'Long Term Debt / Total Capital',
        'Current Ratio',
        'Quick Ratio',
        'Interest Coverage'
    ]

    for col in useful_columns:
        dataframe[col] = pd.to_numeric(dataframe[col].astype(str).str.strip('%'), errors='coerce')

    # Invert columns that are better when smaller
    dataframe['Financial Safety Industry Decile'] = 1 / dataframe['Financial Safety Industry Decile']
    dataframe['Debt / Equity'] = 1 / dataframe['Debt / Equity']
    dataframe['Long Term Debt / Total Capital'] = 1 / dataframe['Long Term Debt / Total Capital']
    dataframe['Beneish M-Score'] = 1 / dataframe['Beneish M-Score']
    dataframe['Debt Per Share'] = 1 / dataframe['Debt Per Share']

    numeric_columns = [col for col in useful_columns if pd.api.types.is_numeric_dtype(dataframe[col])]

    normalized_data = dataframe[numeric_columns].div(dataframe[numeric_columns].max())
    normalized_data.columns = normalized_data.columns.str.replace(' ', '_').str.replace('%', 'pct')

    weights = {
        'Morningstar_Financial_Health_Grade': 6,
        'Solvency_Ratio': 7,
        'Financial_Safety_Industry_Decile': 9,
        'Piotroski_F_Score': 6,
        'Beneish_M‑Score': 4,
        'Altman_Z‑Score': 7,
        'Sloan_Ratio': 5,
        'Cash_Per_Share': 5,
        'Debt_Per_Share': 4,
        'Net_Cash_Per_Share': 5,
        'Net_Cash_as_a_%of_Market_Cap': 5,
        'Debt/Equity': 6,
        'Long_Term_Debt/_Total_Capital': 6,
        'Current_Ratio': 7,
        'Quick_Ratio': 7,
        'Interest_Coverage': 5
        }

    weights = normalize_weights(weights)

    weights_series = pd.Series(weights)
    scores = normalized_data.mul(weights_series).sum(axis=1)

    dataframe['Score'] = scores
    sorted_data = dataframe.sort_values('Score', ascending=False)

    return sorted_data[['Ticker', 'Company', 'Score']]

def valuation_quick(dataframe):
    useful_columns = ['Price / Earnings', 'P/E Adjusted', 'EV / EBITDA', 'EV / FCF', 'Earnings Yield', 'Greenblatt Earnings Yield', 'Price to Graham Number', 'Price to Lynch Fair Value', 'Cash Return', 'Yacktman Forward RoR', 'Margin of Safety (EPV)', 'EPS', 'EPS Diluted', 'EPS Next Year (Est.)', 'EPS Next Year Chg (Est.%)', 'Forward P/E', 'PEG Forward', 'Shiller PE', 'Price / Sales', 'Price / Sales Industry Decile', 'Price / Book', 'Price / Book Industry Decile', 'Shareholder Yield']

    for col in useful_columns:
        dataframe[col] = pd.to_numeric(dataframe[col].astype(str).str.strip('%'), errors='coerce')

    # Invert columns that are better when smaller
    dataframe['Price / Earnings'] = 1 / dataframe['Price / Earnings']
    dataframe['P/E Adjusted'] = 1 / dataframe['P/E Adjusted']
    dataframe['EV / EBITDA'] = 1 / dataframe['EV / EBITDA']
    dataframe['EV / FCF'] = 1 / dataframe['EV / FCF']
    dataframe['Price to Graham Number'] = 1 / dataframe['Price to Graham Number']
    dataframe['Price to Lynch Fair Value'] = 1 / dataframe['Price to Lynch Fair Value']
    dataframe['Forward P/E'] = 1 / dataframe['Forward P/E']
    dataframe['PEG Forward'] = 1 / dataframe['PEG Forward']
    dataframe['Shiller PE'] = 1 / dataframe['Shiller PE']
    dataframe['Price / Sales'] = 1 / dataframe['Price / Sales']
    dataframe['Price / Sales Industry Decile'] = 1 / dataframe['Price / Sales Industry Decile']
    dataframe['Price / Book Industry Decile'] = 1 / dataframe['Price / Book Industry Decile']

    numeric_columns = [col for col in useful_columns if pd.api.types.is_numeric_dtype(dataframe[col])]

    normalized_data = dataframe[numeric_columns].div(dataframe[numeric_columns].max())
    normalized_data.columns = normalized_data.columns.str.replace(' ', '_').str.replace('%', 'pct')

    weights = {
        'Price_/Earnings': 7,
        'P/E_Adjusted': 8,
        'EV/EBITDA': 8,
        'EV/FCF': 9,
        'Earnings_Yield': 7,
        'Greenblatt_Earnings_Yield': 8,
        'Price_to_Graham_Number': 8,
        'Price_to_Lynch_Fair_Value': 9,
        'Cash_Return': 6,
        'Yacktman_Forward_RoR': 8,
        'Margin_of_Safety(EPV)': 7,
        'EPS': 6,
        'EPS_Diluted': 6,
        'EPS_Next_Year_(Est.)': 7,
        'EPS_Next_Year_Chg_(Est.%': 7,
        'Forward_P/E': 8,
        'PEG_Forward': 9,
        'Shiller_PE': 7,
        'Price_/Sales': 6,
        'Price/Sales_Industry_Decile': 7,
        'Price/Book': 6,
        'Price/_Book_Industry_Decile': 7,
        'Shareholder_Yield': 6
        }

    weights = normalize_weights(weights)

    weights_series = pd.Series(weights)
    scores = normalized_data.mul(weights_series).sum(axis=1)

    dataframe['Score'] = scores
    sorted_data = dataframe.sort_values('Score', ascending=False)

    return sorted_data[['Ticker', 'Company', 'Score']]


# Using the income data, calculate market share and rank by companies with the most market share
def rank_by_market_share(df, sales_column='Sales', ticker_column='Ticker'):
    # Remove any non-numeric characters (e.g., commas) from the sales_column
    df[sales_column] = df[sales_column].astype(str).str.replace(',', '')

    # Convert the sales_column to a numeric data type (float)
    df[sales_column] = pd.to_numeric(df[sales_column], errors='coerce')

    # Calculate the total sales of all companies in the sector
    total_sales = df[sales_column].sum()

    # Calculate the market share for each company
    df['Market Share'] = df[sales_column] / total_sales

    # Convert market share to percentage
    df['Market Share (%)'] = df['Market Share'] * 100

    # Sort the DataFrame by Market Share (%) in descending order
    sorted_data = df.sort_values('Market Share (%)', ascending=False)

    # Assign scores in ascending order based on the sorted market share
    sorted_data['Score'] = sorted_data['Market Share (%)'].rank(ascending=True)

    # Return the sorted DataFrame with Ticker and Market Share columns
    return sorted_data[[ticker_column, 'Market Share (%)', 'Score']]


def rank_by_profitability(dataframe):
    # List of columns representing profitability metrics
    profitability_columns = [
        'Return on Assets', 'Return on Equity', 'ROIC', 'Greenblatt ROC',
        'Gross Profit / Total Assets', 'Gross Margin', 'Operating Margin',
        'Net Margin', 'EBITDA Margin', 'Operating Margin vs Industry',
        'Net Margin vs Industry'
    ]

    # Convert percentage columns to numeric values
    for col in profitability_columns:
        if col in dataframe.columns:
            dataframe[col] = pd.to_numeric(dataframe[col].astype(str).str.strip('%'), errors='coerce')



    # Normalize the columns
    normalized_data = dataframe[profitability_columns].div(dataframe[profitability_columns].max())
    normalized_data.columns = normalized_data.columns.str.replace(' ', '_').str.replace('%', 'pct')

    # Assign weights to each column
    weights = {
        'Return on Assets': 8,
        'Return on Equity': 9,
        'ROIC': 8,
        'Greenblatt ROC': 7,
        'Gross Profit / Total Assets': 7,
        'Gross Margin': 7,
        'Operating Margin': 8,
        'Net Margin': 8,
        'EBITDA Margin': 8,
        'Operating Margin vs Industry': 7,
        'Net Margin vs Industry': 7
        }

    weights = normalize_weights(weights)

    # Calculate the score for each company based on the weighted sum of the columns
    scores = normalized_data.mul(weights.values()).sum(axis=1)

    # Add the score to the original dataframe
    dataframe['Score'] = scores

    # Sort the dataframe by the score in descending order
    sorted_data = dataframe.sort_values('Score', ascending=False)

    # Return the sorted dataframe with Ticker, Company, and Profitability Score columns
    return sorted_data[['Ticker', 'Company', 'Score']]


# ----------------- Other Functions ------------------ #
# Make sure the weights sum to 1, by changing the total weights proportionately
def normalize_weights(weights):
    total_weight = sum(weights.values())
    normalized_weights = {key: round(value / total_weight, 6) for key, value in weights.items()}
    return normalized_weights

def normalize_weights_list(weights):
    # Calculate the total weight
    total_weight = sum(weights)
    # Normalize each weight and round to 6 decimal places
    normalized_weights = [round(weight / total_weight, 6) for weight in weights]
    return normalized_weights

def extract_values_from_dict(dictionary):
    """
    This function extracts the values from a dictionary and puts them in an ordered list.
    The order of the values in the list is based on the order of the keys in the dictionary.

    Parameters:
    - dictionary (dict): The input dictionary from which to extract values.

    Returns:
    - list: A list containing the values extracted from the input dictionary.
    """
    # Extract values from the dictionary and put them in an ordered list
    values_list = list(dictionary.values())
    return values_list


def extract_tickers_from_csv(csv_content):
    """
    This function extracts the tickers (Symbol column) from a CSV content and puts them into a list.

    Parameters:
    - csv_content (str): The content of the CSV file.

    Returns:
    - list: A list containing the tickers (Symbol column) extracted from the CSV content.
    """
    df = pd.read_csv(csv_content)

    # Extract the tickers (Symbol column) and convert it to a list
    tickers = df['Symbol'].tolist()
    return tickers


# ----------------- Final Ranking ------------------ #

# put weights in as list in order of the dataframes
# Final Ranking companies based off the results from all the analysis
def rank_rows_weighted(*dataframes, weights=None):
    # Ensure that all DataFrames have the same number of rows
    n_rows = len(dataframes[0])
    for df in dataframes[1:]:
        assert len(df) == n_rows, "All DataFrames must have the same number of rows"

    # If no weights are provided, use equal weights for all DataFrames
    if weights is None:
        weights = [1 / len(dataframes)] * len(dataframes)
    else:
        assert len(weights) == len(dataframes), "The number of weights must match the number of DataFrames"

    # Calculate the weighted score for each row
    weighted_scores = pd.Series([0.0] * n_rows)
    for df, weight in zip(dataframes, weights):
        weighted_scores += df['Score'] * weight

    # Add the weighted scores as a new column to the first DataFrame
    result_df = dataframes[0].copy()
    result_df['weighted_score'] = weighted_scores

    # Rank the rows based on the weighted scores
    result_df['rank'] = result_df['weighted_score'].rank(ascending=False)
    result_df.sort_values('rank', ascending=True, inplace=True)

    # Reset the index of the DataFrame
    result_df.reset_index(drop=True, inplace=True)

    # Return the DataFrame with the added columns
    return result_df



