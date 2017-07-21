'''
Program takes input from users and makes a list of symbols representing stocks.
The program returns the values for the stocks the last day the exchange was open.
'''

import pandas as pd
import pandas_datareader as reader
import datetime
from datetime import timedelta

version = '0.3'

today = datetime.date.today()
yesterday = today - timedelta(days=1)

#method for 
def getCompanies():
	names = []
	i = 1
	print('Enter the companies you wish to check. \nLeave blank when finished.\n')
	while 1:
		company = input('Company nr.%d: ' %i)
		if company == '':
			break
		names.append(company.upper())
		i = i+1
	return names

def getStockValue(names, today, yesterday):
	alldata = pd.DataFrame()
	alldata = reader.get_quote_google(names)
	#alldata = alldata['time'].dt.time
	return alldata

def getHistoric(names):
	alldata = pd.DataFrame()
	for name in names:
		stockdata = reader.DataReader(name, "google", yesterday, today)
		stockdata = stockdata.tail(1)
		alldata = alldata.append(stockdata)
	#col = ['Company']
	#col.extend(alldata.columns.tolist())
	alldata = alldata.assign(Company=names)
	#alldata = alldata[col]
	alldata = alldata.set_index(['Company'], append=True)
	return alldata

print('\ndes the mediocre\'s StockValue \nv' + version + '\n')
#companies = getCompanies()
companies = ['AAPL','MSFT']
stockvalues = getStockValue(companies, today, yesterday)
historicvalues = getHistoric(companies)

print('\n')
print(stockvalues)
print('\n')
print(historicvalues)
print('\n')
