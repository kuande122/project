import streamlit as st
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
from PIL import Image
st.set_page_config(
    page_title="猛祺的期末報告",
    page_icon="st.image(phil)",
    phil = Image.open('phil.jpg')
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
    bp=pd.read_excel('bp.xlsx')
    st.write(bp)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    bt=pd.read_excel('bt.xlsx')
    st.write(bt) 
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
  
elif option == '樂天桃猿':
  image = Image.open('Rakuten.png')
  st.image(image)
  
  
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

