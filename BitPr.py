import pyupbit
import pandas as pd
import numpy as np

df = pyupbit.get_ohlcv("USDT-BTC", count=600, interval="minute3")
df = df.reset_index()
close = df['close']
y = df['index']
low = df['low']
high = df['high']

# n=일수

def mal(n): # 이평선
    return close.rolling(n).mean()

def slope(n): # 기울기
    maN_l = mal(n)[599]
    maN_s = mal(n)[580]
    maN_t = maN_l - maN_s 
    maN_y = 19/maN_t
    return maN_y 

def cci(n): #cci
    M = (close + low + high)/3
    m = M/n
    d = (abs(M - m))/n
    return (M - m) / d*0.015

def rsi(n): # RSI
    date_index = df.index.astype('str')
    U = np.where(df.diff(1)['close'] > 0, df.diff(1)['close'],0)
    D = np.where(df.diff(1)['close'] < 0, df.diff(1)['close']*-1, 0)
    AU = pd.DataFrame(U, index=date_index). rolling(window=n).mean()
    AD = pd.DataFrame(D, index=date_index). rolling(window=n).mean()
    return AU / (AU + AD)*100

