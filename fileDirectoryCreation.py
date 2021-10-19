## Script created by Joseph Armstrong (armstjc@mail.uc.edu
## Latest Script edit: 10/05/2021
##
## Script name: fileDirectoryCreation.py
## Script use case: Creates the default directories for the user to use in these python scripts

import os



##########################################
##              WARNING!                ##
##########################################
## When inputting a file extension in   ##
## Windows, DO NOT USE '\'!! This       ##
## character has a seperate use in      ##
## Python!!                             ##
##########################################

global fileDirectory

fileDirectory = 'D:/Stocks'

def checkFolderIntegrity():
    '''
    If you haven't created the directories to save your data in, use this function to create the directories. 
    Uses the global variable fileDirectory in fileDirectoryCreation.py to create directories to effiently save your data.
    Please make sure you change fileDirectory to a place you want these scripts to save your data to.
    '''
    # Checks to make sure the folders used for saving CSV's 
    # are already there.
    global fileDirectory
    fileDirectory = 'D:/Stocks'
    try:
        os.mkdir(fileDirectory+'/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/StockHistory/')
    except:
        pass
    
    try:
        os.mkdir(fileDirectory + '/StockEvents/')
    except:
        pass
    
    try:
        os.mkdir(fileDirectory + '/StockFinancials/')
    except:
        pass
    
    try:
        os.mkdir(fileDirectory + '/Options/')
    except:
        pass
    
    try:
        os.mkdir(fileDirectory + '/Options/Calls/')
    except:
        pass
    
    try:
        os.mkdir(fileDirectory + '/Options/Puts/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/ByMinuteHistory/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Holders/Major/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Holders/Institutional/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/Annual/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/Quarterly/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/BalanceSheet/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/BalanceSheet/Annual/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/BalanceSheet/Quarterly/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/Annual/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Financials/Quarterly/')
    except:
        pass

    try:
        os.mkdir(fileDirectory + '/Crypto/')
    except:
        pass