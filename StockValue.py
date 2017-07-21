'''
Program takes input from users and makes a list of symbols representing stocks.
The program returns the values for the stocks the last day the exchange was open.
'''

import pandas as pd
import pandas_datareader as reader
import datetime
from datetime import timedelta

version = '0.2'

today = datetime.date.today()
yesterday = today - timedelta(days=1)

#method for finding values of stocks inputted by the user
def getStockValue(today, yesterday):
	names = []
	i = 1
	alldata = pd.DataFrame()
	print('Enter the companies you wish to check. \nLeave blank when finished.\n')
	while 1:
		company = input('Company nr.%d: ' %i)
		if company == '':
			break
		names.append(company.upper())
		i = i+1
	for name in names:
		stockdata = reader.DataReader(name, "google", yesterday, today)
		stockdata = stockdata.tail(1)
		alldata = alldata.append(stockdata)
	#list of columns to change order and add company names
	col = ['Company']
	col.extend(alldata.columns.tolist())
	alldata = alldata.assign(Company=names)
	return alldata[col]

print('\ndes the mediocre\'s StockValue \nv' + version + '\n')
stockvalues = getStockValue(today, yesterday)

print('\n')
print(stockvalues)
print('\n')
