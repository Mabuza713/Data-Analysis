import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


class MomentumStrat:
    def __init__(self, stockName, start = "2020-01-01", end = "2024-06-12"):
        self.stockName = stockName
        self.start = start
        self.end = end

    
    def GetData(self):
        # Download and prepared dataframe
        data = yf.download(self.stockName, self.start, self.end)
        data["Day"] = np.arange(1, len(data) + 1)
        data.drop(columns = ["Adj Close", "Volume"], inplace = True)
        data = data[["Day", "Open", "High", "Low", "Close"]]
        return data
    

    def MomentumStrat(self):
        data = self.GetData()

        # Creating new columns containing two "sliders"? when fast > slow we buy calls 
        # when fast < slow we buy puts as simple as that not a financial advice tho.
        data["9 Days fast"] = data["Close"].rolling(9).mean().shift()
        data["21 Days slow"] = data["Close"].rolling(21).mean().shift()
        data = data.dropna()

        # Adding signal column
        data["Signal"] = np.where(data["9 Days fast"] > data["21 Days slow"], 1, 0) # long singal
        data["Signal"] = np.where(data["9 Days fast"] < data["21 Days slow"], -1, data["Signal"]) # short signal

        # Adding return column
        data["Return"] = np.log(data["Close"]).diff()
        data["Sys return"] = data["Signal"] * data["Return"]
 
        # Add direction
        data["Entry"] = data.Signal.diff()

        # Plotting our data
        plt.plot(data.iloc[-120:]["Close"], label = f"{self.stockName}")
        plt.plot(data.iloc[-120:]["9 Days fast"], label = "9 days fast")
        plt.plot(data.iloc[-120:]["21 Days slow"], label = "21 days slow")

        # Plotting an entry points
        plt.plot(data[-120:].loc[data.Entry == 2].index, data[-120:]["9 Days fast"][data.Entry == 2], "^", color = "g", markersize = 12)
        plt.plot(data[-120:].loc[data.Entry == -2].index, data[-120:]["21 Days slow"][data.Entry == -2], "v", color = "r", markersize = 12)


        plt.title("Momentum Strategy")
        plt.ylabel("Stock price")
        plt.xlabel("Date")
        plt.legend(loc = 2)
        plt.show()
result = MomentumStrat("PFE")
result.MomentumStrat()

#EVE look out
#MESA
#T
#AAPL