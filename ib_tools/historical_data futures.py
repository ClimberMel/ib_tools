'''
Create sample for Futures data such as CL
'''

# Based on: chatGPT

from ib_insync import IB, Future, util

# Connect to IB Gateway or TWS
ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)

# Define the contract for Crude Oil Futures
contract = Future('CL', '202409', 'NYMEX')

# Request historical data
bars = ib.reqHistoricalData(
    contract,
    endDateTime='',
    durationStr='3 y',
    barSizeSetting='1 day',
    whatToShow='TRADES',
    useRTH=True,
    formatDate=1
)

# Convert the data to a pandas DataFrame
df = util.df(bars)
print(df)

# Disconnect
ib.disconnect()
