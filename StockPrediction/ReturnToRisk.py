import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import yfinance as yf


class ReturnToRisk:
    def __init__(self, stocksName, start, end):
        self.stocksName = stocksName
        self.start = start
        self.end = end
        self.data = None
        
        
    def GetData(self):
        # Downloading the data
        self.data = yf.download(self.stocksName, start= self.start, end = self.end)
        
        # Creating a new CSV file 
        self.data.to_csv("StockData.csv")
        csvRead = pd.read_csv("StockData.csv", header = [0,1], index_col = [0], parse_dates= [0])
        
        # Getting only the Close column from dataframe
        csvClose = csvRead.loc[:,"Close"].copy()
        
        return csvRead, csvClose
        
        
    def PlottingData(self):
        data, dataClose = self.GetData()
        
        # Serializing data
        dataCloseNorm = dataClose.div(dataClose.iloc[0])
        
        # Ploting normalized data
        dataCloseNorm.plot(figsize=(10,10),fontsize= 10)
        plt.grid(axis = "both")
        plt.show()
    
    def CalculatingRiskToReturn(self):
        data, dataClose = self.GetData()
        
        # Getting percentage change between two values 
        dataClosePct = dataClose.pct_change().dropna()
        dataCloseNorm = dataClose.div(dataClose.iloc[0])
        closeStdMean = dataCloseNorm.describe().T.loc[:,["mean", "std"]]
        print(closeStdMean)
        # Getting annual data
        closeStdMean["mean"] = closeStdMean['mean'] 
        closeStdMean["std"] = closeStdMean['std'] 

        # Plotting data
        closeStdMean.plot.scatter(x = "std", y = "mean", figsize = (10, 10), s= 50, fontsize = 12)
        for compName in closeStdMean.index:
            plt.annotate(compName, xy = (closeStdMean.loc[compName, 'std'] + 0.005, closeStdMean.loc[compName, 'mean'] + 0.005),size = 15)
        
        plt.grid(axis="both")
        plt.show()

stocksName = ["PFE", "NIO"]

result = ReturnToRisk(stocksName, start = "2020-06-07", end = "2024-06-07")
result.PlottingData()
result.CalculatingRiskToReturn()