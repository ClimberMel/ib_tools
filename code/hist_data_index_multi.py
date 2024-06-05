'''
The ib.reqHistoricalData() works back in time.  
It starts at the end date and goes back until it runs out of bars
This will process multiple index contracts
'''

# https://groups.io/g/insync/message/8991

from ib_insync import *
import pandas as pd

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=11)

# I need data subscription for this to work (currently only SPX, Tick, Trin & VIX works)
#contracts = [Index('TICK-NYSE', 'NYSE'),Index('TRIN-NYSE', 'NYSE'),Index('SPX', 'CBOE'),Index('INDU', 'NYSE'),Index('COMP', 'NASDAQ'),Index('VIX', 'CBOE')]
contracts = [Index('TICK-NYSE', 'NYSE'), Index('TRIN-NYSE', 'NYSE'), Index('SPX', 'CBOE'), Index('VIX', 'CBOE')]

for contract in contracts:
    ib.qualifyContracts(contract)
    historical_data = ib.reqHistoricalData(
        contract, 
        endDateTime='', 
        barSizeSetting = '1 min', 
        durationStr = '1 M', 
        whatToShow = 'TRADES', 
        useRTH = False,
        timeout=500
        )
    # Convert to dataframe -------------------------------------------------------------------
    histDF = pd.DataFrame(historical_data)
    #histDF['Symbol'] = contract.symbol         # Adds the symbol name in a new column Symbol to the end
    histDF.insert(0,"Symbol", contract.symbol)  # Inserts the coolmn as the first column (0)
    #histDF.insert(1,"Symbol", contract.symbol)  # Inserts the symbol after the datetime column(1)

    # Print the first 5 lines for testing
    print(histDF.head())
