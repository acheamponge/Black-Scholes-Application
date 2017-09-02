from googlefinance import getQuotes
import json
import csv
import sys
import pandas
stocks = ['AAPL','GOOGL', 'AMZN', 'FB', 'SSNLF', 'MSFT', 'SNE', 'IBM', 'NTDOY', 'ORCL', 'VMW', 'INTC', 'HPQ', 'DVMT',
'CSCO', 'ADBE', 'SAP', 'LNVGY', 'RHT', 'SYMC', 'TWTR']

stock_json = json.dumps(getQuotes(stocks), indent=2)    

#stock_load = json.loads(stock_json)

#output = csv.writer(sys.stdout)

#output.writerow(stock_load[0].keys())

#for row in stock_load:
    #output.writerow(row.values())
df = pandas.read_json(stock_json)

df.to_csv("stock.csv")
