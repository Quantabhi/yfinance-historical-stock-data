import yfinance as yf
import matplotlib.pyplot as plt 
 
'''
In Yahoo Finance, the suffix ".NS" is used for stocks listed on the National 
Stock Exchange of India (NSE).

For example:

TATAMOTORS.NS → Tata Motors on NSE
TATAMOTORS.BO → Tata Motors on BSE (Bombay Stock Exchange)
Since Indian stocks can be listed on both NSE and BSE
you need to specify the exchange using the appropriate suffix:

".NS" → NSE
".BO" → BSE
'''

# use historical date
stock = yf.download("YATRA.BO",start="2024-01-01",end="2025-03-01")

# create plot
close_prices = stock['Close']

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(close_prices)

# Show the plot
plt.show()
