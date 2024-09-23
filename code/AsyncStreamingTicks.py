# https://web.archive.org/web/20230322131733/https://ib-insync.readthedocs.io/recipes.html#async-streaming-ticks
# Not sure why this was removed from Ewalds Code Recipes.  
# Perhaps there were too many issues with using async that he didn't want to deal with all the questions

import asyncio

import ib_insync as ibi

class App:

    async def run(self):
        self.ib = ibi.IB()
        with await self.ib.connectAsync('127.0.0.1', 4001, clientId=1):
            contracts = [
                ibi.Stock(symbol, 'SMART', 'USD')
                for symbol in ['AAPL', 'TSLA', 'AMD', 'INTC']]
            for contract in contracts:
                self.ib.reqMktData(contract)

            async for tickers in self.ib.pendingTickersEvent:
                for ticker in tickers:
                    print(ticker)

    def stop(self):
        self.ib.disconnect()


app = App()
try:
    asyncio.run(app.run())
except (KeyboardInterrupt, SystemExit):
    app.stop()