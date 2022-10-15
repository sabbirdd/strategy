import numpy as np
import pandas as pd
import ta
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.sidebar.title("Sabbir's Stock Scanner")

price = pd.read_excel('Price.xlsx', index_col=0)

stocks = price['symbol'].to_list()

symbol = []
for i in stocks:
    if i not in symbol:
        symbol.append(i)


symbol_tup = tuple(symbol)

option = st.sidebar.selectbox("Please select the dasboard you want to see", ('Strategy Checking', 'Technicals'))

if option =='Strategy Checking':
    selected_stock = st.sidebar.selectbox("Please select the stock",symbol_tup)
    data = price[price.symbol==selected_stock]
    st.write(data.head())
    