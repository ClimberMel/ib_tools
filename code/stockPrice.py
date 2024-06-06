
from ib_insync import *


import logging
#util.logToConsole(logging.DEBUG)

ib = IB()
#ib.connect('127.0.0.1', 7496, clientId=12)
ib.connect('127.0.0.1', 4001, clientId=16)

# Stock
stk = Contract()
stk.secType = "STK"
stk.exchange = "SMART"
stk.currency = "USD"
stk.symbol = "AAPL"

ib.qualifyContracts(stk)

data = ib.reqMktData(stk)
while data.last != data.last: ib.sleep(0.01) #Wait until data is in. 
ib.cancelMktData(stk)

#print(data)
print(stk.symbol, " Last: ", data.last)
