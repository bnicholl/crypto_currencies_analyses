
def moving_average(price, date, total_bars):
        """when i mo e this to a function, these two vars will be the vars that are returned.
        I'll then want to save these variables in some list so we can check things, like how 
        many times the 5 day moving average drops below the 30 day mmoving average. This 'checker'
        funtion will be a different method inside of this class """
        moving_average_list = []
        corresponding_date = []
        
        stop_iteration = len(price)
        begining_bar = 0
            
        end_bar = total_bars
        
        """if our pips moving average is odd, such as 3 day or 5 hour moving average """
            
        while end_bar < stop_iteration:
            
            moving_average = sum(price[begining_bar:end_bar]) / total_bars
            moving_average_list.append(moving_average)
            corresponding_date.append(date[end_bar])
            
            begining_bar += 1
            end_bar += 1
        
        return moving_average_list, corresponding_date