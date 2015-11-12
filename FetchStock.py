import urllib
import urllib2
import time


today = time.strftime("%Y-%m-%d")

ticker = 'MSFT'
startDate = '2015-01-01'
endDate = today


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

# print url
response = urllib2.urlopen(url)
print ''.join(response.readlines())



