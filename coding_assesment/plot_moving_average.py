#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 6

@author: bennicholl
"""


from moving_average import moving_average
from buy_crossover import buy_crossover
from pull_crypto_from_postgres import pull_crypto_from_postgres
from dashboard import build_dash_microservice

import plotly.graph_objs as go


class get_currency():
    
    
    def __init__(self, crypto_currency):
        
        self.calculations = {}

        self.high_price, self.low_price, self.date = pull_crypto_from_postgres(crypto_currency)
        
        self.plot_currency()     
        
    def plot_currency(self):
        self.data = go.Figure()
        
        self.data.add_trace(go.Candlestick(x=self.date,
                        #open=,
                        high=self.high_price,
                        low=self.low_price,
                        #close=,
                        name = 'candlestick'))
    
    
    def moving_ave(self, total_bars, name, prices = 'low'):
            
            if prices == 'low':
                price = self.low_price
                
            date = self.date
            """call moving_average function """
            moving_average_list, corresponding_date = moving_average(price, date, total_bars)
            
            save_calculations = {name: {'prices' : moving_average_list, 'dates' : corresponding_date }}
            self.calculations.update(save_calculations)
            
            self.plot_function(name = name, x = corresponding_date, y = moving_average_list, mode = 'lines')
            
        
        
                
    def plot_function(self, x, y, name, mode):
        self.data.add_trace(
            go.Scatter(
                x=x,
               y=y,
               name = name,
               mode = mode
            ))
        
        self.addUpdateMenu()
        
    def addUpdateMenu(self):

        self.data.layout.update(
            updatemenus=[
            go.layout.Updatemenu(
                active=0,
                buttons=[
                    dict(label='show everything',
                         method="update",
                         args=[{"visible": [True, True, True, True, True, True]},
                               ]),
    
                    dict(label='moving averages',
                         method="update",
                         args=[{"visible": [True, True, True, False, False, False]},
                               ]),
                   
                ],
            )
        ])
        
        
    
    def buy_crossover(self, calc_name_one, calc_name_two, sell_back, stop_loss, buy = 0):
        first_calculation = self.calculations[calc_name_one]
        second_calculation = self.calculations[calc_name_two]
        buy, buy_date, profit_point, profit_point_date, stop_loss_point, stop_loss_date = buy_crossover(first_calculation, second_calculation, 
                                                                                                        sell_back, stop_loss, self.low_price, self.high_price, buy)
        
        self.plot_function(name = 'purchase', x = buy_date, y = buy, mode = 'markers')
        self.plot_function(name = 'profit', x = profit_point_date, y = profit_point, mode = 'markers')
        self.plot_function(name = 'stop loss', x = stop_loss_date, y = stop_loss_point, mode = 'markers')
    
    
# THESE BELOW CLASS AND METHOD CALLS ARE HOW WE RUN THE CODE    
    
a = get_currency(crypto_currency = 'doge')
a.moving_ave(2, 'moving_ave_1')
a.moving_ave(4, 'moving_ave_2')

a.buy_crossover(calc_name_one = 'moving_ave_1', calc_name_two = 'moving_ave_2', sell_back = 10000, stop_loss = -1000)

plot = build_dash_microservice(a.data)