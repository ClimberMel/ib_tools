# Here is the layout for the returned Portfolio Item

## ib.portfolio() returns a List[PortfolioItem]

- for portfolio you need to connect using one account (unlike positions, it won't return all accounts)
- You can then loop through the list and get each PortfolioItem
- Then you can select PortfolioItem.position or .realizedPNL to get the various data

## Here is the structure of each PortfolioItem.  I have included one each for STK, OPT and FX

```
PortfolioItem(
	contract=Stock(conId=334902388, 
			symbol='NWN', 
			right='0', 
			primaryExchange='NYSE', 
			currency='USD', 
			localSymbol='NWN', 
			tradingClass='NWN'), 
	position=10.0, 
	marketPrice=47.30810165, 
	marketValue=473.08, 
	averageCost=48.27314, 
	unrealizedPNL=-9.65, 
	realizedPNL=0.0, 
	account='X1234567')

PortfolioItem(
	contract=Option(conId=592137994, 
			symbol='NA', 
			lastTradeDateOrContractMonth='20230421', 
			strike=105.0, 
			right='C', 
			multiplier='100', 
			primaryExchange='CDE',
			currency='CAD', 
			localSymbol='NA    230421C00105000', 
			tradingClass='NA'), 
	position=-1.0, 
	marketPrice=0.06998345, 
	marketValue=-7.0, 
	averageCost=103.5, 
	unrealizedPNL=96.5, 
	realizedPNL=0.0, 
	account='X1234567')
	
PortfolioItem(
	contract=Forex('USDCAD', 
			conId=15016062, 
			right='0', 
			primaryExchange='IDEALPRO', 
			localSymbol='USD.CAD', 
			tradingClass='USD.CAD'), 
	position=15010.0, 
	marketPrice=1.37310005, 
	marketValue=20610.23, 
	averageCost=1.2548713, 
	unrealizedPNL=1774.61, 
	realizedPNL=0.0, 
	account='X1234567')
```

