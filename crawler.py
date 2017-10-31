import urllib2
from bs4 import BeautifulSoup

def search_links(symbol):
    url = 'https://seekingalpha.com/symbol/'+ symbol + '/focus'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=hdr)
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html)
    tables = soup.find_all("div", class_="content_block_investment_views")[0]
    return tables

