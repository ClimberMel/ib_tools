from ib_insync import IB, Option

# Connect to IB Gateway or TWS
ib = IB()
#ib.connect('127.0.0.1', 7497, clientId=1)
ib.connect('127.0.0.1', 4001, clientId=103)

# Define the SPX option contract
spx_option = Option(
    symbol='SPX',
    lastTradeDateOrContractMonth='20250113',
    strike=5905.0,
    right='P',  # 'C' for Call, 'P' for Put
    exchange='SMART'
)

# Request contract details
contract_details = ib.reqContractDetails(spx_option)

# Print the details
for detail in contract_details:
    print(detail)