## Script created by Joseph Armstrong (armstjc@mail.uc.edu
## Latest Script edit: 10/05/2021
##
## Script name: YFinance_scripts.py
## Script use case: Gives the user the ability to run YFinance scripts throughout the entire US stock market

import yfinance as yf
import os 
import pandas as pd
from multiprocessing import Pool
from datetime import timedelta, date
import datetime
import time
from tqdm import tqdm
from fileDirectoryCreation import *
checkFolderIntegrity()

## Defining variables as global variables 
## (can be used without calling this function directly)

stockList = pd.read_csv(fileDirectory + '/Stock_List.csv')
stockListLen = len(stockList)

# Date format = "2021-09-01"
today = date.today()
strToday = str(today)
#print(strToday)
tomorow = today + datetime.timedelta(days=1)
strTomorow = str(tomorow)
#print(strTomorow)
#print(next_monday)

def getTodaysStockHistory(daysOffset):
    '''
    WARNING! TOO UNSTABLE TO USE CONSISTENTLY!! NEEDS MORE TESTING!!!
    Grabs the by-minute history of a stock.

    '''
    d = daysOffset
    print('get ticker data')
    #2021-09-30 = "$Y-%m-%d"
    today = date.today() - datetime.timedelta(days= 1)
    strToday = today.strftime("%Y-%m-%d")

    tomorow = date.today() - datetime.timedelta(days= 0)
    strTomorow = tomorow.strftime("%Y-%m-%d")
    listLen = len(stockList)
    for i in tqdm(stockList.index, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        #print(str(i)+'/'+str(listLen)+' ' + stockList['Symbol'][i])
        try:
            stockTickers = yf.download(stockList['Symbol'][i], start=strToday, end=strTomorow, interval = "1m" )
            stockTickers['ABV'] =  stockList['Symbol'][i]
            stockTickers.to_csv(fileDirectory + '/ByMinuteHistory/'+stockList['Symbol'][i]+'_'+strTomorow+'.csv')
        except:
            pass


def getStockHistory():
    '''

    Runs through a csv file with stock abreviations 
    to download the daily history of every stock in the file.

    By default, this function is looking for a file called 
    'Stock_List.csv', located at the root of the directory 
    you specified with 'fileDirectory', with a column called [Symbol]. 
    
    Without modification, this function will not work on your csv file, 
    unless you have it formatted this way.
   
    '''
    for i in tqdm(stockList.index, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(stockList['Symbol'][i])
            hist = stock.history(period="max")
            hist['ABV'] = stockList['Symbol'][i]
            hist.to_csv(fileDirectory + '/StockHistory/'+stockList['Symbol'][i]+'.csv')
        except:
            pass

def getStockActions(): 
    '''

    Runs through a csv file with stock abreviations 
    to download stock dividends and stock splits for every abreviation in a csv file.

    By default, this function is looking for a file called 
    'Stock_List.csv', located at the root of the directory 
    you specified with 'fileDirectory', with a column called [Symbol]. 
    
    Without modification, this function will not work on your csv file, 
    unless you have it formatted this way.

    '''   
    for i in tqdm(stockList.index, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(stockList['Symbol'][i])
            hist = stock.actions
            hist['ABV'] = stockList['Symbol'][i]
            hist.to_csv(fileDirectory + '/StockEvents/'+stockList['Symbol'][i]+'.csv')
        except:
            pass

def getStockFinancials():
    '''

    Runs through a csv file with stock abreviations 
    to download the basic financial information of every stock 
    abreviation in a csv file.

    By default, this function is looking for a file called 
    'Stock_List.csv', located at the root of the directory 
    you specified with 'fileDirectory', with a column called [Symbol]. 
    
    Without modification, this function will not work on your csv file, 
    unless you have it formatted this way.

    '''
    for i in tqdm(stockList.index, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(stockList['Symbol'][i])
            hist = stock.financials
            df_transposed = hist.transpose()
            df_transposed['ABV'] = stockList['Symbol'][i]
            df_transposed.to_csv(fileDirectory + '/StockFinancials/'+stockList['Symbol'][i]+'.csv')
        except:
            pass

def getStockOptions():
    for i in tqdm(stockList.index, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stockABV = stockList['Symbol'][i]
            stock = yf.Ticker(stockABV)
            options = stock.options
            datalist = list(options)
            listOptions = pd.DataFrame(datalist, columns=['Dates'])
            for s in listOptions.index:
                opt = stock.option_chain(listOptions['Dates'][s])
                optCallsTable = opt.calls
                optCallsTable['ABV'] = stockList['Symbol'][i]
                optCallsTable.to_csv(fileDirectory + '/Options/Calls/'+stockABV+'_'+listOptions['Dates'][s]+'.csv',index=False)
                optPutsTable = opt.puts
                optPutsTable['ABV'] = stockList['Symbol'][i]
                optPutsTable.to_csv(fileDirectory + '/Options/Puts/'+stockABV+'_'+listOptions['Dates'][s]+'.csv',index=False)
        except:
            pass

def getDayStockTicker():
    print('get ticker data')
    #2021-09-30 = "$Y-%m-%d"

    listLen = len(stockList)
    for i in tqdm(stockList.index, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        print('888888888888888888888888888888888888888888888888888888888888888888888888888888888')
        print(str(i)+'/'+str(listLen)+' ' + stockList['Symbol'][i])
        try:
            for d in range(1,29):
            
                today = date.today() - datetime.timedelta(days=d+1)
                strToday = today.strftime("%Y-%m-%d")

                tomorow = date.today() - datetime.timedelta(days=d)
                strTomorow = tomorow.strftime("%Y-%m-%d")
                
                stockTickers = yf.download(stockList['Symbol'][i], start=strToday, end=strTomorow, interval = "1m" )
                stockTickers['ABV'] =  stockList['Symbol'][i]
                stockTickers.to_csv(fileDirectory + '/ByMinuteHistory/'+stockList['Symbol'][i]+'_'+strTomorow+'.csv')
        except:
            pass
        print('888888888888888888888888888888888888888888888888888888888888888888888888888888888')
        
def getMajorHolders():
    print('')
    for i in tqdm(stockList.index, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        
        stock = yf.Ticker(stockList['Symbol'][i])
        stockMajorHolders = stock.major_holders

        try:
            stockInstitutionalHolders['ABV'] = stockList['Symbol'][i]
            stockMajorHolders.to_csv(fileDirectory + '/Holders/Major/'+ stockList['Symbol'][i] + '_major_holders.csv')
        except:
            pass

def getInstitutionalHolders():
    print('show major holders')
    stock = yf.Ticker("MSFT")
    stockInstitutionalHolders = stock.institutional_holders
    #df_transposed = stockMajorHolders.transpose()
    stockInstitutionalHolders['ABV'] = "MSFT" #stockList['Symbol'][i]
    stockInstitutionalHolders.to_csv(fileDirectory + '/Holders/Institutional/'+'MSFT'+'.csv')
    print(stockMajorHolders)


#def mutiThreading():
#    if __name__ == '__main__':
#        if((os.cpu_count()-1)<2):
#            p = Pool(1)
#        else:
#            p = Pool(os.cpu_count()-1)
#        p.map(getStockOptions())
#        p.close()
#        p.join()

######################################################
# WORKING CODE
######################################################



