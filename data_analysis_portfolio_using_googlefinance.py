from googlefinance import getQuotes #Google Finance may not be active anymore.
import json
import csv
import pandas

stocks = ['AAPL','GOOGL', 'AMZN', 'FB', 'SSNLF', 'MSFT', 'SNE', 'IBM', 'NTDOY', 'ORCL', 'VMW', 'INTC', 'HPQ', 'DVMT',
'CSCO', 'ADBE', 'SAP', 'LNVGY', 'RHT', 'SYMC', 'TWTR', 'ATNY', 'ACTS', 'ATVI', 'IOTS', 'ADRO', 'AMD', 'ADVS', 'ZBRA', 
'XPLR', 'XBIT', 'WIX', 'WBMD', 'VNOM', 'VIA', 'VECO', 'UPLD', 'UBNT', 'UFPT', 'TYME', 'TRIV', 'TRIP', 'TGA', 'TSI',
'TESS', 'AIR', 'ATEN', 'AQN', 'DDD', 'WUBA', 'ASX', 'A', 'AYX', 'AMBR', 'AEE', 'BHE', 'BIO', 'CPL', 'CTS', 'CMI', 'DGI',
'D', 'HEI', 'ASUR', 'AVID', 'EPAY', 'CBAK', 'CPSH', 'CYAN', 'DBVT', 'DELT', 'EDGW', 'XELA', 'FALC', 'SVVC', 'FBIO', 'GEOS',
'QQQC', 'GPRO', 'MRVL', 'MZOR', 'BKFS', 'BA', 'CAJ', 'CRY', 'CUB', 'DGI', 'GME', 'GM', 'GNE', 'ASR', 'PAC', 'MDT',
'MTD', 'MIXT', 'MULE', 'NC', 'NPTN', 'NXPI', 'NSTG', 'UEPS'] #list of particular tech stocks boutique firm is interested in

stock_json = json.dumps(getQuotes(stocks), indent=2)    #extracts data using Google Finance API and dumps the data in a json file to be further analyzed.
                                                        #uses json to keep the order and serialization of the data in python dictionary.
stock_df = pandas.read_json(stock_json)   #reads the dumped json file.

stock_df.to_csv("stock.csv")  #converts the json file to a comma separated values file

company_stock = pandas.read_csv("stock.csv")  #reads the stock csv file
companies = pandas.read_csv("companies.csv")   #reads a csv file that contains the names, locations and number of stocks the firm invests in. 

merged = company_stock.merge(companies, on = 'StockSymbol')  #merges the companies csv and the stock csv to provide conclusive data

merged.to_csv('portfolio.csv', index=False) #creates a new file that contains the entire portfolio of the company.
