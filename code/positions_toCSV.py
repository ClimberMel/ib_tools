# viewPositions.py
# 2022-07-19 created by ClimberMel
# Used content from getPositions and getHoldings variations
# I have removed all the unneeded code for just viewing and writing to csv all my combined holdings.
# This currently (2022-11-20) both displays in a dataframe and writes it out to a CSV file
# 2023-04-03: Modified to use new parms.json format for connection

from ib_insync import *
import pandas as pd
import datetime as dt
import file

parms = file.read_json("parms/parms.json")
pconnect = parms['connect']

ib = IB()
ib.connect(pconnect["ip"], pconnect["port"], clientId=pconnect["id"])

pos = ib.positions()

position    = []      # temporary list to hold element from pos during parsing
myPositions  = []      # create a list of my combined positions

header = ['Account', 'Alias', 'secType', 'conId', 'Symbol', 'Exchange', 'Currency', 'localSymbol', 'tradingClass', 'Position', 'avgCost', 'ContractMonth', 'Strike', 'Right', 'Multiplier']
x = dt.datetime.now()                       # get current datetime
now_str = x.strftime('%Y-%m-%d_%H-%M')

accounts = file.read_json("parms/accounts.json")

#None can be used as a place holder for rows that have missing elements
for s in pos:
    position.clear
    if s.contract.secType == 'STK':
        position = [s.account, accounts[s.account], s.contract.secType, s.contract.conId, s.contract.symbol, s.contract.exchange, s.contract.currency, s.contract.localSymbol, s.contract.tradingClass, s.position, s.avgCost, None, None, None, None]
        myPositions.append(position)
    elif s.contract.secType == 'OPT':
        position = [s.account, accounts[s.account], s.contract.secType, s.contract.conId, s.contract.symbol, None, s.contract.currency, s.contract.localSymbol, s.contract.tradingClass, s.position, s.avgCost, s.contract.lastTradeDateOrContractMonth, s.contract.strike, s.contract.right, s.contract.multiplier]
        myPositions.append(position)
    elif s.contract.secType == 'CASH':
        position = [s.account, accounts[s.account], s.contract.secType, s.contract.conId, s.contract.symbol, None, None, s.contract.localSymbol, s.contract.tradingClass, s.position, s.avgCost, None, None, None, None]
        myPositions.append(position)
    else: print('ERROR: '.join(position))

print('Start process')

positions = pd.DataFrame(myPositions, columns = header)

# Using DataFrame.to_string() to print without index
dfh = positions.to_string(index=False)

# Write DataFrame to CSV File with Default params.
output_folder = 'output/'
positions.to_csv(output_folder + now_str + " positions.csv", index=False)

print(dfh)

print('End process.  File saved to: ' + output_folder + now_str + " positions.csv")
ib.disconnect()
