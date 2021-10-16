import yfinance as yf

from fileDirectoryCreation import *
checkFolderIntegrity()

stock = yf.Ticker("MSFT")

print('get stock info')
stockInfo = stock.info
print(stockInfo)
print('')

# get historical market data
print('get historical market data')
hist = stock.history(period="max")
print(hist)
print('')

# show actions (dividends, splits)
print('show actions (dividends, splits)')
stockActions = stock.actions
print(stockActions)
print('')

# show dividends
print('show dividends')
stockDividends = stock.dividends
print(stockDividends)
print('')

# show splits
print('show splits')
stockSplits = stock.splits
print(stockSplits)
print('')
 
# show financials
print('show financials')
stockFinancials = stock.financials
print(stockFinancials)
print('')

print('show quarterly financials')
stockQuarterlyFinancials = stock.quarterly_financials
print(stockQuarterlyFinancials)
print('')

# show major holders
print('show major holders')
stockMajorHolders = stock.major_holders
print(stockMajorHolders)
print('')

# show institutional holders
print('show institutional holders')
stockInstitutionalHolders = stock.institutional_holders
print(stockInstitutionalHolders)
print('')

# show balance sheet
print('show balance sheet')
stockBalanceSheet = stock.balance_sheet
print(stockBalanceSheet)
print('')

print('show quarterly balance sheet')
stockQuarterlyBalanceSheet = stock.quarterly_balance_sheet
print(stockQuarterlyBalanceSheet)
print('')

# show cashflow
print('show cashflow')
stockCashflow = stock.cashflow
print(stockCashflow)
print('')

print('show quarterly cashflow')
stockQuarterlyCashflow = stock.quarterly_cashflow
print(stockQuarterlyCashflow)
print('')

# show earnings
print('show earnings')
stockEarnings = stock.earnings
print(stockEarnings)
print('')

print('show quarterly earnings')
stockQuarterlyEarnings = stock.quarterly_earnings
print(stockQuarterlyEarnings)
print('')

# show sustainability
print('show sustainability')
stockSustainability = stock.sustainability
print(stockSustainability)
print('')

# show analysts recommendations
print('show analysts recommendations')
stockRecomendations = stock.recommendations
print(stockRecomendations)
print('')

# show next event (earnings, etc)
print('show next event (earnings, etc)')
stockCalendar = stock.calendar
print(stockCalendar)
print('')

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
print('show ISIN code - *experimental*')
print('ISIN = International Securities Identification Number')
stockISIN_Code = stock.isin
print(stockISIN_Code)
print('')

# show options expirations
print('show options expirations')
stockOptions = stock.options
print(stockOptions)
print('')

# get option chain for specific expiration
print('get option chain for specific expiration')
opt = stock.option_chain('2021-10-01')
print('')

# data available via: opt.calls, opt.puts
print('data available via: opt.calls')
stockOptionCalls = opt.calls
print(stockOptionCalls)
print('')

print('data available via: opt.puts')
stockOptionPuts = opt.puts
print(stockOptionPuts)
print('')

# get ticker data
print('get ticker data')
stockTickers = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "MSFT",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1d",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )
df = stockTickers
print(df)