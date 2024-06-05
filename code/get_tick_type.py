
'''
Here's a brief explanation of some commonly used tick types in Interactive Brokers:
	tickType=1: Bid Price
	tickType=2: Ask Price
	tickType=3: Last Price
	tickType=4: High Price
	tickType=5: Low Price
	tickType=6: Volume
	tickType=7: Close Price

'''
from ib_insync import IB, Stock, TickByTickAllLast

# Connect to IB Gateway or TWS
ib = IB()
ib.connect('127.0.0.1', 4001, clientId=11)  # Change the host, port, and clientId as necessary

# Define the contract for which you want to request market data
contract = Stock('MMM', 'SMART', 'USD')

# Request tick-by-tick data for the contract, specifying tick type 'Last' (which corresponds to last trade price)
ticker = ib.reqTickByTickData(contract, 'Last')

# Define a callback function to handle tick data updates
def onTickByTickAllLast(tick):
    if isinstance(tick, TickByTickAllLast):
        print(f"Last Price: {tick.price}, Size: {tick.size}, Time: {tick.time}, Exchange: {tick.exchange}, Special Conditions: {tick.specialConditions}")

# Assign the callback function to the ticker's updateEvent
ticker.updateEvent += onTickByTickAllLast

# Start the event loop to receive data
try:
    ib.run()
except KeyboardInterrupt:
    pass  # Allow graceful exit with a keyboard interrupt

# Optionally, you can sleep for a specific duration and then stop the loop if needed
# ib.sleep(10)  # Wait for 10 seconds (adjust as needed)
# ib.disconnect()  # Disconnect from IB Gateway or TWS
