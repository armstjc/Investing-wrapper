
# First import the libraries that we need to use
import pandas as pd
import requests
import json
from urllib.request import urlopen 
from bs4 import BeautifulSoup
from fileDirectoryCreation import *
from tqdm import tqdm
from ta import add_all_ta_features
from ta.momentum import *
from ta.volume import *
from ta.volatility import *
from ta.trend import * 
from ta.others import *
from ta.utils import dropna
import glob
import datetime
import numpy as np

year = str(datetime.date.today().year)
print(year)
checkFolderIntegrity()

def fetchCryptoCurrencies():
    '''
    
    Fetches a list of cryptocurrencies from a JSON file through the Crypto Compare API, and
    then parses the JSON file into a more usable CSV file.
    
    Source used: https://min-api.cryptocompare.com/data/all/coinlist


    '''
    URL = 'https://min-api.cryptocompare.com/data/all/coinlist'
    response = requests.get(URL)
    storage = response.json()

    df_crypto = pd.DataFrame()

    cryptoID = ''
    cryptoURL = ''
    cryptoImageURL = ''
    cryptoCreationDate = ''
    cryptoName = ''
    cryptoSymbol = ''
    cryptoCoinName = ''
    cryptoFullName = ''
    cryptoDescription = ''
    cryptoAssetTokenStatus = ''
    cryptoAlgorithm = ''
    cryptoProofType = ''
    cryptoSortOrder = ''
    cryptoSponsored = ''
    cryptoTaxonomyAccess = ''
    cryptoTaxonomyFCA = ''
    cryptoTaxonomyFINMA = ''
    cryptoTaxonomyIndustry = ''
    cryptoTaxonomyCollateralizedAsset = ''
    cryptoTaxonomyCollateralizedAssetType = ''
    cryptoTaxonomyCollateralType = ''
    cryptoTaxonomyCollateralInfo = ''
    cryptoWeissRating = ''
    cryptoWeissTechnologyAdoptionRating = ''
    cryptoWeissMarketPerformanceRating = ''
    cryptoIsTrading = ''
    cryptoTotalCoinsMined = ''
    cryptoCirculatingSupply = ''
    cryptoBlockNumber = ''
    cryptoNetHashesPerSecond = ''
    cryptoBlockReward = ''
    cryptoBlockTime = ''
    cryptoAssetLaunchDate = ''
    cryptoAssetWhitepaperUrl = ''
    cryptoAssetWebsiteUrl = ''
    cryptoMaxSupply = ''
    cryptoMktCapPenalty = ''
    cryptoIsUsedInDefi = ''
    cryptoIsUsedInNft = ''

    for bill in tqdm(storage['Data'],ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        try:
            cryptoID = storage['Data'][bill]['Id']
        except:
            cryptoID = ''

        try:
            cryptoURL = storage['Data'][bill]['Url']
        except: 
            cryptoURL =''

        try:
            cryptoImageURL = storage['Data'][bill]['ImageUrl']
        except:
            cryptoImageURL = ''

        try:
            cryptoCreationDate = storage['Data'][bill]['ContentCreatedOn']
        except:
            cryptoCreationDate = ''

        try:
            cryptoName = storage['Data'][bill]['Name']
        except:
            cryptoName = ''

        try:
            cryptoSymbol = storage['Data'][bill]['Symbol']
        except:
            cryptoSymbol = ''

        try:
            cryptoCoinName = storage['Data'][bill]['CoinName']
        except:
            cryptoCoinName = ''

        try:
            cryptoFullName = storage['Data'][bill]['FullName']
        except:
            cryptoFullName = ''

        try:
            cryptoDescription = storage['Data'][bill]['Description']
        except:
            cryptoDescription = ''

        try:
            cryptoAssetTokenStatus = storage['Data'][bill]['AssetTokenStatus']
        except:
            cryptoAssetTokenStatus = ''

        try:
            cryptoAlgorithm = storage['Data'][bill]['Algorithm']
        except:
            cryptoAlgorithm = ''

        try:
            cryptoProofType = storage['Data'][bill]['ProofType']
        except:
            cryptoProofType = ''

        try:
            cryptoSortOrder = storage['Data'][bill]['SortOrder']
        except:
            cryptoSortOrder = ''

        try:
            cryptoSponsored = storage['Data'][bill]['Sponsored']
        except:
            cryptoSponsored = ''

        try:
            cryptoTaxonomyAccess = storage['Data'][bill]['Taxonomy']['Access']
        except:
            cryptoTaxonomyAccess = ''

        try:
            cryptoTaxonomyFCA = storage['Data'][bill]['Taxonomy']['FCA']
        except:
            cryptoTaxonomyFCA = ''

        try:
            cryptoTaxonomyFINMA = storage['Data'][bill]['Taxonomy']['FINMA']
        except:
            cryptoTaxonomyFINMA = ''

        try:
            cryptoTaxonomyIndustry = storage['Data'][bill]['Taxonomy']['Industry']
        except:
            cryptoTaxonomyIndustry = ''

        try:
            cryptoTaxonomyCollateralizedAsset = storage['Data'][bill]['Taxonomy']['CollateralizedAsset']
        except:
            cryptoTaxonomyCollateralizedAsset = ''

        try:
            cryptoTaxonomyCollateralizedAssetType = storage['Data'][bill]['Taxonomy']['CollateralizedAssetType']
        except:
            cryptoTaxonomyCollateralizedAssetType = ''

        try:
            cryptoTaxonomyCollateralType = storage['Data'][bill]['Taxonomy']['CollateralType']
        except:
            cryptoTaxonomyCollateralType = ''
        
        try:
            cryptoTaxonomyCollateralInfo = storage['Data'][bill]['Taxonomy']['CollateralInfo']
        except:
            cryptoTaxonomyCollateralInfo = ''

        try:
            cryptoWeissRating = storage['Data'][bill]['Rating']['Weiss']['Rating']
        except:
            cryptoWeissRating = ''

        try:
            cryptoWeissTechnologyAdoptionRating = storage['Data'][bill]['Rating']['Weiss']['TechnologyAdoptionRating']
        except:
            cryptoWeissTechnologyAdoptionRating = ''

        try:
            cryptoWeissMarketPerformanceRating = storage['Data'][bill]['Rating']['Weiss']['MarketPerformanceRating']
        except:
            cryptoWeissMarketPerformanceRating = ''

        try:
            cryptoIsTrading = storage['Data'][bill]['IsTrading']
        except:
            cryptoIsTrading = ''
        
        try:
            cryptoTotalCoinsMined = storage['Data'][bill]['TotalCoinsMined']
        except:
            cryptoTotalCoinsMined = ''
        
        try:
            cryptoCirculatingSupply = storage['Data'][bill]['CirculatingSupply']
        except:
            cryptoCirculatingSupply = ''
        
        try:
            cryptoBlockNumber = storage['Data'][bill]['BlockNumber']
        except:
            cryptoBlockNumber = ''
        
        try:
            cryptoNetHashesPerSecond = storage['Data'][bill]['NetHashesPerSecond']
        except:
            cryptoNetHashesPerSecond = ''
        
        try:
            cryptoBlockReward = storage['Data'][bill]['BlockReward']
        except:
            cryptoBlockReward = ''
        
        try:
            cryptoBlockTime = storage['Data'][bill]['BlockTime']
        except:
            cryptoBlockTime = ''
        
        try:
            cryptoAssetLaunchDate = storage['Data'][bill]['AssetLaunchDate']
        except:
            cryptoAssetLaunchDate = ''
        
        try:
            cryptoAssetWhitepaperUrl = storage['Data'][bill]['AssetWhitepaperUrl']
        except:
            cryptoAssetWhitepaperUrl = ''
        
        try:
            cryptoAssetWebsiteUrl = storage['Data'][bill]['AssetWebsiteUrl']
        except:
            cryptoAssetWebsiteUrl = ''
        
        try:
            cryptoMaxSupply = storage['Data'][bill]['MaxSupply']
        except:
            cryptoMaxSupply = ''
        
        try:
            cryptoMktCapPenalty = storage['Data'][bill]['MktCapPenalty']
        except:
            cryptoMktCapPenalty = ''

        try:
            cryptoIsUsedInDefi = storage['Data'][bill]['IsUsedInDefi']
        except:
            cryptoIsUsedInDefi = ''

        try:
            cryptoIsUsedInNft = storage['Data'][bill]['IsUsedInNft']
        except:
            cryptoIsUsedInNft = ''

        new_row = {
        'cryptoID':cryptoID,
        'cryptoURL':cryptoURL,
        'cryptoImageURL':cryptoImageURL,
        'cryptoCreationDate':cryptoCreationDate,
        'cryptoName':cryptoName,
        'cryptoSymbol':cryptoSymbol,
        'cryptoCoinName':cryptoCoinName,
        'cryptoFullName':cryptoFullName,
        'cryptoDescription':cryptoDescription,
        'cryptoAssetTokenStatus':cryptoAssetTokenStatus,
        'cryptoAlgorithm':cryptoAlgorithm,
        'cryptoProofType':cryptoProofType,
        'cryptoSortOrder':cryptoSortOrder,
        'cryptoSponsored':cryptoSponsored,
        'cryptoTaxonomyAccess':cryptoTaxonomyAccess,
        'cryptoTaxonomyFCA':cryptoTaxonomyFCA,
        'cryptoTaxonomyFINMA':cryptoTaxonomyFINMA,
        'cryptoTaxonomyIndustry':cryptoTaxonomyIndustry,
        'cryptoTaxonomyCollateralizedAsset':cryptoTaxonomyCollateralizedAsset,
        'cryptoTaxonomyCollateralizedAssetType':cryptoTaxonomyCollateralizedAssetType,
        'cryptoTaxonomyCollateralType':cryptoTaxonomyCollateralType,
        'cryptoTaxonomyCollateralInfo':cryptoTaxonomyCollateralInfo,
        'cryptoWeissRating':cryptoWeissRating,
        'cryptoWeissTechnologyAdoptionRating':cryptoWeissTechnologyAdoptionRating,
        'cryptoWeissMarketPerformanceRating':cryptoWeissMarketPerformanceRating,
        'cryptoIsTrading':cryptoIsTrading,
        'cryptoTotalCoinsMined':cryptoTotalCoinsMined,
        'cryptoCirculatingSupply':cryptoCirculatingSupply,
        'cryptoBlockNumber':cryptoBlockNumber,
        'cryptoNetHashesPerSecond':cryptoNetHashesPerSecond,
        'cryptoBlockReward':cryptoBlockReward,
        'cryptoBlockTime':cryptoBlockTime,
        'cryptoAssetLaunchDate':cryptoAssetLaunchDate,
        'cryptoAssetWhitepaperUrl':cryptoAssetWhitepaperUrl,
        'cryptoAssetWebsiteUrl':cryptoAssetWebsiteUrl,
        'cryptoMaxSupply':cryptoMaxSupply,
        'cryptoMktCapPenalty':cryptoMktCapPenalty,
        'cryptoIsUsedInDefi':cryptoIsUsedInDefi,
        'cryptoIsUsedInNft':cryptoIsUsedInNft            
        }
        df_crypto = df_crypto.append(new_row, ignore_index=True)
        #print(cryptoID+': '+cryptoName)
    df_crypto.to_csv(fileDirectory+'/cryptoABV.csv',index=False)
    print(df_crypto)
    
def fetchCoinbaseSymbols(file):
    '''

    Utilizes the Coinbase PRO API to grab a list of cryptocurencies supported
    by Coinbase, and their online platform, and saves them to a local CSV file.

    To start, download the file from 'https://api.pro.coinbase.com/products' as a JSON file,
    then feed it through this function to get desired results.

    Args:
    file: the directory your saved JSON file exists in.

    '''
    print(file)
    jsonFile = file
    df = pd.read_json(jsonFile)
    df.to_csv(fileDirectory+'/Crypto/coinbase_listings.csv')
    print(df)


def fetchDailyData(symbol):
    '''
    args: symbol
    You need to input the Cryptocurrency, and the currency you are trying to compare agianst.
    For example, if you want the price of Bitcoin (BTC) agianst the United States Dollar (USD) you input
    etch_daily_data(symbol="BTC/USD")

    Code pre-developed from CryptoDataDownload.com

    Grabs the historical price data for a provided cryptocurrency agianst another currency.

    '''
    # Code pre-developed from CryptoDataDownload
    pair_split = symbol.split('/')  # symbol must be in format XXX/XXX ie. BTC/EUR
    symbol = pair_split[0] + '-' + pair_split[1]
    url = f'https://api.pro.coinbase.com/products/{symbol}/candles?granularity=86400'
    response = requests.get(url)
    if response.status_code == 200:  # check to make sure the response from server is good
        data = pd.DataFrame(json.loads(response.text), columns=['unix', 'low', 'high', 'open', 'close', 'volume'])
        data.sort_values(by=['unix'],inplace=True)
        data['date'] = pd.to_datetime(data['unix'], unit='s')  # convert to a readable date
        data['vol_fiat'] = data['volume'] * data['close']      # multiply the BTC volume by closing price to approximate fiat volume
        data['Symbol'] = symbol
        Momentum_AOI = AwesomeOscillatorIndicator(high=data.high, low=data.low)
        data['AOI'] = Momentum_AOI.awesome_oscillator()

        Momentum_KARMA = KAMAIndicator(close=data.close)
        data['KAMA'] = Momentum_KARMA.kama()

        Momentum_PPO = PercentagePriceOscillator(close=data.close)
        data['PPO'] = Momentum_PPO.ppo()
        data['PPO_Histogram'] = Momentum_PPO.ppo_hist()
        data['PPO_Signal'] = Momentum_PPO.ppo_hist()

        Momentum_PVO = PercentageVolumeOscillator(volume=data.volume)
        data['PVO'] = Momentum_PVO.pvo()
        data['PVO_Histogram'] = Momentum_PVO.pvo_hist()
        data['PVO_Signal'] = Momentum_PVO.pvo_signal()

        Momentum_RSI = RSIIndicator(close=data.close,window=14)
        data['RSI'] = Momentum_RSI.rsi()

        Momentum_StochasticOscillator = StochasticOscillator(data.high, data.low, data.close)
        data['Stochastic Oscillator'] = Momentum_StochasticOscillator.stoch()
        data['Stochastic Oscillator_Signial'] = Momentum_StochasticOscillator.stoch_signal()

        Momentum_UltimateOscillator = UltimateOscillator(high=data.high, low=data.low, close=data.close)
        data['Ultimate Oscillator'] = Momentum_UltimateOscillator.ultimate_oscillator()

        Momentum_Williams_R = WilliamsRIndicator(high=data.high,low=data.low,close=data.close)
        data['Williams %R'] = Momentum_Williams_R.williams_r()

        Volume_ADI = AccDistIndexIndicator(high=data.high,low=data.low,close=data.close,volume=data.volume)
        data['ADI'] = Volume_ADI.acc_dist_index()

        Volume_CMF = ChaikinMoneyFlowIndicator(high=data.high,low=data.low,close=data.close,volume=data.volume)
        data['CMF'] = Volume_CMF.chaikin_money_flow()

        Volume_FI = ForceIndexIndicator(close=data.close,volume=data.volume)
        data['FI'] = Volume_FI.force_index()

        Volume_MFI = MFIIndicator(high=data.high,low=data.low,close=data.close,volume=data.volume)
        data['MFI'] = Volume_MFI.money_flow_index()

        Volume_VWAP = VolumeWeightedAveragePrice(high=data.high,low=data.low,close=data.close,volume=data.volume)
        data['VWAP'] = Volume_VWAP.volume_weighted_average_price()

        Volitility_Bollinger = BollingerBands(close=data.close)
        data['Bollinger High Band'] = Volitility_Bollinger.bollinger_hband()
        data['Bollinger High Band Indicator'] = Volitility_Bollinger.bollinger_hband_indicator()
        data['Bollinger Low Band'] = Volitility_Bollinger.bollinger_lband()
        data['Bollinger Low Band Indicator'] = Volitility_Bollinger.bollinger_lband_indicator()
        data['Bollinger Middle Band'] = Volitility_Bollinger.bollinger_mavg()
        data['Bollinger Percetage Band'] = Volitility_Bollinger.bollinger_pband()
        data['Bollinger Band Width'] = Volitility_Bollinger.bollinger_wband()

        Volitility_Donchian = DonchianChannel(high=data.high,low=data.low,close=data.close)
        data['Donchian Channel High Band'] = Volitility_Donchian.donchian_channel_hband()
        data['Donchian Channel Low Band'] = Volitility_Donchian.donchian_channel_lband()
        data['Donchian Channel Middle Band'] = Volitility_Donchian.donchian_channel_mband()
        data['Donchian Channel Percentage Band'] = Volitility_Donchian.donchian_channel_pband()
        data['Donchian Channel Band Width'] = Volitility_Donchian.donchian_channel_wband()

        Volatility_Keltner = KeltnerChannel(high=data.high,low=data.low,close=data.close)
        data['Keltner Channel High Band'] = Volatility_Keltner.keltner_channel_hband()
        data['Keltner Channel Indicator Crossing High Band'] = Volatility_Keltner.keltner_channel_hband_indicator()
        data['Keltner Channel Low Band'] = Volatility_Keltner.keltner_channel_lband()
        data['Keltner Channel Indicator Crossing Low Band'] = Volatility_Keltner.keltner_channel_lband_indicator()
        data['Keltner Channel Middle Band'] = Volatility_Keltner.keltner_channel_mband()
        data['Keltner Channel Percentage Band'] = Volatility_Keltner.keltner_channel_pband()
        data['Keltner Channel Band Width'] = Volatility_Keltner.keltner_channel_wband()

        Volatility_Ulcer = UlcerIndex(close=data.close)
        data['Ulcer Index'] = Volatility_Ulcer.ulcer_index()

        try:
            Volatility_ATR = average_true_range(high=data.high,low=data.low,close=data.close)
            data['ATR'] = Volatility_ATR
        except:
            pass
        
        

        Trend_Aroon = AroonIndicator(close=data.close)
        data['Aroon Down Channel'] = Trend_Aroon.aroon_down()
        data['Aroon Indicator'] = Trend_Aroon.aroon_indicator()
        data['Aroon Up Channel'] = Trend_Aroon.aroon_up()

        Trend_CCI = CCIIndicator(high=data.high,low=data.low,close=data.close)
        data['CCI'] = Trend_CCI.cci()

        Trend_DPO = DPOIndicator(close=data.close)
        data['DPO'] = Trend_DPO.dpo()

        Trend_EMA = EMAIndicator(close=data.close)
        data['EMA'] = Trend_EMA.ema_indicator()

        Trend_Ichimoku = IchimokuIndicator(high=data.high,low=data.low)
        data['Ichimoku Senkou Span A'] = Trend_Ichimoku.ichimoku_a()
        data['Ichimoku Senkou Span B'] = Trend_Ichimoku.ichimoku_b()
        data['Ichimoku Kujun-sen'] = Trend_Ichimoku.ichimoku_base_line()
        data['Ichimoku Tenkan-Sen'] = Trend_Ichimoku.ichimoku_conversion_line()

        Trend_KST = KSTIndicator(close=data.close)
        data['KST'] = Trend_KST.kst()
        data['Diff KST'] = Trend_KST.kst_diff()
        data['Signal Line KST'] = Trend_KST.kst_sig()

        Trend_MACD = MACD(close=data.close)
        data['MACD Line'] = Trend_MACD.macd()
        data['MACD Histogram'] = Trend_MACD.macd_diff()
        data['MACD Signal Line'] = Trend_MACD.macd_signal()

        Trend_MI = MassIndex(high=data.high,low=data.low)
        data['Mass Index'] = Trend_MI.mass_index()

        Trend_PSAR = PSARIndicator(high=data.high,low=data.low,close=data.close)
        data['PSAR'] = Trend_PSAR.psar()
        data['PSAR Down'] = Trend_PSAR.psar_down()
        data['PSAR Down Indicator'] = Trend_PSAR.psar_down_indicator()
        data['PSAR Up'] = Trend_PSAR.psar_up()
        data['PSAR Up Indicator'] = Trend_PSAR.psar_up_indicator()

        Trend_STC = STCIndicator(close=data.close)
        data['STC'] = Trend_STC.stc()

        Trend_TRIX = TRIXIndicator(close=data.close)
        data['TRIX'] = Trend_TRIX.trix()

        Trend_Vortex = VortexIndicator(high=data.high,low=data.low,close=data.close)
        data['VI'] = Trend_Vortex.vortex_indicator_diff()
        data['VI-'] = Trend_Vortex.vortex_indicator_neg()
        data['VI+'] = Trend_Vortex.vortex_indicator_pos()

        Trend_WMA = WMAIndicator(close=data.close)
        data['WMA'] = Trend_WMA.wma()

        Other_CR = CumulativeReturnIndicator(close=data.close)
        data['CR'] = Other_CR.cumulative_return()

        Other_DLR = DailyLogReturnIndicator(close=data.close)
        data['DLR'] = Other_DLR.daily_log_return()

        Other_DR = DailyReturnIndicator(close=data.close)
        data['DR'] = Other_DR.daily_return()
        # if we failed to get any data, print an error...otherwise write the file
        if data is None:
            print("Did not return any data from Coinbase for this symbol")
        else:
            if(pair_split[1] == "EUR"):
                data.to_csv(fileDirectory+'/Crypto/EUR/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+'dailydata.csv', index=False)
            elif(pair_split[1] == "GBP"):
                data.to_csv(fileDirectory+'/Crypto/GBP/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)
            elif(pair_split[1] == "USD"):
                data.to_csv(fileDirectory+'/Crypto/USD/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)
            elif(pair_split[1] == "USDC"):
                data.to_csv(fileDirectory+'/Crypto/USDC/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)
            elif(pair_split[1] == "USDT"):
                data.to_csv(fileDirectory+'/Crypto/USDT/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)
            elif(pair_split[1] == "UST"):
                data.to_csv(fileDirectory+'/Crypto/UST/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)
            elif(pair_split[1] == "BTC"):
                data.to_csv(fileDirectory+'/Crypto/USDT/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)
            elif(pair_split[1] == "ETH"):
                data.to_csv(fileDirectory+'/Crypto/UST/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)
            elif(pair_split[1] == "DAI"):
                data.to_csv(fileDirectory+'/Crypto/UST/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)
            else:
                data.to_csv(fileDirectory+'/Crypto/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_'+year+ '_dailydata.csv', index=False)


    else:
        print("Did not receieve OK response from Coinbase API")

def fetchAllCoinbase():
    coinbaseSymbols = pd.read_csv(fileDirectory+'/Crypto/coinbase_listings.csv')
    df = coinbaseSymbols['id'].to_numpy()
    for c in tqdm(df.T, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        fetchDailyData(str(c).replace('-','/'))

def mergeCoinbaseFiles():
    main_df = pd.DataFrame()
    l = fileDirectory + "/Crypto/USD"
    f = 0
    for file in glob.iglob(l+"/*csv"):
        f = f + 1

    for file in tqdm(glob.iglob(l+"/*csv"),total=f,ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        df = pd.read_csv(file)
        main_df = pd.concat([main_df, df], ignore_index=True)
    main_df.to_csv(fileDirectory + "/Crypto/Merged"+year+".csv", index=False)


#if __name__ == "__main__":
#    # we set which pair we want to retrieve data for
#    pair = "BTC/USD"
#    fetch_daily_data(symbol="BTC/USD")
