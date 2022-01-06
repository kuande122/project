import streamlit as st
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
from PIL import Image
wang = pd.read_excel('wang.xlsx')
st.write(wang)    # 顯示前3筆資料
ym = [None] * len(wang["年度"])     # 建立一個空列表，數量為年月的數量

# 以for迴圈逐一將年月資料類別轉成字串類別
for i in range(len(wang["年度"])):  
    ym[i] = str(wang["年度"][i])
    
["年度"] = ym  # 將原本年月欄位資料替換掉
plt.plot(wang.年度, wang.打擊率, color='b')
plt.xlabel('SEASON') # 設定x軸標題
plt.xticks(wang.SEASON_ID, rotation='vertical') # 設定x軸label以及垂直顯示
plt.title('wang') # 設定圖表標題
plt.show()
option = st.sidebar.selectbox( '選擇球隊？', ['中信兄弟', '統一7-Eleven獅', '味全龍', '樂天桃猿','富邦悍將'])
if option == '中信兄弟':
  image = Image.open('brothers.png')
  st.image(image)
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

