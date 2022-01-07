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
BrothersBatting=pd.read_excel('BrothersBatting.xlsx')
UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
RakutenBatting=pd.read_excel('RakutenBatting.xlsx')
GuardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
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
fig, (ax1, ax2) = plt.subplots(1, 2, sharex = True, sharey = True, figsize = (12, 4.5))

ax1.plt.style.use("ggplot")
ax1.plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-' ,color='yellow')
ax1.plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-' ,color='darkorange')
ax1.plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, '.-',color='red')
ax1.plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率,'.-', color='darkblue')
ax1.plt.plot(RakutenPitching.年度, RakutenPitching.防禦率,'.-', color='maroon')
ax1.plt.xlabel('Season') # 設定x軸標題
ax1.plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
ax1.plt.xticks(BrothersPitching.年度) # 設定x軸
ax1.plt.xticks(UnilionsPitching.年度) 
ax1.plt.xticks(RakutenPitching.年度) 
ax1.plt.xticks(GuardiansPitching.年度)
ax1.plt.xticks(DragonsPitching.年度) 
ax1.plt.title('CTBC Brothers Pitching ERA VS Other Teams ') # 設定圖表標題
ax1.plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
st.pyplot(ax1.plt)
st.header('數據分析')
ax2.plt.style.use("ggplot") 
ax2.plt.plot(BrothersBatting.年度, BrothersBatting.打擊率,'.-', color='yellow')
ax2.plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率,'.-', color='darkorange')
ax2.plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, '.-',color='red')
ax2.plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率,'.-', color='darkblue')
ax2.plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, '.-',color='maroon')
ax2.plt.xlabel('Season') # 設定x軸標題
ax2.plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
ax2.plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
ax2.plt.xticks(UnilionsBatting.年度) 
ax2.plt.xticks(RakutenBatting.年度) 
ax2.plt.xticks(GuardiansBatting.年度) 
ax2.plt.xticks(DragonsBatting.年度) 
ax2.plt.title('CTBC Brothers Batting Avg VS Other Teams ') # 設定圖表標題
ax2.plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
st.pyplot(ax2.plt)
    



