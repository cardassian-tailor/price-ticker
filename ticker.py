import requests
from lxml import html

page = requests.get('https://www.worldcoinindex.com/')
tree = html.fromstring(page.content)
#b=tree.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/table/tbody/tr/td[4]/text()')[0].split()[1]



ETH = tree.xpath('//*[@id="myTable"]/tbody/tr[2]/td[5]/span[2]/text()')
BTC = tree.xpath('//*[@id="myTable"]/tbody/tr[1]/td[5]/span[2]/text()')
LTC = tree.xpath('//*[@id="myTable"]/tbody/tr[3]/td[5]/span[2]/text()')
XMR = tree.xpath('//*[@id="myTable"]/tbody/tr[8]/td[5]/span[2]/text()')
ZEC = tree.xpath('//*[@id="myTable"]/tbody/tr[20]/td[5]/span[2]/text()')
BAT = tree.xpath('//*[@id="myTable"]/tbody/tr[17]/td[5]/span[2]/text()')
NEO = tree.xpath('//*[@id="myTable"]/tbody/tr[12]/td[5]/span[2]/text()')
SNT = tree.xpath('//*[@id="myTable"]/tbody/tr[66]/td[5]/span[2]/text()')

print("ETH price is: ", ETH) 
print("LTC price is: ", LTC)
print("BTC price is: ", BTC)
print("Monero price is: ", XMR)
print("ZCASH price is: ", ZEC)
print("BAT price is: ", BAT)
print("NEO: ", NEO)
print("Status: ", SNT)
