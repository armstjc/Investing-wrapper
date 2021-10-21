
# First import the libraries that we need to use
import pandas as pd
import requests
import json
from urllib.request import urlopen 
from bs4 import BeautifulSoup
from fileDirectoryCreation import *
from tqdm import tqdm
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

    for bill in storage['Data']:
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
        print(cryptoID+': '+cryptoName)
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
        data['date'] = pd.to_datetime(data['unix'], unit='s')  # convert to a readable date
        data['vol_fiat'] = data['volume'] * data['close']      # multiply the BTC volume by closing price to approximate fiat volume

        # if we failed to get any data, print an error...otherwise write the file
        if data is None:
            print("Did not return any data from Coinbase for this symbol")
        else:
            data.to_csv(fileDirectory+'/Crypto/Coinbase_'+ pair_split[0] +'-'+ pair_split[1] + '_dailydata.csv', index=False)

    else:
        print("Did not receieve OK response from Coinbase API")

def fetchAllCoinbase():
    coinbaseSymbols = pd.read_csv(fileDirectory+'/Crypto/coinbase_listings.csv')

    for c in tqdm(coinbaseSymbols.index, ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        fetchDailyData(str(coinbaseSymbols['id'][c]).replace('-','/'))


#if __name__ == "__main__":
#    # we set which pair we want to retrieve data for
#    pair = "BTC/USD"
#    fetch_daily_data(symbol="BTC/USD")
