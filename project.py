import streamlit as st
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
import xlrd
from PIL import Image
st.set_page_config(
    page_title="猛祺的期末報告",
    page_icon='phil.ico'
    )
st.title('中華職棒數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇球隊？', ['中信兄弟', '統一7-Eleven獅', '味全龍', '樂天桃猿','富邦悍將'])
option1 = st.sidebar.selectbox( '選擇所想查看的數據？', ['球隊成績', '投手成績', '打擊成績', '守備成績'])
BrothersPitching=pd.read_excel('BrothersPitching.xlsx')
UnilionsPitching=pd.read_excel('UnilionsPitching.xlsx')
DragonsPitching=pd.read_excel('DragonsPitching.xlsx')
RakutenPitching=pd.read_excel('RakutenPitching.xlsx')
GuardiansPitching=pd.read_excel('GuardiansPitching.xlsx')



if option=='味全龍':
    st.subheader("折線圖")
    chart_data = pd.DataFrame(pd.read_excel("BrothersBatting.xlsx"),
                             columns=['打擊率'],
                             
                         )
    st.line_chart(chart_data)
st.header('投手成績')
st.write(BrothersPitching)
st.header('數據分析')
plt.style.use("ggplot")
plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-' ,color='yellow')
plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-' ,color='darkorange')
plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, '.-',color='red')
plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率,'.-', color='darkblue')
plt.plot(RakutenPitching.年度, RakutenPitching.防禦率,'.-', color='maroon')
plt.xlabel('Season') # 設定x軸標題
plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
plt.xticks(BrothersPitching.年度) # 設定x軸
plt.xticks(UnilionsPitching.年度) 
plt.xticks(RakutenPitching.年度) 
plt.xticks(GuardiansPitching.年度)
plt.xticks(DragonsPitching.年度) 
plt.title('CTBC Brothers Pitching ERA VS Other Teams ') # 設定圖表標題
plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
st.pyplot(plt)
  



