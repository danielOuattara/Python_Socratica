# !bin/bash
# Daniel OUATTARA
# 21 06 2024


""""
CSV: comma separated values.

A popular format for storing data,

CSV is simple and convenient

Python has a CSV module to handle it

To be useful, we need to store the data

1- without CSV module
2- with CSV module

"""

import csv
from datetime import datetime

path = "./20_google_stock_data.csv"

# for item in dir(csv):
#     print(item)


""""
Dialect
DictReader
DictWriter
Error
QUOTE_ALL
QUOTE_MINIMAL
QUOTE_NONE
QUOTE_NONNUMERIC
Sniffer
StringIO
_Dialect
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
__version__
excel
excel_tab
field_size_limit
get_dialect
list_dialects
re
reader
register_dialect
unix_dialect
unregister_dialect
writer
"""


file = open(path, newline='')

# create a reader to parse the data from the file
reader = csv.reader(file)

# the first line is the header use the next() method to extract it
header = next(reader)

# # then read the remaining data
# data = [line for line in reader]
# print(header)
# print(data[0])


# ------------------------------------------

data = []
for row in reader:
    # each data = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']

    date = datetime.strptime(row[0], '%m/%d/%Y')

    # 'open_price' instead of 'open', the name of a built-in func.
    open_price = float(row[1])
    high_price = float(row[2])
    low_price = float(row[3])
    close_price = float(row[4])

    # volume: number of stock traded
    volume = float(row[5])

    #  alternative adjusted closing price
    adj_close = float(row[6])

    data.append([date, open_price, high_price, low_price, close_price, volume])


# for item in data:
#     print(item)

print(data[0])


"""
In finance : 

Stock Return = % change in price

common times frames: 
> Daily
> Weekly
> Monthly
> Quarterly
> Annually
"""


# Compute & Store daily stock returns
return_path = "./20_google_return_data.csv"

file = open(return_path, 'w')

# CSV writer object to store our computed results
writer = csv.writer(file)

writer.writerow(["Date", "Return"])

"""NOTE: data is set as most recent last first"""

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]

    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
