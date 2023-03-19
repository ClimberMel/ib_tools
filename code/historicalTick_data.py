'''
Fetch Historical tick data

Historical tick data can be fetched with a maximum of 1000 ticks at a time. 
Either the start time or the end time must be given, and one of them must remain empty:
'''

import datetime
from ib_insync import *
import pandas as pd


# Start IB session running
ib = IB()
ib.connect('127.0.0.1', 4002, clientId=2)
#ib.connect('127.0.0.1', 7496, clientId=1)

# Create some Forex contracts:
contracts = [Forex(pair) for pair in ('EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'USDCAD', 'AUDUSD')]
ib.qualifyContracts(*contracts)

eurusd = contracts[0]

start = ''
end = datetime.datetime.now()
ticks = ib.reqHistoricalTicks(eurusd, start, end, 1000, 'BID_ASK', useRth=False)

#print(ticks[-1])
#print(ticks)
print(util.df(ticks))

ib.disconnect()