import pandas_datareader as web

df = web.DataReader('BTCUSD=X', 'yahoo')
df.to_csv('btc_usd.csv', mode='w', header=True)
