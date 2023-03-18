''' 
news.py
2023-03-18 created by ClimberMel
an assorment of code to retrieve News articles from IB
''' 

from ib_insync import *
import pandas as pd
import datetime as dt
import file

parms = file.read_json("parms/parms.json")
pconnect = parms['connect']
#acct = parms["account"]
#myacct = acct[3]['account']
#print(myacct)

ib = IB()
ib.connect(pconnect["ip"], 
           pconnect["port"], 
           clientId=0           # clientId=0 will show orders placed in TWS.
          )


def DJNLbroadtapeNewsFeed():
        #! [newscontractbz]
        contract = Contract()
        contract.symbol = "DJNL:DJNL_ALL"
        contract.secType = "NEWS"
        contract.exchange = "DJNL"
        #! [newscontractbz]
        return contract

def getNews():
    x = dt.datetime(2020, 6, 20)
    y = dt.datetime(2020, 6, 27)
    print(x,y)
    newsProviders = ib.reqNewsProviders()
    print(newsProviders)
    codes = '+'.join(np.code for np in newsProviders)
    print(codes)
    amd = Stock('AMD', 'SMART', 'USD')
    ib.qualifyContracts(amd)
    print(amd)
    headlines = ib.reqHistoricalNews(amd.conId, codes ,x,y, 10)
    print(headlines)
    latest = headlines[0]
    print(latest)
    article = ib.reqNewsArticle(latest.providerCode, latest.articleId)
    print(article)

def getBRnews():
        news = ib.reqHistoricalNews(268084, "BRFG+BRFUPDN+DJNL", "",   "", 100, [])
        df = util.df(news)
        print(df)

#print(DJNLbroadtapeNewsFeed())
#getBRnews()
getNews()

ib.disconnect()