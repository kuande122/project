import streamlit as st
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
from PIL import Image

option = st.sidebar.selectbox( '選擇球隊？', ['中信兄弟', '統一7-Eleven獅', '味全龍', '樂天桃猿','富邦悍將'])
option1 = st.sidebar.selectbox( '選擇所想查看的數據？', ['球隊成績', '投手成績', '打擊成績', '守備成績'])
if option == '中信兄弟':
  image = Image.open('brothers.png')
  st.image(image)
  if option1=='球隊成績':
    st.write('##球隊成績')
    b=pd.read_excel('b.xlsx')
    st.write(b) 
  elif option1=='投手成績':
    st.write('##投手成績')
    bp=pd.read_excel('bp.xlsx')
    st.write(bp)   
  elif option1=='打擊成績':
    st.write('##打擊成績')
    bt=pd.read_excel('bt.xlsx')
    st.write(bt) 
  else:
    st.write('##守備成績')
    bc=pd.read_excel('bc.xlsx')
    st.write(bc)   
    
elif option == '統一7-Eleven獅':
  image = Image.open('unilion.png')
  st.image(image)
  st.write('投手成績')
  lp = pd.read_excel('lp.xlsx')
  st.write(lp)
elif option == '味全龍':
  image = Image.open('Dragons.png')
  st.image(image)
elif option == '樂天桃猿':
  image = Image.open('Rakuten.png')
  st.image(image)
elif option == '富邦悍將':
  image = Image.open('guardians.png')
  st.image(image)

