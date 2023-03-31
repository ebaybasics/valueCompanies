import pandas as pd


def normalize_and_score_financial_metrics(df, metrics_list, weights):
    # Copy the input dataframe to avoid modifying the original one
    df_copy = df.copy()

    # Replace spaces in the column names with underscores
    df_copy.columns = df_copy.columns.str.replace(' ', '_')

    # Convert specified metrics to numeric values if they aren't already
    for metric in metrics_list:
        df_copy[metric] = pd.to_numeric(df_copy[metric], errors='coerce')

    # Normalize the numeric metrics by dividing them by their respective maximum values
    normalized_metrics = df_copy[metrics_list].div(df_copy[metrics_list].max())

    # Normalize the weights so that they sum to 1
    total_weight = sum(weights.values())
    normalized_weights = {key: value / total_weight for key, value in weights.items()}

    # Multiply the normalized metrics by their respective normalized weights and calculate the overall score
    df_copy['score'] = (normalized_metrics * pd.Series(normalized_weights)).sum(axis=1)

    # Sort the companies by score in descending order
    df_copy = df_copy.sort_values(by='score', ascending=False)

    # Select the required columns and return the resulting dataframe
    return df_copy[['ticker', 'company', 'score']]


# Let's define a sample dataframe for testing
sample_data = {
    'ticker': ['AAPL', 'MSFT', 'GOOG'],
    'company': ['Apple Inc.', 'Microsoft Corp.', 'Alphabet Inc.'],
    'revenue': ['100', '80', '90'],
    'earnings': ['20', '18', '15'],
    'assets': ['500', '300', '400']
}

# Define the metrics list and weights for testing
metrics_list = ['revenue', 'earnings', 'assets']
weights = {'revenue': 0.5, 'earnings': 0.3, 'assets': 0.2}

# Create a sample dataframe and call the function
sample_df = pd.DataFrame(sample_data)
result_df = normalize_and_score_financial_metrics(sample_df, metrics_list, weights)
result_df