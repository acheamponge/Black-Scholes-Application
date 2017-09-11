import pandas_datareader as pdr
import csv
import pandas
import json

stocks = ['AAPL','GOOGL', 'AMZN', 'FB', 'SSNLF', 'MSFT', 'SNE', 'IBM', 'NTDOY', 'ORCL', 'VMW', 'INTC', 'HPQ', 'DVMT',
'CSCO', 'ADBE', 'SAP', 'LNVGY', 'RHT', 'SYMC', 'TWTR', 'ATNY', 'ACTS', 'ATVI', 'IOTS', 'ADRO', 'AMD', 'ADVS', 'ZBRA',
'XPLR', 'XBIT', 'WIX', 'WBMD', 'VNOM', 'VIA', 'VECO', 'UPLD', 'UBNT', 'UFPT', 'TYME', 'TRIV', 'TRIP', 'TGA', 'TSI',
'TESS', 'AIR', 'ATEN', 'AQN', 'DDD', 'WUBA', 'ASX', 'A', 'AYX', 'AMBR', 'AEE', 'BHE', 'BIO', 'CPL', 'CTS', 'CMI', 'DGI',
'D', 'HEI', 'ASUR', 'AVID', 'EPAY', 'CBAK', 'CPSH', 'CYAN', 'DBVT', 'DELT', 'EDGW', 'XELA', 'FALC', 'SVVC', 'FBIO', 'GEOS',
'QQQC', 'GPRO', 'MRVL', 'MZOR', 'BKFS', 'BA', 'CAJ', 'CRY', 'CUB', 'DGI', 'GME', 'GM', 'GNE', 'ASR', 'PAC', 'MDT',
'MTD', 'MIXT', 'MULE', 'NC', 'NPTN', 'NXPI', 'NSTG', 'UEPS']

stock_df = pdr.get_quote_yahoo(stocks)

stock_df.index.name = "StockSymbol"

stock_df.to_csv("stock.csv")

company_stock = pandas.read_csv("stock.csv")
companies = pandas.read_csv("companies.csv")

merged = company_stock.merge(companies, on = 'StockSymbol')

merged.to_csv('new.csv', index=False)
