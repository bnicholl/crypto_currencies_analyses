import numpy as np





def buy_crossover(first_calculation, second_calculation, sell_back, stop_loss, low_price_for_bar, high_price_for_bar, buy):
    difference_between_calculations = abs(len(first_calculation['prices']) - len(second_calculation['prices']))
    
    
    """our moving averages will have different amount of values in them depending on if its a 3 day or,
    53 day moving average, so we need to make sure the amount of values in each calculation is the same """
    if len(first_calculation['prices']) < len(second_calculation['prices']):
        dates = first_calculation['dates']
        second_calculation_prices = np.array(second_calculation['prices'][difference_between_calculations:])
        first_calculation_prices = np.array(first_calculation['prices'])
        total_length_of_values = len(first_calculation['prices'])
        
        difference_between_calculations_and_candlestick_prices = len(low_price_for_bar) - len(first_calculation['prices'])
        
    elif len(second_calculation['prices']) < len(first_calculation['prices']):
        dates = second_calculation['dates']
        first_calculation_prices = np.array(first_calculation['prices'][difference_between_calculations:])
        second_calculation_prices = np.array(second_calculation['prices'])
        total_length_of_values = len(second_calculation['prices'])
    
        difference_between_calculations_and_candlestick_prices = len(low_price_for_bar) - len(second_calculation['prices'])
    
    
    high_price_for_bar = high_price_for_bar[difference_between_calculations_and_candlestick_prices:]    
    low_price_for_bar = low_price_for_bar[difference_between_calculations_and_candlestick_prices:]
    
    
    initial_buy_date = []
    initial_buy = []
    
    profit_point_date = []
    profit_point = []
    
    stop_loss_date = []
    stop_loss_point = []
    
    our_goal = 'is first_calc_less_than_than_second_calc'
    index = 0    
    while index < total_length_of_values:
        # first calculation need to start off as greater then second calculation to short
        if our_goal == 'is first_calc_less_than_than_second_calc':
            if first_calculation_prices[index] - second_calculation_prices[index] < 0:
                our_goal = 'checking_for_crossover'
                
        
        elif our_goal == 'checking_for_crossover':
            # if true, we have a crossover!!!
            if first_calculation_prices[index] - second_calculation_prices[index] >= 0:             
            
                initial_buy_date.append(dates[index])
                initial_buy.append(second_calculation_prices[index])
                
                do_we_hit_sell_back = second_calculation_prices[index] + sell_back
                do_we_hit_stop_loss = second_calculation_prices[index] + stop_loss
                
                for high_price_point_after_crossover in high_price_for_bar[index:]:
                    if high_price_point_after_crossover >= do_we_hit_sell_back:
                        print(high_price_point_after_crossover)
                        print(do_we_hit_sell_back)
                        profit_point.append(high_price_point_after_crossover)
                        profit_point_date.append(dates[index])
                        our_goal = 'is first_calc_less_than_than_second_calc'
                        break
                        
                    elif low_price_for_bar[index] <= do_we_hit_stop_loss:
                        stop_loss_point.append(low_price_for_bar[index])
                        stop_loss_date.append(dates[index])
                        our_goal = 'checking_for_crossover'
                        break         
                    """adding one to the index right here ensures we do not log in another short while 
                    were currently already shorted a forex pair"""
                    index += 1 
                    
        index += 1
                
        
    return initial_buy, initial_buy_date, profit_point, profit_point_date, stop_loss_point, stop_loss_date
            
    
    
