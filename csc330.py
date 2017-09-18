  GNU nano 2.2.6                                File: csc330.py                                                                       

import pandas_datareader as pdr
import csv
import pandas
import json
from pandas_datareader.data import Options
from datetime import date

stocks = ['AAPL','GOOGL', 'AMZN', 'FB', 'SSNLF', 'MSFT', 'SNE', 'IBM', 'NTDOY', 'ORCL', 'VMW', 'INTC', 'HPQ', 'DVMT',
'CSCO', 'ADBE', 'SAP', 'LNVGY', 'RHT', 'SYMC', 'TWTR', 'ATNY', 'ACTS', 'ATVI', 'IOTS', 'ADRO', 'AMD', 'ADVS', 'ZBRA',
'XPLR', 'XBIT', 'WIX', 'WBMD', 'VNOM', 'VIA', 'VECO', 'UPLD', 'UBNT', 'UFPT', 'TYME', 'TRIV', 'TRIP', 'TGA', 'TSI',
'TESS', 'AIR', 'ATEN', 'AQN', 'DDD', 'WUBA', 'ASX', 'A', 'AYX', 'AMBR', 'AEE', 'BHE', 'BIO', 'CPL', 'CTS', 'CMI', 'DGI',
'D', 'HEI', 'ASUR', 'AVID', 'EPAY', 'CBAK', 'CPSH', 'CYAN', 'DBVT', 'DELT', 'EDGW', 'XELA', 'FALC', 'SVVC', 'FBIO', 'GEOS',
'QQQC', 'GPRO', 'MRVL', 'MZOR', 'BKFS', 'BA', 'CAJ', 'CRY', 'CUB', 'DGI', 'GME', 'GM', 'GNE', 'ASR', 'PAC', 'MDT',
'MTD', 'MIXT', 'MULE', 'NC', 'NPTN', 'NXPI', 'NSTG', 'UEPS']

stock_df = pdr.get_quote_yahoo(stocks)


#s = Options('AAPL')._get_data_in_date_range(date.today())
#print s
stock_df.index.name = "StockSymbol"

stock_df.to_csv("stock.csv")

company_stock = pandas.read_csv("stock.csv")
companies = pandas.read_csv("companies.csv")

merged = company_stock.merge(companies, on = 'StockSymbol')
merged['Amount'] = merged['last']*(merged['NumberofStocks']).astype(float)
merged.columns = map(str.lower, merged.columns)
merged.rename(columns = {'change_pct':'changepct','short_ratio' : 'shortratio'}, inplace = True)
merged.to_csv('new_stock.csv', index=False)
