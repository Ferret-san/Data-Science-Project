import os
import pandas as pd


file_list = []
path = "D:/RobinhoodPopularity/robintrack-popularity-history/tmp/popularity_export"
for file in os.listdir(path):
    if file.endswith('.csv'):
        df = pd.read_csv("D:/RobinhoodPopularity/robintrack-popularity-history/tmp/popularity_export/" + file, parse_dates=['timestamp'])
        df.index = df['timestamp']
        df = df.resample('D').sum()
        df['symbol'] = file.rstrip('.csv')
        df['date'] = df.index
        df.index = df['symbol']
        df.drop(['symbol'], axis=1, inplace = True)
        file_list.append(df)
        print(file)

all_stocks = pd.concat(file_list, ignore_index = False)
all_stocks.to_csv("stock_popularity.csv")