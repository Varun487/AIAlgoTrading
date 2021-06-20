from pandas_datareader import data
import pandas as pd

# Get data from Yahoo finance
panel_data = data.DataReader('TCS.NS', 'yahoo', '2021-04-01', '2021-05-31')
print(panel_data)
panel_data.to_csv('../TCS_Yahoo_data.csv')
