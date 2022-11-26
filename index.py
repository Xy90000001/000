print('...000...')

import alpaca_trade_api as tradeapi
# from alpaca_trade_api import TimeFrame
from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd
import os

# API Info for fetching data, portfolio, etc. from Alpaca
BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = "PKT4SCGG9HB02E5VFTVW"
ALPACA_SECRET_KEY = "pDluLKOnSTlqP58JCSNVxtfXAX8uPJayHB7buwEf"

# Instantiate REST API Connection
api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=BASE_URL, api_version='v1')
acc = api.get_account()

from datetime import datetime, timedelta
import math
import time

SYMBOL = 'BTCUSD'
# SYMBOL = 'XMRUSD'
SMA_FAST = 12
SMA_SLOW = 24
# QTY_PER_TRADE = 1
power, status = acc.buying_power, acc.status #acc.currency,
# equity =acc.equity
portfolio = api.list_positions()
# if portfolio ==
# coinrol = portfolio[:]  #TK mul coin latr
# print(coinrol)
# print(p.qty)
qty2buy = 100
# qty2sel = coinrol.qty #notional


# clock = api.get_clock()
# if clock.is_open:
#     print('Market is open')
# else:
#     print('Market is closed')


# active_assets = api.list_assets(status='active')
# print(active_assets[0])

# Description is given in the article
def get_pause():
    now = datetime.now()
    next_min = now.replace(second=0, microsecond=0) + timedelta(minutes=1)
    pause = math.ceil((next_min - now).seconds)
    print(f"Sleep for {pause}")
    return pause

# Same as the function in the random version
def get_position(symbol):
    positions = api.list_positions()
    for p in positions:
        if p.symbol == symbol:
            return float(p.qty)
    return 0


# Returns a series with the moving average
def get_sma(series, periods):
    return series.rolling(periods).mean()

# Checks whether we should buy (fast ma > slow ma)
def get_signal(fast, slow):
    print(f"Fast {fast[-1]}  /  Slow: {slow[-1]}")
    return fast[-1] > slow[-1]

# Get up-to-date 1 minute data from Alpaca and add the moving averages
def get_bars(symbol):
    bars = api.get_crypto_bars(symbol, TimeFrame.Minute).df
    bars = bars[bars.exchange == 'CBSE']
    bars[f'sma_fast'] = get_sma(bars.close, SMA_FAST)
    bars[f'sma_slow'] = get_sma(bars.close, SMA_SLOW)
    return bars

# help(api.submit_order)
##web

from flask import Flask, render_template, request
# import subprocess
# rep = 0
# globalize(rep)
# rep = 0
# global rep
lstr =[]
li='dududuDuuuhh'
app = Flask(__name__)

@app.route('/')
def home():
  return 'duh ...!'+str(li)+str(lstr)

# @app.route('/', methods=['GET','POST'])
# def my_form_post() -> 'html':
#     if flask.request.method == 'GET':
#         # redirect('/in')
#         return 'duh'+str(lstr)

#     elif flask.request.method == 'POST':
#         # var = request.form['variable']
#         # return render_template('form.html', value=output)
#         return 'duh!.......'+str(lstr)

# app.run(debug=True)

def mainloop():
    rep = 0
    while True:
        # app.run(debug=True)
        # @app.route('/')#, methods=['GET','POST'])
        # def my_form_post():
        #     return 'duh'
        print('startloo')
        rep = rep+1
        print('rep:  ',rep)
                # GET DATA
        bars = get_bars(symbol=SYMBOL)
                # CHECK POSITIONS
        position = get_position(symbol=SYMBOL)
        should_buy = get_signal(bars.sma_fast,bars.sma_slow)
        print(f"Position: {position} / Should Buy: {should_buy}")

        if position == 0 and should_buy == True:
            # WE BUY ONE BITCOIN
            # api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='buy')
            try:
                api.submit_order(symbol=SYMBOL, notional=qty2buy, side='buy', type='market', time_in_force='gtc')#day, gtc, opg, cls, ioc, fok
                print(f'Symbol: {SYMBOL} / Side: BUY / Quantity: {qty2buy} ')
            except:
                print('insufficient fund')
            # return 'symbol; '
        elif position > 0 and should_buy == False:
            # WE SELL ONE BITCOIN
            try:
                api.submit_order(SYMBOL, qty=get_position(SYMBOL), side='sell',time_in_force='gtc' )
                print(f'Symbol: {SYMBOL} / Side: SELL / Quantity: {get_position(SYMBOL)}')
            except:
                print('insufficient')



        time.sleep(get_pause())
        print("*"*20)
        print('endloop')
    # @app.route('/')#, methods=['GET','POST'])
    # def my_form_post():
    #     return 'duh'#print("*"*20)
        lstr.clear()
        lstr.append(f'Symbol: {SYMBOL} / Side: SELL / Quantity: {get_position(SYMBOL)}, sell: {qty2buy},\n{portfolio} ')
    return lstr #, f'Symbol: {SYMBOL} / Side: BUY / Quantity: {QTY_PER_TRADE}'

def web():
    app.run(debug=True)#, Port = int(os.environ.get("PORT", 8008)), host='0.0.0.0' )    

# r = 0
# while True:
#     r+=1
#     print('asdf',r)
#     app.run(debug=True)
#     print('qwerty')

# web()

# import threading
if __name__ == "__main__":
  mainloop()
#   web()
#     x = threading.Thread(target=mainloop)#, args=(a,))
#    # threads.append(x)
#     x.start()
#     time.sleep(1)
# app.run(debug=True)


# web()

# # Fetch Account
# account = api.get_account()

# # Print Account Details
# print(account.id, account.status)# account.equity)

# #graph
# import matplotlib.pyplot as plt
# from alpaca_trade_api.rest import REST, TimeFrame

# # Fetch Apple data from last 100 days
# # APPLE_DATA = api.get_bars('AAPL', 'day', limit=100).df
# # APPLE_DATA = api.get_bars('AAPL', limit=100).df
# APPLE_DATA = api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df
# print(APPLE_DATA, 'asdf')

# # Reformat data (drop multiindex, rename columns, reset index)
# APPLE_DATA.columns = APPLE_DATA.columns.to_flat_index()
# APPLE_DATA.columns = [x[1] for x in APPLE_DATA.columns]
# APPLE_DATA.reset_index(inplace=True)
# print(APPLE_DATA.head())

# # Plot stock price data
# # plot = APPLE_DATA.plot(x="timestamp", y="r", legend=False)
# # plot.set_xlabel("Date")
# # plot.set_ylabel("Apple Close Price ($)")
# # plt.show()


# #trade
# api.submit_order(symbol='AAPL', qty=1, side='buy', type='market', time_in_force='day')
# help(api.submit_order)
# # api.submit_order('TSLA', notational=100, 'buy', 'market', 'day')
# api.submit_order(symbol='TSLA', notional=100, side='buy', type='market', time_in_force='day')

# # Get stock position for Apple
# # try:
# aapl_position = api.get_position('AAPL')
# print(aapl_position)
# # except: print('noapplesfoyu2day')



# print('.........................')
