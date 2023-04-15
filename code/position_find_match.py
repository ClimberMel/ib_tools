'''
position_find_match.py
2023-04-15 created by ClimberMel
Doesn't need account# like you do in portfolio
I want to be able to find open positions in case conditions state they need to be closed
It will use patten matching.
    RY will give both US & CAD matches as well as any options like covered calls
    AA would give both AA - Alcoa as well as AAPL - Apple so this would need to be used with caution
''' 

from ib_insync import *
import pandas as pd
import datetime as dt
import file

parms = file.read_json("parms/parms.json")
pconnect = parms['connect']
searchfor = "RY"
space = ' '
ib = IB()
ib.connect(pconnect["ip"], pconnect["port"], clientId=pconnect["id"])
#ib.connect(pconnect["ip"], 4003, clientId=pconnect["id"])  
#ib.connect(pconnect["ip"], 7496, clientId=pconnect["id"])

positions = ib.positions()  # A list of positions, according to IB
for position in positions:
    contract = position.contract
    if searchfor in contract.localSymbol:
        print(f'Position: {position.account} {contract.secType} {contract.currency} {position.position} {contract.localSymbol}')

print('End process')
ib.disconnect()
