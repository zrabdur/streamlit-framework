import os
import streamlit as st
from dotenv import load_dotenv
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
#import numpy as np
import pandas as pd
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.

import requests
import json

import plotly.graph_objects as go
#import matplotlib.pyplot as plt
from io import StringIO

load_dotenv()

add_textinput = st.sidebar.text_input(
    'Enter company name'
)
ticker = add_textinput
add_selectbox = st.sidebar.selectbox(
'Select Year',
('2015','2016','2017','2018', '2019', '2020')
)
year1 = add_selectbox
add_selectbox = st.sidebar.selectbox(
'Select Month',
('January','February','March','April','May','June','July','August','September','October','November','December')
)
month1=add_selectbox

if month1 == 'January':
    month1 = '01'
elif month1 == 'February':
    month1 = '02'
elif month1 == 'March':
    month1 = '03'
elif month1 == 'April':
    month1 = '04'
elif month1 == 'May':
    month1 = '05'
elif month1 == 'June':
    month1 = '06'
elif month1 == 'July':
    month1 = '07'
elif month1 == 'August':
    month1 = '08'
elif month1 == 'September':
    month1 = '09'
elif month1 == 'October':
    month1 = '10'
elif month1 == 'November':
    month1 = '11'
elif month1 == 'December':
    month1 = '12'

#
###########key = 'DVIO8GSIISAAPZE1'

key = os.getenv('key')
# ticker = 'AAPL'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)

response = requests.get(url)
dat=(response.json())
#
# Set date here
# year1='2020'
# month1='12'

# Find the time series data from the overall data
tsd = dat['Time Series (Daily)']

# Set search key and find all items containing the search key
searchKey1 = year1 + '-' + month1
res = dict(filter(lambda item: searchKey1 in item[0], tsd.items()))

# Aqcuire close values and index values for items found earlier
df = pd.DataFrame(res)
tdf = df.T
tdf = tdf.iloc[::-1]##reversed_df to reveser dates
l1 = tdf['4. close'].values.tolist()
itdf = tdf.index


# Graph
fig = go.Figure(go.Scatter(
    x = itdf,
    y = l1
))
fig.update_xaxes(type='category')

#
st.title('Title: Get API Data')

st.write(fig)
