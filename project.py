import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image
import matplotlib
option = st.sidebar.selectbox( '選擇球隊？', ['中信兄弟', '統一7-Eleven獅', '味全龍', '樂天桃猿','富邦悍將'])
if option == '中信兄弟':
  image = Image.open('brothers.png')
  st.image(image)
  st.write('兄弟象(1990-2013)–中信兄弟(2014-至今)')
elif option == '統一7-Eleven獅':
  image = Image.open('unilion.png')
  st.image(image)
elif option == '味全龍':
  image = Image.open('Dragons.png')
  st.image(image)
elif option == '樂天桃猿':
  image = Image.open('Rakuten.png')
  st.image(image)
elif option == '富邦悍將':
  image = Image.open('guardians.png')
  st.image(image)

df = pd.read_excel("wang.xlsx") 
plt.plot(年度, 打擊率, color='b')
plt.xlabel('year') # 設定x軸標題
plt.xticks(打擊率, rotation='vertical') # 設定x軸label以及垂直顯示
plt.title('Wang') # 設定圖表標題
plt.show()
