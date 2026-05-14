import yfinance as yf
import pandas as pd
from topdf import convertPDF
from whatsapp_send import whatsapp_sending
from datetime import datetime
import os
pdf = os.path.abspath("stock_info.pdf")


#Grab time
t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#hard code the tickers from source
tickers = ["NVDA", "GOOG", "AAPL", "MSFT", "AMZN", "TSM", "AVGO", "META", "TSLA", "WMT"]

#set up empty list for storing data
data = []

for ticker in tickers: #for loop to get the data
    info = yf.Ticker(ticker).info
    data.append({
    "Ticker":     info.get("symbol"),
    "Name":       info.get("shortName"),
    "Price":      info.get("currentPrice"),
    "Price change percent": info.get("regularMarketChangePercent"),
    "Day low": info.get("dayLow"),
    "Day high": info.get("dayHigh"),
    "Year low": info.get("fiftyTwoWeekLow"),
    "Year high": info.get("fiftyTwoWeekHigh"),
    "Volume": info.get("volume"),
    "Average volume": info.get("averageVolume"),
    "Bid": info.get("bid"),
    "Ask": info.get("ask"),
    "Beta": info.get("beta"),
    "P/E ratio": info.get("trailingPE"),
    "Market cap": info.get("marketCap"),
    "Currency":   info.get("currency"),
    })

df = pd.DataFrame(data)
df1 = df[["Ticker", "Name", "Price", "Price change percent", "Day low", "Day high", "Year low", "Year high"]]
df2 = df[["Ticker", "Volume", "Average volume", "Bid", "Ask", "Beta", "P/E ratio", "Market cap", "Currency"]]
df2["Market cap"] = df2["Market cap"] / 1e12 # Set it as trillion of dollars


convertPDF(df1, df2, t)


whatsapp_sending(pdf, "+852 68720365")