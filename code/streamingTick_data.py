'''
Streaming tick data
Keep in mind this will keep on running...
You need a provision to cancel it.
'''

import datetime
from ib_insync import *
import pandas as pd

# Start IB session running
ib = IB()
ib.connect('127.0.0.1', 4001, clientId=2)
#ib.connect('127.0.0.1', 7496, clientId=1)

# Create some Forex contracts:
contracts = [Forex(pair) for pair in ('EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'USDCAD', 'AUDUSD')]
ib.qualifyContracts(*contracts)

eurusd = contracts[0]

# Request streaming ticks for them:
for contract in contracts:
    ib.reqMktData(contract, '', False, False)

# Wait a few seconds for the tickers to get filled.
ticker = ib.ticker(eurusd)
ib.sleep(2)

print(ticker)

# The price of Forex ticks is always nan. To get a midpoint price use midpoint() or marketPrice().
# The tickers are kept live updated, try this a few times to see if the price changes:
print(ticker.marketPrice())

# The following cell will start a 30 second loop that prints a live updated ticker table. It is updated on every ticker change.
df = pd.DataFrame(
    index=[c.pair() for c in contracts],
    columns=['bidSize', 'bid', 'ask', 'askSize', 'high', 'low', 'close'])

def onPendingTickers(tickers):
    for t in tickers:
        df.loc[t.contract.pair()] = (
            t.bidSize, t.bid, t.ask, t.askSize, t.high, t.low, t.close)
    print(df)        

ib.pendingTickersEvent += onPendingTickers
ib.sleep(30)
ib.pendingTickersEvent -= onPendingTickers

for contract in contracts:
    ib.cancelMktData(contract)
