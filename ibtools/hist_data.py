# hist_data.py
''' Get historical data for multiple symbols'''

import csv

from ib_insync import *
ib = IB()
#ib.connect(host='127.0.0.1', port=4002, clientId=1)
ib.connect(host='127.0.0.1', port=4002, clientId=99)

exchange = 'SMART'
currency = 'USD'
barSizeSetting = '1 day'
durationStr = '1 M'
whatToShow = 'TRADES'
symbols = ['AAPL', 'GOOGL', 'MSFT', 'ZM']
contracts = []
allRows = []
headers = ['Symbol', 'Date', 'Open', 'High', 'Low', 'Close']

#contract = Stock('AAPL', 'SMART', 'USD')
for symbol in symbols:
    contracts.append(Stock(symbol, exchange, currency))

for contract in contracts:
    bars = ib.reqHistoricalData(contract=contract, barSizeSetting=barSizeSetting, endDateTime='', durationStr=durationStr, whatToShow=whatToShow, useRTH=True)
    rows = []
    for bar in bars:
        rows.append([contract.symbol, bar.date, bar.open, bar.high, bar.low, bar.close])
    with open("./{}.csv".format(contract.symbol), 'w') as f:
        write = csv.writer(f)
        write.writerow(headers)
        write.writerows(rows)
    
    allRows = allRows + rows

print(allRows)