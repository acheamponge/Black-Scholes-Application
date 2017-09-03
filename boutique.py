from googlefinance import getQuotes
import json
import csv
import pandas

stocks = ['AAPL','GOOGL', 'AMZN', 'FB', 'SSNLF', 'MSFT', 'SNE', 'IBM', 'NTDOY', 'ORCL', 'VMW', 'INTC', 'HPQ', 'DVMT',
'CSCO', 'ADBE', 'SAP', 'LNVGY', 'RHT', 'SYMC', 'TWTR', 'ATNY', 'ACTS', 'ATVI', 'IOTS', 'ADRO', 'AMD', 'ADVS', 'ZBRA', 
'XPLR', 'XBIT', 'WIX', 'WBMD', 'VNOM', 'VIA', 'VECO', 'UPLD', 'UBNT', 'UFPT', 'TYME', 'TRIV', 'TRIP', 'TGA', 'TSI',
'TESS', 'AIR', 'ATEN', 'AQN', 'DDD', 'WUBA', 'ASX', 'A', 'AYX', 'AMBR', 'AEE', 'BHE', 'BIO', 'CPL', 'CTS', 'CMI', 'DGI',
'D', 'HEI', 'ASUR', 'AVID', 'EPAY', 'CBAK', 'CPSH', 'CYAN', 'DBVT', 'DELT', 'EDGW', 'XELA', 'FALC', 'SVVC', 'FBIO', 'GEOS',
'QQQC', 'GPRO', 'MRVL', 'MZOR', 'BKFS', 'BA', 'CAJ', 'CRY', 'CUB', 'DGI', 'GME', 'GM', 'GNE', 'ASR', 'PAC', 'MDT',
'MTD', 'MIXT', 'MULE', 'NC', 'NPTN', 'NXPI', 'NSTG', 'UEPS']

stock_json = json.dumps(getQuotes(stocks), indent=2)    

stock_df = pandas.read_json(stock_json)

stock_df.to_csv("stock.csv")

company_stock = pandas.read_csv("stock.csv")
companies = pandas.read_csv("companies.csv")

merged = company_stock.merge(companies, on = 'StockSymbol')

merged.to_csv('new.csv')
