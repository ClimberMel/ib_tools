'''
Create sample for Historical data for multiple contracts and contract types
'''

from ib_insync import IB, Future, Index, Stock, Option, util
import pandas as pd

# Connect to IB Gateway or TWS
ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)

# Define the contracts
contracts = [
    Index('TICK-NYSE', 'NYSE'),
    Index('TRIN-NYSE', 'NYSE'),
    Index('SPX', 'CBOE'),
    Index('VIX', 'CBOE'),
    Future('CL', '202411', 'NYMEX'),
    Stock('AAPL', 'SMART', 'USD'),
    Stock('AMZN', 'SMART', 'USD')
]

# Initialize an empty list to collect all DataFrames
all_dfs = []

# Request historical data
for contract in contracts:
    ib.qualifyContracts(contract)
    bars = ib.reqHistoricalData(
        contract, 
        endDateTime='', 
        barSizeSetting='1 day', 
        durationStr='3 y', 
        whatToShow='TRADES', 
        useRTH=False,
        timeout=500
    )

    # Convert the data to a pandas DataFrame
    df = util.df(bars)

    # Add a column with the contract name
    df.insert(0, 'Contract', contract.symbol)

    # Append the DataFrame to the list
    all_dfs.append(df)

    # Print the DataFrame
    print(df)

# Optionally, concatenate all DataFrames into one
final_df = pd.concat(all_dfs, ignore_index=True)

# Disconnect
ib.disconnect()
