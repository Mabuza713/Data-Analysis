import pandas as pd
import pandas_ta as ta
import yfinance as yf
import plotly.graph_objects as go
import numpy as np


class PriceBreakOut:
    def __init__(self, stockName, start = "2024-06-07", end = "2024-06-13"):
        self.stockName = stockName
        self.start = start
        self.end = end

    
    def GetData(self):
        # Download and prepared dataframe
        data = yf.download(self.stockName, self.start, self.end, interval="1m")
        data = data[data["Volume"] != 0]
        
        data["Day"] = np.arange(1, len(data) + 1)
        data.drop(columns = ["Adj Close", "Volume"], inplace = True)
        data = data[["Day", "Open", "High", "Low", "Close"]]
        data["EMA"] = ta.ema(data.Close , length= 150)
        
        
        return data
    
    def TrendDetection(self, prevCandelsAmount):
        data = self.GetData()
        EMAsignal = [0]*len(data)
        for row in range(prevCandelsAmount, len(data)):
            up = 0
            down = 0
            for i in range(row - prevCandelsAmount, row + 1):
                if max(data.Open[i], data.Close[i]) >= data.EMA[i]:
                    up = 1
                elif min(data.Open[i], data.Close[i]) <= data.EMA[i]:
                    down = 1
            if up == 0 and down == 0:
                EMAsignal[row] = 0
            elif up == 1:
                EMAsignal[row] = 1
            elif down == 1:
                EMAsignal = -1
        data["EMAsignal"] = EMAsignal

        print(data)

    def PivitPointDetect(self, candle, window):
        #func that determins if candle is a pivit point 
        data = self.GetData()
        if candle - window < 0 or candle + window >= len(data):
            return 0
        
        high = 1
        low = -1
        for i in range(candle - window, candle + window + 1):
            if data.iloc[candle].Low > data.iloc[i].Low:
                low = 0
            if data.iloc[candle].High < data.iloc[i].High:
                high = 0
        if (high == 0 and low == 0):
            return 0
        if high == 1:
            return high
        if low == -1:
            return low
        else:
            return 0
    def CreatePoint(self, point):
        if point["isPivot"] == -1:
            return point["Low"] + 1e-3
        elif point["isPivot"] == 1:
            return point["High"] + 1e-3
        return np.NaN
    
    def PlotVal(self): #To plot candle plots its easier to use go
        data = self.GetData()
        fig = go.Figure(data = [go.Candlestick(x = data["Day"], open = data["Open"], high = data["High"], low = data["Low"], close = data["Close"])])

        #create indicators of pivit points
        data["isPivot"] = data.apply(lambda row: self.PivitPointDetect(int(row["Day"]), 10),axis = 1)
        data["Point"] = data.apply(lambda row: self.CreatePoint(point = row), axis = 1)

        fig.add_scatter(x = data["Day"], y = data["Point"], mode = "markers", marker = dict(size = 6, color = "green"), name = "pivot")
        fig.update_layout(xaxis_rangeslider_visible = False)
        fig.show()

     




result = PriceBreakOut("O")

result.PlotVal()
    




