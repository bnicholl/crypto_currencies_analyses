#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 6

@author: bennicholl
"""

import psycopg2
import pandas as pd

def pull_crypto_from_postgres(crypto_currency):
    
    con = psycopg2.connect(database="postgres", user="postgres", password="***", host="***", port="5432")
    
    data = pd.read_sql_query("SELECT * FROM {}".format(crypto_currency), con)   
    time_period_start = data['time_period_start'].tolist()
    price_high = data['price_high'].tolist()
    price_low = data['price_low'].tolist()

    con.close()
    
    return price_high, price_low, time_period_start

#example pull
#btc_pull = pull_crypto_from_postgres('btc')
