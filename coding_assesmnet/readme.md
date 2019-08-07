# What we are implimenting. 
We are implimenting a simple moving average crossover. When our smaller moving average goes passed our larger moving average, that indicates we should buy. Below will describe what each function is doing, and how the algorihtm works. 

# setup virtual enviroment, install dependencies, and run algorithm (instructions are for Mac OS)

Install virtualenv by running command:   pip install virtualenv

1. download coding_assignment folder, then CD into coding_assignment folder
2. run from the command line:   virtualenv coding_assignment
 3. From command line, run:   source coding_assignment/bin/activate 
 4. from command line run:   pip install -r requirements.txt
 5. from command line run:    python plot_moving_average.py
 6. The dahsboard should be running on localhost 8050. The terminal should state where it is running.
 7. If you'd like, go down to line 104 and change the crypto currency being analyzed. The arguments include:   'btc', 'eth', 'xrp', 'doge'
 8. You can also change the moving average values in line 105 and 106 for their respective moving averages.
 9. The sell back and stop loss parameters in the buy_crossover are the prices we sell our curreny back. For exmaple, if sell_back is set at 10,000, we sell that currency back at the price we bought the currency + 10,000 dollars. If our stop loss is -1,000, we sell the currency back at the price we bought our currency - 1,000 dollars. 

# What our functions are doing
1. When the function pull_crypto_into_postgres is ran, it pulls data from the crypto coinAPI, and puts it into a postgres database, which is hosted on AWS RDS. The post_to_postgres function inside this script is meant create a postgres table from a pandas dataframe. So this function should only be ran for the intial posting of data, so don't try and run it again. 

2. The next python script that is called is plot_moving_average. The first thing this script does is call the pull_crypto_from_postgres script to grab the crypto data that is hosted on the AWS postgres database. 
    
3.  Next, this script calculates moving averages, which is what the moving_ave method is doing. The moving_ave method calls the moving_average script to perform this operation. The total_bars argument is the varaible that tells the method how many bars the moving average should be. For example, total_bars = 3 for daily data would calculate a 3 day moving average. 
    
4. We call moving_ave method twice, then call the buy_crossover method, which buys a currency when our shorter moving average crosses over our longer moving average. The buy_crossover method calls the buy_crossover script to perform this operation. Our sell_back and stop_loss arguments under the buy_crossover method tell our algorithm when to buy or sell, given the exact moment our moving averages cross over. This script then calls the dashboard script, which sets up the dashboard showing the moving averages, and the purchase dates, and the profits and stop loss dates

5. To change the parameters and run the code, simply go down to line 103, which is where the class and method calls are, and play around with the parameters.
    
    
