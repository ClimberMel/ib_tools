'''
The ib.reqHistoricalData() works back in time.  
It starts at the end date and goes back until it runs out of bars or reaches the duration
or you can set a start date (startdt) so it quits when it gets there.
'''

import datetime as dt
from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=102)
#ib.connect('127.0.0.1', 7496, clientId=106)

# Get path of running module
import sys, os
cDir = os.path.dirname(sys.argv[0])
cDir = cDir + '/output/'

#contract = Stock('TSLA', 'SMART', 'USD')
contract = Stock('MMM', 'SMART', 'USD')

#dt = YYYYMMDD{SPACE}hh:mm:ss[{SPACE}TMZ]
#startdt = dt.datetime(2023, 1, 15)


# comtract:         a qualified contract not just a ticker
# endDateTime:      the start of the loop as it starts with current and goes back through time.
#                   so it will get everything BEFORE that time.
#                   Example: edt = '20221230 23:59:59' will get all bars befor the end of 2022
#                            edt = '' will get everything before the current bar depending on durationStr
# duration:         the time frame reqHistoricalData will go back
# NOTE:             duration format is integer{SPACE}unit (S|D|W|M|Y)
# barSizeSetting:   size of each bar data to return, 1 min, 5 min, 1 hour, 1 day etc
# whatToShow:       TRADES, MIDPOINT, BID, ASK etc
# useRTH            True or False, show Regular Trading Hours
# formatDate:       set to 1, but not sure what it does...


#edt = '20000101 00:00:01'
edt = ''

barsList = []
bars = ib.reqHistoricalData(
    contract,
    endDateTime=edt,
    durationStr='10 Y',
    barSizeSetting='1 day',
    whatToShow='TRADES',
    useRTH=True,
    formatDate=1)

barsList.append(bars)

# save to CSV file
allBars = [b for bars in reversed(barsList) for b in bars]
df = util.df(allBars)
#df.to_csv(cDir + contract.symbol + ' 1day.csv', index=False)
print(df)