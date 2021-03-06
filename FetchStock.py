import urllib
import urllib2
import time
import json
from matplotlib import pyplot


today = time.strftime("%Y-%m-%d")

ticker = 'MSFT'
startDate = '2015-01-01'
endDate = today


def fetchstock(ticker, startDate, endDate):
    url = 'https://query.yahooapis.com/v1/public/yql?q='
    url += urllib2.quote('select * from yahoo.finance.historicaldata')
    url += urllib2.quote(' where symbol = "%s"' % ticker)
    url += urllib2.quote(' and startDate = "%s"' % startDate)
    url += urllib2.quote(' and endDate = "%s"' % endDate)

    url += '&' + urllib.urlencode([
        ('format', 'json'),
        ('diagnostics', 'true'),
        ('env', 'store://datatables.org/alltableswithkeys'),
        ('callback', '')])

    twait = 5  # waiting time to not exceed yahoo quota
    tstart = time.time()
    response = urllib2.urlopen(url)
    tend = time.time()
    tdiff = tend-tstart
    time.sleep(max(0, twait-tdiff))
    return response  # ''.join(response.readlines())

response = fetchstock(ticker, startDate, today)
data = json.load(response)
try:
    node = data['query']['results']['quote']
except TypeError:
    node = []

# for i, entry in enumerate(node):
#     keys = ['Date', 'Close', 'Volume']
#     print [entry.get(key) for key in keys]

xval, xticklabel, yval = [], [], []
for i, entry in enumerate(reversed(node)):
    xval.append(i)
    xticklabel.append(entry['Date'])
    yval.append(entry['Close'])

pyplot.plot(xval, yval)
pyplot.xticks(xval, xticklabel, rotation=80)
pyplot.subplots_adjust(bottom=0.15)
pyplot.show()
