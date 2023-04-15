# findPositions
# Don't need account for positions like you do in portfolio
# 2023-04-15 created by ClimberMel
# I want to be able to find open positions in case conditions state they need to be closed

from ib_insync import *
import pandas as pd
import datetime as dt
import file

parms = file.read_json("parms/parms.json")
pconnect = parms['connect']

ib = IB()
ib.connect(pconnect["ip"], pconnect["port"], clientId=pconnect["id"])

positions = ib.positions()  # A list of positions from IB
for position in positions:
    contract = position.contract
    if position.position > 0: # Active Long positions
        direction = "Long "
    elif position.position < 0: # Active Short positions
        direction = 'Short' 
    else:
        assert False
    totalQuantity = abs(position.position)
    #print(f'Position: {direction} {totalQuantity} {contract.localSymbol}')
    print(f'Position: {direction} {position.account} {contract.secType} {contract.currency} {position.position} {contract.localSymbol}')
print('End process')
ib.disconnect()
