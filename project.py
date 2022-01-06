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
    b=pd.read_excel('b.xlsx')
    st.write(b) 
  elif option1=='投手成績':
    st.header('投手成績')
    BrothersPitching=pd.read_excel('BrothersPitching.xlsx')
    st.write(BrothersPitching)
                 
   
  elif option1=='打擊成績':
    st.header('打擊成績')
    bt=pd.read_excel('bt.xlsx')
    lt=pd.read_excel('lt.xlsx')
    st.write(bt) 
    plt.plot(bt.年度, bt.打擊率, color='y')
    plt.plot(lt.年度, lt.打擊率, color='b')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(bt.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(lt.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.title('CTBC Brothers Batting AVG VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["bt", "lt"], loc = 'best')
    st.pyplot(plt)
    
  else:
    st.header('守備成績')
    bc=pd.read_excel('bc.xlsx')
    st.write(bc)   
    
elif option == '統一7-Eleven獅':
  image = Image.open('unilion.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    l=pd.read_excel('l.xlsx')
    st.write(l) 
  elif option1=='投手成績':
    st.header('投手成績')
    lp=pd.read_excel('lp.xlsx')
    st.write(lp)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    lt=pd.read_excel('lt.xlsx')
    st.write(lt) 
  else:
    st.header('守備成績')
    lc=pd.read_excel('lc.xlsx')
    st.write(lc) 
    
elif option == '味全龍':
  image = Image.open('Dragons.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    w=pd.read_excel('w.xlsx')
    st.write(w) 
  elif option1=='投手成績':
    st.header('投手成績')
    wp=pd.read_excel('wp.xlsx')
    st.write(wp)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    wt=pd.read_excel('wt.xlsx')
    st.write(wt) 
  else:
    st.header('守備成績')
    wc=pd.read_excel('wc.xlsx')
    st.write(wc)  
  
elif option == '樂天桃猿':
  image = Image.open('Rakuten.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    r=pd.read_excel('r.xlsx')
    st.write(r) 
  elif option1=='投手成績':
    st.header('投手成績')
    rp=pd.read_excel('rp.xlsx')
    st.write(rp)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    rt=pd.read_excel('rt.xlsx')
    st.write(rt) 
  else:
    st.header('守備成績')
    rc=pd.read_excel('rc.xlsx')
    st.write(rc)  
  
elif option == '富邦悍將':
  image = Image.open('guardians.png')
  st.image(image)
  if option1=='球隊成績':
    st.header('球隊成績')
    g=pd.read_excel('g.xlsx')
    st.write(g) 
  elif option1=='投手成績':
    st.header('投手成績')
    gp=pd.read_excel('gp.xlsx')
    st.write(gp)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    gt=pd.read_excel('gt.xlsx')
    st.write(gt) 
  else:
    st.header('守備成績')
    gc=pd.read_excel('gc.xlsx')
    st.write(gc)  

