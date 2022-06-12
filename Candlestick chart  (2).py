#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import requests
import json


# In[2]:


quote='GOOGL'
days=30
def candlestick(quote,days):
    r=requests.get(f'https://financialmodelingprep.com/api/v3/historical-price-full/{quote}?timeseries={days}&apikey=5440fa1b83055823728a35b8988f31eb')
    r=r.json()
    ourdata=r['historical']
    df=pd.DataFrame.from_dict(ourdata)
    df
    fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])
    fig.update_layout(
    title="Candle stock price",
    yaxis_title='price')
    fig.show()

candlestick(quote,days)


# In[ ]:





# In[ ]:




