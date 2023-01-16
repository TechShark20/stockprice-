# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:54:10 2023

@author: Samar jain

"""
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import streamlit as st 
df11=pd.read_csv("https://github.com/TechShark20/stockprice-/blob/11a045d03a26cf1ca8ebce270244669e615cd09c/stocksreport1.csv")
df21=pd.read_csv("https://github.com/TechShark20/stockprice-/blob/11a045d03a26cf1ca8ebce270244669e615cd09c/stocksreport2.csv")
df31=pd.read_csv("https://github.com/TechShark20/stockprice-/blob/11a045d03a26cf1ca8ebce270244669e615cd09c/stocksreport3.csv")
df = pd.concat((df11,df21,df31))
st.title('Stock market analyser')
st.write("""
Analysis of Nifty 50 stocks
""")
df.drop(columns=['Trades','Series'])
shname='TATASTEEL'
st.write("""
enter particular details

""")
tab1, tab2, tab3 = st.tabs(["Stockname", "Startdate", "Enddate"])
with tab1:
  shname=st.text_input("enter the name of your share ")
shname=shname.upper()
df1=df[df['Symbol']==shname]
with tab2:
  d1 = st.date_input( "Enter start date to view",datetime.datetime(2011, 1, 1))
with tab3:
  d2 = st.date_input( "Enter start date to view",datetime.datetime(2011, 7, 1))
df1['Date']= pd.to_datetime(df1['Date'])
df2 = df1[(df1['Date']>pd.Timestamp(d1))&(df1['Date']<pd.Timestamp(d2))]
st.write("showing the chart for"+shname)
st.dataframe(df2)
st.write("""closing price chart""")
chart1,chart2=st.tabs(['Closing','Volume'])
with chart1:
  st.header('Closing price chart')
  st.line_chart(df2,x='Date',y=['Close'])
with chart2:
  st.header(' volumes traded')
  st.line_chart(df2,x='Date',y=['Volume'])
