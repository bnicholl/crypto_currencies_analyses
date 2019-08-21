#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:37:22 2019

@author: bennicholl
"""
import pandas as pd
import requests
from sqlalchemy import create_engine

def historical_data(symbol):

    url = 'https://rest.coinapi.io/v1/ohlcv/{}/USD/history?period_id=5DAY&time_start=2018-08-05T00:00:00'.format(symbol)
    headers = {'X-CoinAPI-Key' : 'A72D9280-4CE1-4F97-A824-6DEB066D7BE5'}
    response = requests.get(url, headers=headers).json()
    
    values = []
    for time_period in response:
        values.append([time_period['time_period_start'], time_period['time_period_end'], time_period['price_high'], time_period['price_low']])
    
    
    dataframe = pd.DataFrame(values, columns = ['time_period_start', 'time_period_end', 'price_high', 'price_low'])  
    dataframe['time_period_start'] = pd.to_datetime(dataframe['time_period_start']).dt.strftime('%Y/%m/%d')
    dataframe['time_period_end'] = pd.to_datetime(dataframe['time_period_end']).dt.strftime('%Y/%m/%d')
    
    return dataframe


"""below function calls get the crypto data from the API and puts it into a pandas DF """
#btc = historical_data('BTC')
#eth = historical_data('ETH')
#xrp = historical_data('XRP')
#doge = historical_data('DOGE')



def post_to_postgres(df, name):
    engine = create_engine('***')
    """creates the table in postgres, then puts the respective pandas dataframe into that table """
    df.to_sql(name, engine)

"""below function calls puts data into postgres dataframe running on AWS server """
#post_btc = post_to_postgres(btc, 'btc')
#post_eth = post_to_postgres(eth, 'eth')
#post_xrp = post_to_postgres(xrp, 'xrp')
#post_doge = post_to_postgres(doge, 'doge')





