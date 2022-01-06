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

if option == '中信兄弟':
  image = Image.open('brothers.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    Brothers=pd.read_excel('Brothers.xlsx')
    st.write(Brothers) 
  elif option1=='投手成績':
    st.header('投手成績')
    BrothersPitching=pd.read_excel('BrothersPitching.xlsx')
    st.write(BrothersPitching)                  
  elif option1=='打擊成績':
    st.header('打擊成績')
    BrothersBatting=pd.read_excel('BrothersBatting.xlsx')
    UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
    DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
    st.write(BrothersBatting) 
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率, color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, color='red')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(DragonsBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.title('CTBC Brothers Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting"], loc = 'best')
    st.pyplot(plt)
    
  else:
    st.header('守備成績')
    BrothersDefense=pd.read_excel('BrothersDefense.xlsx')
    st.write(BrothersDefense)   
    
elif option == '統一7-Eleven獅':
  image = Image.open('unilion.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    Unilions=pd.read_excel('Unilions.xlsx')
    st.write(Unilions) 
  elif option1=='投手成績':
    st.header('投手成績')
    UnilionsPitching=pd.read_excel('UnilionsPitching.xlsx')
    st.write(UnilionsPitching)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
    st.write(UnilionsBatting) 
  else:
    st.header('守備成績')
    UnilionsDefense=pd.read_excel('UnilionsDefense.xlsx')
    st.write(UnilionsDefense) 
    
elif option == '味全龍':
  image = Image.open('Dragons.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    Dragons=pd.read_excel('Dragons.xlsx')
    st.write(Dragons) 
  elif option1=='投手成績':
    st.header('投手成績')
    DragonsPitching=pd.read_excel('DragonsPitching.xlsx')
    st.write(DragonsPitching)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
    st.write(DragonsBatting) 
  else:
    st.header('守備成績')
    DragonsDefense=pd.read_excel('DragonsDefense.xlsx')
    st.write(DragonsDefense)  
  
elif option == '樂天桃猿':
  image = Image.open('Rakuten.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    Rakuten=pd.read_excel('Rakuten.xlsx')
    st.write(Rakuten) 
  elif option1=='投手成績':
    st.header('投手成績')
    RakutenPitching=pd.read_excel('RakutenPitching.xlsx')
    st.write(RakutenPitching)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    RakutenBatting=pd.read_excel('RakutenBatting.xlsx')
    st.write(RakutenBatting) 
  else:
    st.header('守備成績')
    RakutenDefense=pd.read_excel('RakutenDefense.xlsx')
    st.write(RakutenDefense)  
  
elif option == '富邦悍將':
  image = Image.open('guardians.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    Guardians=pd.read_excel('Guardians.xlsx')
    st.write(Guardians) 
  elif option1=='投手成績':
    st.header('投手成績')
    GuardiansPitching=pd.read_excel('GuardiansPitching.xlsx')
    st.write(GuardiansPitching)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    GuardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
    st.write(GuardiansBatting) 
  else:
    st.header('守備成績')
    GuardiansDefense=pd.read_excel('GuardiansDefense.xlsx')
    st.write(GuardiansDefense)  

