import pandas as pd
from ta import add_all_ta_features
from ta.momentum import *
from ta.volume import *
from ta.volatility import *
from ta.trend import * 
from ta.others import *
from ta.utils import dropna

# Load datas
hist = pd.read_csv('D:/Stocks/StockHistory/AAPL.csv', sep=',')

# Clean NaN values
hist.dropna(axis=0, inplace=True)

print(hist)


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

#Momentum_ROC = ROCIndicator(close=hist.Close, window=12)
#hist['ROC'] = ROCIndicator.roc()

Momentum_RSI = RSIIndicator(close=hist.Close,window=14)
hist['RSI'] = Momentum_RSI.rsi()

#Momentum_S_RSI = StochRSIIndicator(close=hist.Close,window=14)
#hist['Stoch RSI'] = StochRSIIndicator.stochrsi()

Momentum_StochasticOscillator = StochasticOscillator(hist.High, hist.Low, hist.Close)
hist['Stochastic Oscillator'] = Momentum_StochasticOscillator.stoch()
hist['Stochastic Oscillator_Signial'] = Momentum_StochasticOscillator.stoch_signal()

#Momentum_TSI = TSIIndicator(close=hist.Close)
#hist['TSI'] = TSIIndicator.tsi()

Momentum_UltimateOscillator = UltimateOscillator(high=hist.High, low=hist.Low, close=hist.Close)
hist['Ultimate Oscillator'] = Momentum_UltimateOscillator.ultimate_oscillator()


Momentum_Williams_R = WilliamsRIndicator(high=hist.High,low=hist.Low,close=hist.Close)
hist['Williams %R'] = Momentum_Williams_R.williams_r()

#Momentum_AwesomeOscillator = awesome_oscillator(high=hist.High,low=hist.Low)
#hist['Awesome Oscillator'] = Momentum_AwesomeOscillator()

#Momentum_KAMA = kama(close=hist.Close)
#hist['KAMA'] = Momentum_KAMA()

Volume_ADI = AccDistIndexIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
hist['ADI'] = Volume_ADI.acc_dist_index()

Volume_CMF = ChaikinMoneyFlowIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
hist['CMF'] = Volume_CMF.chaikin_money_flow()

#Volume_EoM_EMV = EaseOfMovementIndicator(high=hist.High,low=hist.Low,volume=hist.Volume)
#hist['EoM/EMV'] = EaseOfMovementIndicator.ease_of_movement()
#hist['SMA EoM/EMV'] = EaseOfMovementIndicator.sma_ease_of_movement()

Volume_FI = ForceIndexIndicator(close=hist.Close,volume=hist.Volume)
hist['FI'] = Volume_FI.force_index()

Volume_MFI = MFIIndicator(high=hist.High,low=hist.Low,close=hist.Close,volume=hist.Volume)
hist['MFI'] = Volume_MFI.money_flow_index()

#Volume_NVI = NegativeVolumeIndexIndicator(close=hist.Close,volume=hist.Volume)
#hist['NVI'] = NegativeVolumeIndexIndicator.negative_volume_index()

#Volume_OBV = OnBalanceVolumeIndicator(close=hist.Close,volume=hist.Volume)
#hist['OBV'] = OnBalanceVolumeIndicator.on_balance_volume()

#Volume_VPD = VolumePriceTrendIndicator(close=hist.Close,volume=hist.Volume)
#hist['VPD'] = Volume_VPD

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


## DO NOT USE FOR ALL STOCKS!! MAY CAUSE RUNTIME ERRORS!!
#Trend_ADX = ADXIndicator(high=hist.High,low=hist.Low,close=hist.Close)
#hist['ADX'] = Trend_ADX.adx()
#hist['ADX -DI'] = Trend_ADX.adx_neg()
#hist['Adx +DI'] = Trend_ADX.adx_pos()

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

#Trend_SMA = SMAIndicator(close=hist.Close)
#hist['SMA'] = Trend_SMA.sma_indicator()

Trend_STC = STCIndicator(close=hist.Close)
hist['STC'] = Trend_STC.stc()

Trend_TRIX = TRIXIndicator(close=hist.Close)
hist['TRIX'] = Trend_TRIX.trix()

Trend_Vortex = VortexIndicator(high=hist.High,low=hist.Low,close=hist.Close)
hist['VI'] = Trend_Vortex.vortex_indicator_diff()
hist['-VI'] = Trend_Vortex.vortex_indicator_neg()
hist['+VI'] = Trend_Vortex.vortex_indicator_pos()

Trend_WMA = WMAIndicator(close=hist.Close)
hist['WMA'] = Trend_WMA.wma()

Other_CR = CumulativeReturnIndicator(close=hist.Close)
hist['CR'] = Other_CR.cumulative_return()

Other_DLR = DailyLogReturnIndicator(close=hist.Close)
hist['DLR'] = Other_DLR.daily_log_return()

Other_DR = DailyReturnIndicator(close=hist.Close)
hist['DR'] = Other_DR.daily_return()



hist.to_csv('TA_test.csv')

print(hist)