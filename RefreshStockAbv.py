## Script created by Joseph Armstrong (armstjc@mail.uc.edu
## Latest Script edit: 10/05/2021
##
## Script name: RefreshStockAbv.py
## Script use case: Downloads a list of US stocks for these scripts to use

from urllib.request import urlopen
import pandas as pd

from fileDirectoryCreation import *
checkFolderIntegrity()

def getStockAbv():
    data = {'Symbol':['A']}
    
    url = "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/all/all_tickers.txt"
    file = urlopen(url)
    stockDF = pd.read_csv(file, sep=" ", header=None, names=["Symbol"])
    stockDF.to_csv(fileDirectory + '/Stock_List.csv',index=False)
    print(stockDF)
