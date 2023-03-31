import pandas as pd
from io import StringIO
import convertText2CSV
import valuation_funs
import placholder_stockrover_data

# ----------- Instructions ---------- #
# Get Data from Tables at stockrover in csv form.
# Insert data in relevant placholder_stock_rover_data.py
# run program

# Get Watchlist Tickers from TOS csv in folder watchlists
watchlists = valuation_funs.extract_tickers_from_csv('./watchlists/2023-03-30-watchlist.csv')


# Import Relevant Data
growth_data = placholder_stockrover_data.growth_data
quickValData = placholder_stockrover_data.quick_valuation_data
profitibility_data = placholder_stockrover_data.profitability
financial_health = placholder_stockrover_data.financial_health
#  Market share uses the income statement line items Sales as total and takes each company as a percentage of total sales
market_share = placholder_stockrover_data.income_data
per_share = placholder_stockrover_data.per_share



# Read the data into a DataFrame
growth_data = pd.read_csv(StringIO(convertText2CSV.text_to_csv_table(growth_data)), on_bad_lines='skip')
quickValData = pd.read_csv(StringIO(convertText2CSV.text_to_csv_table(quickValData)), on_bad_lines='skip')
profitibility_data = pd.read_csv(StringIO(convertText2CSV.text_to_csv_table(profitibility_data)), on_bad_lines='skip')
financial_health = pd.read_csv(StringIO(convertText2CSV.text_to_csv_table(financial_health)), on_bad_lines='skip')
market_share = pd.read_csv(StringIO(convertText2CSV.text_to_csv_table(market_share)), on_bad_lines='skip')
per_share = pd.read_csv(StringIO(convertText2CSV.text_to_csv_table(per_share)), on_bad_lines='skip')

# Get results from dataframe
growth_data_results = valuation_funs.growth(growth_data)
valuation_results = valuation_funs.valuation_quick(quickValData)
profitibility_results = valuation_funs.rank_by_profitability(profitibility_data)
financial_health_results = valuation_funs.financial_health(financial_health)
market_share_results = valuation_funs.rank_by_market_share(market_share)
per_share_results = valuation_funs.per_share(per_share)

# Assign Levels of Importance for each metric
result_weights = {
    'Growth': 9,
    'Valuation': 7,
    'Profitability': 6,
    'Financial_Health': 4,
    'Market_Share': 0,
    'Per_Share': 4

}

weights = valuation_funs.normalize_weights_list(valuation_funs.extract_values_from_dict(result_weights))


# print(valuation_funs.rank_rows_weighted(financial_health_results, per_share_results,market_share_results, profitibility_results, valuation_results, growth_data_results, weights=weights))
print(valuation_funs.rank_rows_weighted(financial_health_results, per_share_results, market_share_results, profitibility_results, valuation_results, growth_data_results, weights=weights))