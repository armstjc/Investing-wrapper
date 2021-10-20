## Script created by Joseph Armstrong (armstjc@mail.uc.edu)
## Latest Script edit: 10/05/2021
##
## Script name: main.py
## Script use case: Executes python scripts in this package.
##                  If you want a starting point, this is the script.

from fileDirectoryCreation import *
from RefreshStockAbv import *
from YFinance_scripts import *
from congress import *
from coinbase_py import *
from getStockHistory import * 

def main():
    #####################################################
    ##          fileDirectoryCreation Scripts          ##
    #####################################################
    checkFolderIntegrity()
     

    #####################################################
    ##          RefreshStockAbv Scripts                ##
    #####################################################
    getStockAbv()

    #####################################################
    ##          YFinance Scripts                       ##
    #####################################################
    #getTodaysStockHistory(1)
    #getStockHistory()
    #getStockActions()
    #getStockFinancials()
    #getStockOptions()
    #getDayStockTicker()
    #getMajorHolders()
    #getInstitutionalHolders()
    
    #####################################################
    ##          congress Scripts                       ##
    #####################################################
    
    #getHouseTransactions()
    #getSenateTransactions()

    #####################################################
    ##          coinbase_py Scripts                    ##
    #####################################################
    #fetchCoinbaseSymbols()
    #fetchCryptoCurrencies()
    #fetchDailyData(symbol="BTC/USD")

if __name__ == "__main__":
    main()