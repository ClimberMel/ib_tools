# portfolio.py
#   Parsing the PorfolioItem object
#   This will iterate through all the accounts and append to data into one DataFrame

from ib_insync import *
from ib_insync import objects
import pandas as pd
import datetime as dt
import code.file as file

parms = file.read_json("parms/parms.json")
pconnect = parms['connect']
acct = parms["account"]
space = ' '

myHoldings  = []      # create a list of my combined positions
position    = []      # temporary list to hold element from pos during parsing

header = ['Account', 'Alias', 'secType', 'conId', 'Symbol', 'Exchange', 'Currency', 'localSymbol', 'Position', 'avgCost', 'Contract Month', 'Strike', 'Right', 'Multiplier', 'Market Price', 'Market Value', 'Unrealized PNL', 'Realized PNL']

for i, a in enumerate(acct):
    myacct = a['account']
    alias = a['alias']
    
    ib = IB()
    ib.connect(pconnect["ip"], pconnect["port"], clientId=pconnect["id"], account=myacct)
    #ib.connect(pconnect["ip"], 7496, clientId=pconnect["id"], account=myacct)

    myPort = ib.portfolio()

    x = dt.datetime.now()                       # get current datetime
    now_str = x.strftime('%Y-%m-%d_%H-%M')      # format it to string and wothout mili seconds

    for s in myPort:
        
        position.clear
        if s.contract.secType == 'STK':
            position = [
                myacct, 
                alias,
                s.contract.secType, 
                s.contract.conId,
                s.contract.symbol, 
                s.contract.primaryExchange,
                s.contract.currency,
                s.contract.localSymbol,
                s.position,
                s.averageCost,
                None,
                None,
                None,
                None,
                s.marketPrice,
                s.marketValue,
                s.unrealizedPNL, 
                s.realizedPNL
                ]
            myHoldings.append(position)
        elif s.contract.secType == 'OPT':
            position = [
                myacct, 
                alias,
                s.contract.secType, 
                s.contract.conId,
                s.contract.symbol, 
                s.contract.primaryExchange,
                s.contract.currency,
                s.contract.localSymbol,
                s.position,
                s.averageCost,
                s.contract.lastTradeDateOrContractMonth, 
                s.contract.strike, 
                s.contract.right,
                s.contract.multiplier,
                s.marketPrice,
                s.marketValue,
                s.unrealizedPNL, 
                s.realizedPNL
                ]
            myHoldings.append(position)
        elif s.contract.secType == 'CASH':
            position = [
                myacct, 
                alias,
                s.contract.secType, 
                s.contract.conId,
                s.contract.symbol, 
                None,
                None,
                s.contract.localSymbol,
                s.position,
                s.averageCost,
                None,
                None, 
                None,
                None,
                s.marketPrice,
                s.marketValue,
                s.unrealizedPNL, 
                s.realizedPNL
                ]
            myHoldings.append(position)
        else: print('ERROR: '.join(position))

    ib.disconnect()

holdings = pd.DataFrame(myHoldings, columns = header)

# Write DataFrame to CSV File with Default params.
output_folder = 'output/'
holdings.to_csv(output_folder + now_str + "_portfolio.csv", index=False)
print("Saved to: ", output_folder + now_str + "_portfolio.csv")
