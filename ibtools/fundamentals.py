# contract.py
''' Get contract detail for provided symbol'''

# This is the contract format
# contract = Stock('AAPL', 'SMART', 'USD')

from ib_insync import *
ib = IB()
ib.connect(host='127.0.0.1', port=4002, clientId=99)

exchange = 'SMART'
currency = 'USD'

contract = Stock('AAPL', 'SMART', 'USD')
print(contract)
ib.qualifyContracts(contract)

contract = Stock('IBM', 'SMART', 'USD')
ticker = ib.reqMktData(contract, '258')
ib.sleep(2)
print(ticker.fundamentalRatios)
