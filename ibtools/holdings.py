import datetime
from ib_insync import *
import file

import pandas as pd

parms = file.read_json("parms.json")
ib = IB()
ib.connect(parms["ip"], parms["port"], clientId=parms["id"])

balHeaders = [
        'Account, Net Liquidation', 'Secutities Gross Position', 'Cash', 'ask', 'askSize',
        'last', 'lastSize', 'close']

pos = ib.positions()
position = []
myAcct = []
myStocks = []
myOptions = []
myFX = []

# pos is a collection of all positions from ib.positions()
# This will filter the positions by security type (secType)
# For each type it will create a list such as myStocks
for s in pos:
    position.clear
    if s.contract.secType == 'STK':
        position = [s.account, s.contract.secType, s.contract.conId, s.contract.symbol, s.contract.exchange, s.contract.currency, s.contract.localSymbol, s.contract.tradingClass, s.position, s.avgCost]
        myStocks.append(position)
    elif s.contract.secType == 'OPT':
        position = [s.account, s.contract.conId, s.contract.symbol, s.contract.lastTradeDateOrContractMonth, s.contract.strike, s.contract.right, s.contract.multiplier, s.contract.currency, s.contract.localSymbol, s.contract.tradingClass, s.position, s.avgCost]
        myOptions.append(position)
    elif s.contract.secType == 'CASH':
        position = [s.account, s.contract.symbol, s.contract.conId, s.contract.localSymbol, s.contract.tradingClass, s.position, s.avgCost]
        myFX.append(position)
    else: print('ERROR: '.join(position))
    

# create a dataframe of myOptions
optionPos = pd.DataFrame(myOptions) 

# set the column header for stocks, options, FX
optionPos.columns = ['Account', 'ConId', 'Underlying', 'Exp', 'Strike', 'P/C', 'Multiplier', 'Curr', 'Symbol', 'Class', 'Position', 'AvgCost']

# make list of columns I want to display
optionDispCol = ['Account', 'Symbol', 'Exp', 'Strike', 'P/C', 'Multiplier', 'Class', 'Position', 'AvgCost', 'Curr']

#option_format_mapping = {"Strike": "{:,.2f}", 
#                        "Multiplier": "{:.0f}", 
#                        "Position": "{:.0f}"}
#                        "Exp": "{:%Y.%m.%d}"

# create a new dataframe from stocks and options by selcting the columns by lists created above
optionDisp = optionPos[optionDispCol]

#Format column data
#optionDisp.style.format(option_format_mapping)
optionDisp['Exp'] = pd.to_datetime(optionDisp['Exp'], format='%Y/%m/%d')
#optionDisp.style.format({"Strike": "{:,.2f}"})

optionDisp['Strike'] = optionDisp['Strike'].map('{:,.2f}'.format)

# suppress printing index in fromt of every row
# prints a nice dataframe of my option holdings
print(optionDisp.to_string(index = False))


ib.disconnect()
