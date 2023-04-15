''' 
Get contract detail for provided symbol
'''

#------------------------------------------------------------------------------------------
# Imports ---------------------------------------------------------------------------------
from ib_insync import IB, Stock, Option, Contract, util
#import pandas as pd

# Local imports ---------------------------------------------------------------------------
import file    # my json file handler file.py

#parms["port"] = 7826    # can be used to over ride the Gateway port of 4002 with the TWS port 7826
parms = file.read_json("parms/parms.json")
pconnect = parms['connect']
acct = parms["account"]
space = ' '
ib = IB()
ib.connect(pconnect["ip"], pconnect["port"], clientId=pconnect["id"])

# Create basic contract

#contract = Stock('TSLA', 'SMART', 'USD')
#contract = Contract(secType='STK', symbol='AAPL', exchange='SMART', currency='USD')
contract = Contract(secType='OPT', symbol='AAPL', exchange='SMART', currency='USD')

# Qualify contrack (fill in details)
ib.qualifyContracts(contract)

sym = contract.symbol
sectype = contract.secType
pExchange = contract.primaryExchange


print(sym, sectype, pExchange)

