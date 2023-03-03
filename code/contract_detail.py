# contract_detail.py
''' Get contract detail for provided symbol'''

#------------------------------------------------------------------------------------------
# Imports ---------------------------------------------------------------------------------
from ib_insync import IB, Stock, Option, Contract, util
#import pandas as pd

# Local imports ---------------------------------------------------------------------------
import file    # my json file handler file.py

# Set global variables --------------------------------------------------------------------
PARMS = file.read_json("parms.json")
#PARMS["port"] = 7826    # can be used to over ride the Gateway port of 4002 with the TWS port 7826

def connect():
    ib = IB()
    try:
        ib.connect(PARMS["ip"], PARMS["port"], clientId=PARMS["id"])
        return ib
    except Exception as e:
        print(f"{PARMS} causes exception {e}")


# Create connection  ---------------------------------------------------------------------
myConn = connect()
if myConn.isConnected:
    print("Connection SUCCESS")
else:
    print("NOT CONNECTED")


# Create basic contract
# This is the contract format
# contract = Stock('AAPL', 'SMART', 'USD')

contract = Stock('TSLA', 'SMART', 'USD')

# Qualify contrack (fill in details)
myConn.qualifyContracts(contract)


sym = contract.symbol
sectype = contract.secType
pExchange = contract.primaryExchange

print(sym, sectype, pExchange)

