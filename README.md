# valueCompanies
Finding the best companies using a large number of datapoints

Program README
This program imports data from stockrover and performs valuations and rankings on various metrics to provide an overall picture of the health of a stock. Here are the steps to use this program:

Get Data from Tables at stockrover in csv form.
Insert data in relevant placholder_stock_rover_data.py
Run the program.
The program uses the following files:

convertText2CSV.py: contains a function that converts text to CSV table format
valuation_funs.py: contains functions for calculating valuations and rankings
placholder_stockrover_data.py: contains placeholder data that should be replaced with actual data from stockrover
The program imports the following libraries:

pandas
StringIO
To run the program, follow these steps:

Import the required libraries
Get Watchlist Tickers from TOS csv in the folder watchlists
Import Relevant Data
Read the data into a DataFrame
Get results from the DataFrame
Assign Levels of Importance for each metric
Print the final results
Please exercise caution when working with hidden files and modifying the code. Make sure to replace the placeholder data with actual data from stockrover before running the program.
