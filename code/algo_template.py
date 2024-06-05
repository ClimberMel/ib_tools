"""From ib_insyc forum Message #6484
1a.
Re: Async event handling problem with orderStatusEvent
From: Patrick Dufour
Date: Tue, 29 Jun 2021 05:17:33 CEST

I made this little example to show you how to use CallBack. I picked and chose codes from many places in my differents projects. 
I just make it works, I didn't made lots of effort to be clean code.

So in your exemple you want to execute code when the event orderStatusEvent happen. 
In my example you have to put this code in the function onOrderStatusEvent.
"""

import logging
from logging.handlers import TimedRotatingFileHandler

# NOTE: These could be changed to use ib_async now

from ib_insync import IB, ib, util
from ib_insync import * 

ib = IB()

logname = "logs.log"
FORMAT = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)


def onConnectedEvent():
    logger.info('connected')

def onDisconnectedEvent():
    logger.info('disconnected')

def onPendingTickersEvent(ticker):
    logger.info(ticker)
    for t in ticker:
        bid = t.bid if not util.isNan(t.bid) else 0
        ask = t.ask if not util.isNan(t.ask) else 0
        last = t.last if not util.isNan(t.last) else t.markPrice
        logger.info({'conid': t.contract.conId,'bid': t.bid, 'ask': t.ask, 'last': t.last})

def onNewOrderEvent(Trade):
    logger.info(Trade)

def onCancelOrderEvent(Trade):
    logger.info(Trade)

def onPositionEvent(Position):
    logger.info(Position)

def onErrorEvent(reqId, errorCode, errorString, contract):
    data = {'action': 'errorEvent','reqId':reqId, 'errorCode':errorCode, 'errorString':errorString, 'contract': contract}
    logger.info(data)

def onOrderModifyEvent(Trade):
    logger.info(Trade)

def onOrderStatusEvent(Trade):
    logger.info(Trade)

def isConnected():
    connected = True
    if not ib.isConnected(): connected = False
    return connected

def connect():
    if not ib.isConnected():
        ib.connect('127.0.0.1', '7496', clientId=4)
        ib.reqMarketDataType(1)

def disconnect():
    if ib.isConnected(): 
        ib.disconnect()
def createContractByConId(conid):
    contract = Contract(conId=conid)
    ib.qualifyContracts(contract)
    return contract

def createOrder(orderType, price, side, quantity):
    if orderType == 'MKT':
        order = MarketOrder(side, quantity, tif='GTC', outsideRth = True)
    else:
        order = LimitOrder(side, quantity, price, tif='GTC', outsideRth = True)
    return order

def placeOrder(contract, order):
    ib.placeOrder(contract, order)

def executeMyStrategy():
        contract = createContractByConId(4391)  #AMD stock = 4391
        order = createOrder("LMT", 80.00, "BUY", 1) 
        placeOrder(contract, order)

        contract = createContractByConId(4391)  #AMD stock = 4391
        order = createOrder("LMT", 81.00, "BUY", 1) 
        placeOrder(contract, order)

        contract = createContractByConId(4391)  #AMD stock = 4391
        order = createOrder("LMT", 82.00, "BUY", 1) 
        placeOrder(contract, order)

def bindEvents():
        ib.connectedEvent += onConnectedEvent
        ib.disconnectedEvent += onDisconnectedEvent
        ib.pendingTickersEvent += onPendingTickersEvent
        ib.newOrderEvent += onNewOrderEvent
        ib.cancelOrderEvent += onCancelOrderEvent
        ib.positionEvent += onPositionEvent
        ib.errorEvent += onErrorEvent
        ib.orderModifyEvent += onOrderModifyEvent
        ib.orderStatusEvent += onOrderStatusEvent
def main():
    bindEvents()
    connect()
    executeMyStrategy()
    IB.run()


if name == 'main':
    main()
