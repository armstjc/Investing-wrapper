## Script created by Joseph Armstrong (armstjc@mail.uc.edu
## Latest Script edit: 10/05/2021
##
## Script name: YFinance_scripts.py
## Script use case: Gives the user the ability to run YFinance scripts throughout the entire US stock market

import yfinance as yf
import os 
import os.path
import pandas as pd
from multiprocessing import Pool
from datetime import timedelta, date
import datetime
import time
from tqdm import tqdm
from fileDirectoryCreation import *
import glob
from ta.momentum import *
from ta.volume import *
from ta.volatility import *
from ta.trend import * 
from ta.others import *
from ta.utils import dropna
import threading
import json

checkFolderIntegrity()

## Defining variables as global variables 
## (can be used without calling this function directly)
global stockList
if(os.path.exists(fileDirectory + '/Stock_List.csv') != True):
    f = open(fileDirectory + "/Stock_List.csv", "a")
    f.close()

else:
    pass

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
    print('Getting today''s stock history.')
    d = daysOffset
    print('get ticker data')
    #2021-09-30 = "$Y-%m-%d"
    today = date.today() - datetime.timedelta(days= 1)
    strToday = today.strftime("%Y-%m-%d")

    tomorow = date.today() - datetime.timedelta(days= 0)
    strTomorow = tomorow.strftime("%Y-%m-%d")
    listLen = len(stockList)
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        #print(str(i)+'/'+str(listLen)+' ' + stockList['Symbol'][i])
        try:
            stockTickers = yf.download(i, start=strToday, end=strTomorow, interval = "1m" )
            stockTickers['ABV'] =  i
            stockTickers.to_csv(fileDirectory + '/ByMinuteHistory/'+i+'_'+strTomorow+'.csv')
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
    print('Getting the full history of the stock market.')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(i)
            hist = stock.history(period="max")
            hist.to_csv(fileDirectory + '/StockHistory/'+i+'.csv')
        except:
            pass

def getStockHistoryWithIndicators():
    '''

    Runs through a csv file with stock abreviations 
    to download the daily history of every stock in the file.

    By default, this function is looking for a file called 
    'Stock_List.csv', located at the root of the directory 
    you specified with 'fileDirectory', with a column called [Symbol]. 
    
    Without modification, this function will not work on your csv file, 
    unless you have it formatted this way.

    This Function will run slower than getStockHistory(), 
    because it will calculate indicators as well as grab the stock History.
   
    '''
    print('Getting the full history of the stock market.')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(i)
            hist = stock.history(period="max")
            Momentum_AOI = AwesomeOscillatorIndicator(high=hist.High, low=hist.Low)
            hist['AOI'] = Momentum_AOI.awesome_oscillator()

            Momentum_KARMA = KAMAIndicator(close=hist.Close)
            hist['KAMA'] = Momentum_KARMA.kama()

            Momentum_PPO = PercentagePriceOscillator(close=hist.Close)
            hist['PPO'] = Momentum_PPO.ppo()
            hist['PPO_Histogram'] = Momentum_PPO.ppo_hist()
            hist['PPO_Signal'] = Momentum_PPO.ppo_hist()

            Momentum_PVO = PercentageVolumeOscillator(volume=hist.Volume)
            hist['PVO'] = Momentum_PVO.pvo()
            hist['PVO_Histogram'] = Momentum_PVO.pvo_hist()
            hist['PVO_Signal'] = Momentum_PVO.pvo_signal()

            Momentum_RSI = RSIIndicator(close=hist.Close,window=14)
            hist['RSI'] = Momentum_RSI.rsi()

            Momentum_StochasticOscillator = StochasticOscillator(hist.High, hist.Low, hist.Close)
            hist['Stochastic Oscillator'] = Momentum_StochasticOscillator.stoch()
            hist['Stochastic Oscillator_Signial'] = Momentum_StochasticOscillator.stoch_signal()

            Momentum_UltimateOscillator = UltimateOscillator(high=hist.High, low=hist.Low, close=hist.Close)
            hist['Ultimate Oscillator'] = Momentum_UltimateOscillator.ultimate_oscillator()

            Momentum_Williams_R = WilliamsRIndicator(high=hist.High,low=hist.Low,close=hist.Close)
            hist['Williams %R'] = Momentum_Williams_R.williams_r()

            Volume_ADI = AccDistIndexIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
            hist['ADI'] = Volume_ADI.acc_dist_index()

            Volume_CMF = ChaikinMoneyFlowIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
            hist['CMF'] = Volume_CMF.chaikin_money_flow()

            Volume_FI = ForceIndexIndicator(close=hist.Close,volume=hist.Volume)
            hist['FI'] = Volume_FI.force_index()

            Volume_MFI = MFIIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
            hist['MFI'] = Volume_MFI.money_flow_index()

            Volume_VWAP = VolumeWeightedAveragePrice(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
            hist['VWAP'] = Volume_VWAP.volume_weighted_average_price()

            Volitility_Bollinger = BollingerBands(close=hist.Close)
            hist['Bollinger High Band'] = Volitility_Bollinger.bollinger_hband()
            hist['Bollinger High Band Indicator'] = Volitility_Bollinger.bollinger_hband_indicator()
            hist['Bollinger Low Band'] = Volitility_Bollinger.bollinger_lband()
            hist['Bollinger Low Band Indicator'] = Volitility_Bollinger.bollinger_lband_indicator()
            hist['Bollinger Middle Band'] = Volitility_Bollinger.bollinger_mavg()
            hist['Bollinger Percetage Band'] = Volitility_Bollinger.bollinger_pband()
            hist['Bollinger Band Width'] = Volitility_Bollinger.bollinger_wband()

            Volitility_Donchian = DonchianChannel(high=hist.High,low=hist.Low,close=hist.Close)
            hist['Donchian Channel High Band'] = Volitility_Donchian.donchian_channel_hband()
            hist['Donchian Channel Low Band'] = Volitility_Donchian.donchian_channel_lband()
            hist['Donchian Channel Middle Band'] = Volitility_Donchian.donchian_channel_mband()
            hist['Donchian Channel Percentage Band'] = Volitility_Donchian.donchian_channel_pband()
            hist['Donchian Channel Band Width'] = Volitility_Donchian.donchian_channel_wband()

            Volatility_Keltner = KeltnerChannel(high=hist.High,low=hist.Low,close=hist.Close)
            hist['Keltner Channel High Band'] = Volatility_Keltner.keltner_channel_hband()
            hist['Keltner Channel Indicator Crossing High Band'] = Volatility_Keltner.keltner_channel_hband_indicator()
            hist['Keltner Channel Low Band'] = Volatility_Keltner.keltner_channel_lband()
            hist['Keltner Channel Indicator Crossing Low Band'] = Volatility_Keltner.keltner_channel_lband_indicator()
            hist['Keltner Channel Middle Band'] = Volatility_Keltner.keltner_channel_mband()
            hist['Keltner Channel Percentage Band'] = Volatility_Keltner.keltner_channel_pband()
            hist['Keltner Channel Band Width'] = Volatility_Keltner.keltner_channel_wband()

            Volatility_Ulcer = UlcerIndex(close=hist.Close)
            hist['Ulcer Index'] = Volatility_Ulcer.ulcer_index()

            Volatility_ATR = average_true_range(high=hist.High,low=hist.Low,close=hist.Close)
            hist['ATR'] = Volatility_ATR

            Trend_Aroon = AroonIndicator(close=hist.Close)
            hist['Aroon Down Channel'] = Trend_Aroon.aroon_down()
            hist['Aroon Indicator'] = Trend_Aroon.aroon_indicator()
            hist['Aroon Up Channel'] = Trend_Aroon.aroon_up()

            Trend_CCI = CCIIndicator(high=hist.High,low=hist.Low,close=hist.Close)
            hist['CCI'] = Trend_CCI.cci()

            Trend_DPO = DPOIndicator(close=hist.Close)
            hist['DPO'] = Trend_DPO.dpo()

            Trend_EMA = EMAIndicator(close=hist.Close)
            hist['EMA'] = Trend_EMA.ema_indicator()

            Trend_Ichimoku = IchimokuIndicator(high=hist.High,low=hist.Low)
            hist['Ichimoku Senkou Span A'] = Trend_Ichimoku.ichimoku_a()
            hist['Ichimoku Senkou Span B'] = Trend_Ichimoku.ichimoku_b()
            hist['Ichimoku Kujun-sen'] = Trend_Ichimoku.ichimoku_base_line()
            hist['Ichimoku Tenkan-Sen'] = Trend_Ichimoku.ichimoku_conversion_line()

            Trend_KST = KSTIndicator(close=hist.Close)
            hist['KST'] = Trend_KST.kst()
            hist['Diff KST'] = Trend_KST.kst_diff()
            hist['Signal Line KST'] = Trend_KST.kst_sig()

            Trend_MACD = MACD(close=hist.Close)
            hist['MACD Line'] = Trend_MACD.macd()
            hist['MACD Histogram'] = Trend_MACD.macd_diff()
            hist['MACD Signal Line'] = Trend_MACD.macd_signal()

            Trend_MI = MassIndex(high=hist.High,low=hist.Low)
            hist['Mass Index'] = Trend_MI.mass_index()

            Trend_PSAR = PSARIndicator(high=hist.High,low=hist.Low,close=hist.Close)
            hist['PSAR'] = Trend_PSAR.psar()
            hist['PSAR Down'] = Trend_PSAR.psar_down()
            hist['PSAR Down Indicator'] = Trend_PSAR.psar_down_indicator()
            hist['PSAR Up'] = Trend_PSAR.psar_up()
            hist['PSAR Up Indicator'] = Trend_PSAR.psar_up_indicator()

            Trend_STC = STCIndicator(close=hist.Close)
            hist['STC'] = Trend_STC.stc()

            Trend_TRIX = TRIXIndicator(close=hist.Close)
            hist['TRIX'] = Trend_TRIX.trix()

            Trend_Vortex = VortexIndicator(high=hist.High,low=hist.Low,close=hist.Close)
            hist['VI'] = Trend_Vortex.vortex_indicator_diff()
            hist['VI-'] = Trend_Vortex.vortex_indicator_neg()
            hist['VI+'] = Trend_Vortex.vortex_indicator_pos()

            Trend_WMA = WMAIndicator(close=hist.Close)
            hist['WMA'] = Trend_WMA.wma()

            Other_CR = CumulativeReturnIndicator(close=hist.Close)
            hist['CR'] = Other_CR.cumulative_return()

            Other_DLR = DailyLogReturnIndicator(close=hist.Close)
            hist['DLR'] = Other_DLR.daily_log_return()

            Other_DR = DailyReturnIndicator(close=hist.Close)
            hist['DR'] = Other_DR.daily_return()

            hist.to_csv(fileDirectory + '/StockHistory/'+i+'.csv')
        except:
            pass

def CalculateStockIndicators():
    '''

    Runs through a csv file with stock abreviations 
    to download the daily history of every stock in the file.

    By default, this function is looking for a file called 
    'Stock_List.csv', located at the root of the directory 
    you specified with 'fileDirectory', with a column called [Symbol]. 
    
    Without modification, this function will not work on your csv file, 
    unless you have it formatted this way.

    This Function will run slower than getStockHistory(), 
    because it will calculate indicators as well as grab the stock History.
   
    '''
    print('Getting the full history of the stock market.')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = i
            hist = pd.read_csv(fileDirectory+'/StockHistory/'+ i +'.csv')
            Momentum_AOI = AwesomeOscillatorIndicator(high=hist.High, low=hist.Low)
            hist['AOI'] = Momentum_AOI.awesome_oscillator()

            Momentum_KARMA = KAMAIndicator(close=hist.Close)
            hist['KAMA'] = Momentum_KARMA.kama()

            Momentum_PPO = PercentagePriceOscillator(close=hist.Close)
            hist['PPO'] = Momentum_PPO.ppo()
            hist['PPO_Histogram'] = Momentum_PPO.ppo_hist()
            hist['PPO_Signal'] = Momentum_PPO.ppo_hist()

            Momentum_PVO = PercentageVolumeOscillator(volume=hist.Volume)
            hist['PVO'] = Momentum_PVO.pvo()
            hist['PVO_Histogram'] = Momentum_PVO.pvo_hist()
            hist['PVO_Signal'] = Momentum_PVO.pvo_signal()

            Momentum_RSI = RSIIndicator(close=hist.Close,window=14)
            hist['RSI'] = Momentum_RSI.rsi()

            Momentum_StochasticOscillator = StochasticOscillator(hist.High, hist.Low, hist.Close)
            hist['Stochastic Oscillator'] = Momentum_StochasticOscillator.stoch()
            hist['Stochastic Oscillator_Signial'] = Momentum_StochasticOscillator.stoch_signal()

            Momentum_UltimateOscillator = UltimateOscillator(high=hist.High, low=hist.Low, close=hist.Close)
            hist['Ultimate Oscillator'] = Momentum_UltimateOscillator.ultimate_oscillator()

            Momentum_Williams_R = WilliamsRIndicator(high=hist.High,low=hist.Low,close=hist.Close)
            hist['Williams %R'] = Momentum_Williams_R.williams_r()

            Volume_ADI = AccDistIndexIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
            hist['ADI'] = Volume_ADI.acc_dist_index()

            Volume_CMF = ChaikinMoneyFlowIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
            hist['CMF'] = Volume_CMF.chaikin_money_flow()

            Volume_FI = ForceIndexIndicator(close=hist.Close,volume=hist.Volume)
            hist['FI'] = Volume_FI.force_index()

            Volume_MFI = MFIIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
            hist['MFI'] = Volume_MFI.money_flow_index()

            Volume_VWAP = VolumeWeightedAveragePrice(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
            hist['VWAP'] = Volume_VWAP.volume_weighted_average_price()

            Volitility_Bollinger = BollingerBands(close=hist.Close)
            hist['Bollinger High Band'] = Volitility_Bollinger.bollinger_hband()
            hist['Bollinger High Band Indicator'] = Volitility_Bollinger.bollinger_hband_indicator()
            hist['Bollinger Low Band'] = Volitility_Bollinger.bollinger_lband()
            hist['Bollinger Low Band Indicator'] = Volitility_Bollinger.bollinger_lband_indicator()
            hist['Bollinger Middle Band'] = Volitility_Bollinger.bollinger_mavg()
            hist['Bollinger Percetage Band'] = Volitility_Bollinger.bollinger_pband()
            hist['Bollinger Band Width'] = Volitility_Bollinger.bollinger_wband()

            Volitility_Donchian = DonchianChannel(high=hist.High,low=hist.Low,close=hist.Close)
            hist['Donchian Channel High Band'] = Volitility_Donchian.donchian_channel_hband()
            hist['Donchian Channel Low Band'] = Volitility_Donchian.donchian_channel_lband()
            hist['Donchian Channel Middle Band'] = Volitility_Donchian.donchian_channel_mband()
            hist['Donchian Channel Percentage Band'] = Volitility_Donchian.donchian_channel_pband()
            hist['Donchian Channel Band Width'] = Volitility_Donchian.donchian_channel_wband()

            Volatility_Keltner = KeltnerChannel(high=hist.High,low=hist.Low,close=hist.Close)
            hist['Keltner Channel High Band'] = Volatility_Keltner.keltner_channel_hband()
            hist['Keltner Channel Indicator Crossing High Band'] = Volatility_Keltner.keltner_channel_hband_indicator()
            hist['Keltner Channel Low Band'] = Volatility_Keltner.keltner_channel_lband()
            hist['Keltner Channel Indicator Crossing Low Band'] = Volatility_Keltner.keltner_channel_lband_indicator()
            hist['Keltner Channel Middle Band'] = Volatility_Keltner.keltner_channel_mband()
            hist['Keltner Channel Percentage Band'] = Volatility_Keltner.keltner_channel_pband()
            hist['Keltner Channel Band Width'] = Volatility_Keltner.keltner_channel_wband()

            Volatility_Ulcer = UlcerIndex(close=hist.Close)
            hist['Ulcer Index'] = Volatility_Ulcer.ulcer_index()

            Volatility_ATR = average_true_range(high=hist.High,low=hist.Low,close=hist.Close)
            hist['ATR'] = Volatility_ATR

            Trend_Aroon = AroonIndicator(close=hist.Close)
            hist['Aroon Down Channel'] = Trend_Aroon.aroon_down()
            hist['Aroon Indicator'] = Trend_Aroon.aroon_indicator()
            hist['Aroon Up Channel'] = Trend_Aroon.aroon_up()

            Trend_CCI = CCIIndicator(high=hist.High,low=hist.Low,close=hist.Close)
            hist['CCI'] = Trend_CCI.cci()

            Trend_DPO = DPOIndicator(close=hist.Close)
            hist['DPO'] = Trend_DPO.dpo()

            Trend_EMA = EMAIndicator(close=hist.Close)
            hist['EMA'] = Trend_EMA.ema_indicator()

            Trend_Ichimoku = IchimokuIndicator(high=hist.High,low=hist.Low)
            hist['Ichimoku Senkou Span A'] = Trend_Ichimoku.ichimoku_a()
            hist['Ichimoku Senkou Span B'] = Trend_Ichimoku.ichimoku_b()
            hist['Ichimoku Kujun-sen'] = Trend_Ichimoku.ichimoku_base_line()
            hist['Ichimoku Tenkan-Sen'] = Trend_Ichimoku.ichimoku_conversion_line()

            Trend_KST = KSTIndicator(close=hist.Close)
            hist['KST'] = Trend_KST.kst()
            hist['Diff KST'] = Trend_KST.kst_diff()
            hist['Signal Line KST'] = Trend_KST.kst_sig()

            Trend_MACD = MACD(close=hist.Close)
            hist['MACD Line'] = Trend_MACD.macd()
            hist['MACD Histogram'] = Trend_MACD.macd_diff()
            hist['MACD Signal Line'] = Trend_MACD.macd_signal()

            Trend_MI = MassIndex(high=hist.High,low=hist.Low)
            hist['Mass Index'] = Trend_MI.mass_index()

            Trend_PSAR = PSARIndicator(high=hist.High,low=hist.Low,close=hist.Close)
            hist['PSAR'] = Trend_PSAR.psar()
            hist['PSAR Down'] = Trend_PSAR.psar_down()
            hist['PSAR Down Indicator'] = Trend_PSAR.psar_down_indicator()
            hist['PSAR Up'] = Trend_PSAR.psar_up()
            hist['PSAR Up Indicator'] = Trend_PSAR.psar_up_indicator()

            Trend_STC = STCIndicator(close=hist.Close)
            hist['STC'] = Trend_STC.stc()

            Trend_TRIX = TRIXIndicator(close=hist.Close)
            hist['TRIX'] = Trend_TRIX.trix()

            Trend_Vortex = VortexIndicator(high=hist.High,low=hist.Low,close=hist.Close)
            hist['VI'] = Trend_Vortex.vortex_indicator_diff()
            hist['VI-'] = Trend_Vortex.vortex_indicator_neg()
            hist['VI+'] = Trend_Vortex.vortex_indicator_pos()

            Trend_WMA = WMAIndicator(close=hist.Close)
            hist['WMA'] = Trend_WMA.wma()

            Other_CR = CumulativeReturnIndicator(close=hist.Close)
            hist['CR'] = Other_CR.cumulative_return()

            Other_DLR = DailyLogReturnIndicator(close=hist.Close)
            hist['DLR'] = Other_DLR.daily_log_return()

            Other_DR = DailyReturnIndicator(close=hist.Close)
            hist['DR'] = Other_DR.daily_return()

            hist.to_csv(fileDirectory + '/StockHistory/'+i+'.csv')
        except:
            pass

def fastCalculateStockIndicators():
    t = threading.Thread(target=getStockHistoryWithIndicators())
    t.start()

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
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(i)
            hist = stock.actions
            hist['ABV'] = i
            hist.to_csv(fileDirectory + '/StockEvents/'+ i +'.csv')
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
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stock = yf.Ticker(i)
            hist = stock.financials
            df_transposed = hist.transpose()
            df_transposed['ABV'] = i
            df_transposed.to_csv(fileDirectory + '/StockFinancials/'+i+'.csv')
        except:
            pass

def getStockOptions():
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            stockABV = i
            stock = yf.Ticker(stockABV)
            options = stock.options
            datalist = list(options)
            listOptions = pd.DataFrame(datalist, columns=['Dates'])
            for s in listOptions.index:
                opt = stock.option_chain(listOptions['Dates'][s])
                optCallsTable = opt.calls
                optCallsTable['ABV'] = i
                optCallsTable.to_csv(fileDirectory + '/Options/Calls/'+stockABV+'_'+listOptions['Dates'][s]+'.csv',index=False)
                optPutsTable = opt.puts
                optPutsTable['ABV'] = i
                optPutsTable.to_csv(fileDirectory + '/Options/Puts/'+stockABV+'_'+listOptions['Dates'][s]+'.csv',index=False)
        except:
            pass


        
def getMajorHolders():
    print('')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        
        stock = yf.Ticker(i)
        stockMajorHolders = stock.major_holders

        try:
            stockMajorHolders['ABV'] = i
            stockMajorHolders.to_csv(fileDirectory + '/Holders/Major/'+ i + '_major_holders.csv')
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

def getStockRecommendations():
    print('')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        
        stock = yf.Ticker(i)
        stockRecommendations = stock.recommendations

        try:
            stockRecommendations['ABV'] = i
            stockRecommendations.to_csv(fileDirectory + '/Recommendations/'+ i + '_recommendations.csv')
        except:
            pass

def getStockSustainability():
    print('')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        
        stock = yf.Ticker(i)
        stockSustainability = stock.sustainability
        try:
            stockSustainability = stockSustainability.transpose()
            stockSustainability['ABV'] = i
            stockSustainability.to_csv(fileDirectory + '/Sustainability/'+ i + '_sustainability.csv')
        except:
            pass

def getStockNews():
    print('')
    arr = stockList['Symbol'].to_numpy()
    for i in tqdm(arr.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        
        stock = yf.Ticker(i)
        stockNews = stock.news
        json_string = json.dumps(stockNews)
        #print(json_string)
        with open(fileDirectory+'/StockNews/'+i+'_news.json', 'w+') as file:
            file.write(json_string)    
            


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

def main():
    getStockHistory()

if __name__ == "__main__":
    main()


