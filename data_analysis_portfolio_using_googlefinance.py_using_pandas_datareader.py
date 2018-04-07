  GNU nano 2.2.6                                File: csc330.py                                                                       
#Most recent version of python script
import pandas_datareader as pdr #working finance API
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
'MTD', 'MIXT', 'MULE', 'NC', 'NPTN', 'NXPI', 'NSTG', 'UEPS']  #list of particular tech stocks boutique firm is interested in

stock_df = pdr.get_quote_yahoo(stocks)  #extracts data using pandas datareader Finance API and dumps the data to be further analyzed.

stock_df.index.name = "StockSymbol" #changes the first column name to StockSymbol to help with identification.

stock_df.to_csv("stock.csv") #converts the stock_df file to a comma separated values file

company_stock = pandas.read_csv("stock.csv") #reads the stock csv file
companies = pandas.read_csv("companies.csv") #reads a csv file that contains the names, locations and number of stocks the firm invests in. 

merged = company_stock.merge(companies, on = 'StockSymbol') #merges the companies csv and the stock csv to provide conclusive data
merged['Amount'] = merged['last']*(merged['NumberofStocks']).astype(float) #converts elements of the NumberofStocks into floats
merged.columns = map(str.lower, merged.columns) #formats all words into lower case
merged.rename(columns = {'change_pct':'changepct','short_ratio' : 'shortratio'}, inplace = True) #renames change_pct and short_ratio into changepct and shortratio respectively.
merged.to_csv('portfolio.csv', index=False) #exports the analyzed data into a csv file.
