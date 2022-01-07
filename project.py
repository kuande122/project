import streamlit as st
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt
import plotly.express as px# 資料視覺化套件
import xlrd
from PIL import Image
st.set_page_config(
    page_title="猛祺的期末報告",
    page_icon='phil.ico'
    )
st.title('中華職棒數據查詢系統')
st.sidebar.header('選擇球隊及數據')



import streamlit as st
import pandas as pd
import plotly.express as px

# continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
df = pd.DataFrame(
    [["2021", 1080, 77], ["2020", 1319, 143],["2019",1168,148],["2018",1152,91],["2017",1214,145],["2016",1460,169],
     ["2015",1308,90],["2014",1083,52]],
    columns=["Year", "Hit", "Homerun"]
)

fig = px.bar(df, x="Year", y=["Hit", "Homerun"], barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)


































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

plt.tight_layout()
st.header('投手成績')
st.write(BrothersPitching)
st.header('數據分析')
plt.subplot(2, 1 ,1)
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
plt.title('CTBC Brothers Pitching ERA VS Other Teams ',{'fontsize':10}) # 設定圖表標題
plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
st.pyplot(plt)
x=st.button('點取看更多分析')
if x:
    plt.subplot(2, 1 ,2)
    plt.style.use("ggplot") 
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率,'.-', color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率,'.-', color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, '.-',color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率,'.-', color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, '.-',color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(BrothersBatting.年度) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度) 
    plt.xticks(RakutenBatting.年度) 
    plt.xticks(GuardiansBatting.年度) 
    plt.xticks(DragonsBatting.年度) 
    plt.title('CTBC Brothers Batting Avg VS Other Teams ',{'fontsize':10}) # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
    plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=15.0, 
                    hspace=15.0)



