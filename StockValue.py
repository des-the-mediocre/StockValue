import pandas as pd
import pandas_datareader as reader
import datetime
from datetime import timedelta

version = '0.1'

today = datetime.date.today()
yesterday = today - timedelta(days=1)

def getStockValue(today, yesterday):
	print('Please enter the name of the stock:')
	name = input()
	name = name.upper()
	value = reader.DataReader(name, "google", yesterday, today)
	value = value.tail(1)
	return value

print('\nStockValue version ' + version + '\n')
value = getStockValue(today, yesterday)

print(value)
print('\n')
