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

newsProviders = ib.reqNewsProviders()
print(newsProviders)
codes = '+'.join(np.code for np in newsProviders)

ib.qualifyContracts(contract)
headlines = ib.reqHistoricalNews(contract.conId, codes, '', '', 10)
latest = headlines[0]
print("--Latest Headline-----------------------------------------------------------------------------")
print(latest)
article = ib.reqNewsArticle(latest.providerCode, latest.articleId)
print("--Latest Article------------------------------------------------------------------------------")
print(article)