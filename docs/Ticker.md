# Layout of Ticker object

## If you use reqMktData(contract) this is what is returned

```python
# Stock
stk = Contract()
stk.secType = "STK"
stk.exchange = "SMART"
stk.currency = "USD"
stk.symbol = "AAPL"

myConn.qualifyContracts(stk)

data = myConn.reqMktData(stk)
while data.last != data.last: myConn.sleep(0.01) #Wait until data is in. 
myConn.cancelMktData(stk)

print(data)
```

### The output of data

Ticker(
	contract=Contract(
		secType='STK', 
		conId=265598, 
		symbol='AAPL', 
		exchange='SMART', 
		primaryExchange='NASDAQ', 
		currency='USD', 
		localSymbol='AAPL', 
		tradingClass='NMS'), 
	time=datetime.datetime(2023, 3, 3, 17, 8, 54, 238411, tzinfo=datetime.timezone.utc), 
	minTick=0.01, 
	bid=149.57, 
	bidSize=1000.0, 
	bidExchange='KPQVZU', 
	ask=149.58, askSize=400.0, 
	askExchange='QZU', 
	last=149.76, 
	lastSize=300.0, 
	lastExchange='D', 
	open=147.95, 
	ticks=[	TickData(
				time=datetime.datetime(2023, 3, 3, 17, 8, 54, 238411, tzinfo=datetime.timezone.utc), 
				tickType=4, 
				price=149.76, 
				size=300.0), 
			TickData(
				time=datetime.datetime(2023, 3, 3, 17, 8, 54, 238411, tzinfo=datetime.timezone.utc), 
				tickType=5, 
				price=149.76, 
				size=300.0), 
			TickData(
				time=datetime.datetime(2023, 3, 3, 17, 8, 54, 238411, tzinfo=datetime.timezone.utc), 
				tickType=14, 
				price=147.95, 
				size=0.0)], 
	bboExchange='9c0001', 
	snapshotPermissions=3)
'''