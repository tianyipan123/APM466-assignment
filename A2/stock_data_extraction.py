import yfinance as yf

df = yf.download('AC.TO')["Close"]

df.to_csv("./AC-price.csv")