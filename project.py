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
    UnilionsPitching=pd.read_excel('UnilionsPitching.xlsx')
    DragonsPitching=pd.read_excel('DragonsPitching.xlsx')
    RakutenPitching=pd.read_excel('RakutenPitching.xlsx')
    GuardiansPitching=pd.read_excel('GuardiansPitching.xlsx')
    st.write(BrothersPitching)
    st.header('數據分析')
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-' ,color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-' ,color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, '.-',color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率,'.-', color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率,'.-', color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersPitching.年度, [2014,2015,2016,2017,2018,2019,2020,2021]) # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsPitching.年度,[2014,2015,2016,2017,2018,2019,2020,2021] ) # 設定x軸label以及垂直顯示
    plt.xticks(RakutenPitching.年度,[2014,2015,2016,2017,2018,2019,2020,2021]) # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansPitching.年度, [2014,2015,2016,2017,2018,2019,2020,2021]) # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsPitching.年度, [2014,2015,2016,2017,2018,2019,2020,2021]) # 會影響x座標軸數值更動
    plt.title('CTBC Brothers Pitching Era VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)                 
  elif option1=='打擊成績':
    st.header('打擊成績')
    BrothersBatting=pd.read_excel('BrothersBatting.xlsx')
    UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
    DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
    RakutenBatting=pd.read_excel('RakutenBatting.xlsx')
    GuardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
    st.write(BrothersBatting)
    st.header('數據分析')
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率, color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率, color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsBatting.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('CTBC Brothers Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
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
    BrothersPitching=pd.read_excel('BrothersPitching.xlsx')
    UnilionsPitching=pd.read_excel('UnilionsPitching.xlsx')
    DragonsPitching=pd.read_excel('DragonsPitching.xlsx')
    RakutenPitching=pd.read_excel('RakutenPitching.xlsx')
    GuardiansPitching=pd.read_excel('GuardiansPitching.xlsx')
    st.write(UnilionsPitching)
    st.header('數據分析')
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率, color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率, color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率, color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsPitching.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('Unilions Pitching Era VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)                
  elif option1=='打擊成績':
    st.header('打擊成績')
    BrothersBatting=pd.read_excel('BrothersBatting.xlsx')
    UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
    DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
    RakutenBatting=pd.read_excel('RakutenBatting.xlsx')
    GuardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
    st.write(UnilionsBatting) 
    st.header('數據分析')
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率, color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率, color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsBatting.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('Unilions Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
 
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
    BrothersPitching=pd.read_excel('BrothersPitching.xlsx')
    UnilionsPitching=pd.read_excel('UnilionsPitching.xlsx')
    DragonsPitching=pd.read_excel('DragonsPitching.xlsx')
    RakutenPitching=pd.read_excel('RakutenPitching.xlsx')
    GuardiansPitching=pd.read_excel('GuardiansPitching.xlsx')
    st.write(DragonsPitching)
    st.header('數據分析')
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率, color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率, color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率, color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsPitching.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('Dragons Pitching Era VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    BrothersBatting=pd.read_excel('BrothersBatting.xlsx')
    UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
    DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
    RakutenBatting=pd.read_excel('RakutenBatting.xlsx')
    GuardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
    st.write(DragonsBatting) 
    st.header('數據分析')
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率, color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率, color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsBatting.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('Dragons Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
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
    BrothersPitching=pd.read_excel('BrothersPitching.xlsx')
    UnilionsPitching=pd.read_excel('UnilionsPitching.xlsx')
    DragonsPitching=pd.read_excel('DragonsPitching.xlsx')
    RakutenPitching=pd.read_excel('RakutenPitching.xlsx')
    GuardiansPitching=pd.read_excel('GuardiansPitching.xlsx')
    st.write(RakutenPitching)
    st.header('數據分析')
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率, color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率, color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率, color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsPitching.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('Rakuten Pitching Era VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)   
  elif option1=='打擊成績':
    st.header('打擊成績')
    BrothersBatting=pd.read_excel('BrothersBatting.xlsx')
    UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
    DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
    RakutenBatting=pd.read_excel('RakutenBatting.xlsx')
    GuardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
    st.write(RakutenBatting) 
    st.header('數據分析')
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率, color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率, color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsBatting.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('Rakuten Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
   
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
    BrothersPitching=pd.read_excel('BrothersPitching.xlsx')
    UnilionsPitching=pd.read_excel('UnilionsPitching.xlsx')
    DragonsPitching=pd.read_excel('DragonsPitching.xlsx')
    RakutenPitching=pd.read_excel('RakutenPitching.xlsx')
    GuardiansPitching=pd.read_excel('GuardiansPitching.xlsx')
    st.write(GuardiansPitching)
    st.header('數據分析')
    plt.plot(BrothersPitching.年度, BrothersPitching.防禦率, color='yellow')
    plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率, color='darkorange')
    plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, color='red')
    plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率, color='darkblue')
    plt.plot(RakutenPitching.年度, RakutenPitching.防禦率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansPitching.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsPitching.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('Guardians Pitching Era VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    st.pyplot(plt)       
  elif option1=='打擊成績':
    st.header('打擊成績')
    BrothersBatting=pd.read_excel('BrothersBatting.xlsx')
    UnilionsBatting=pd.read_excel('UnilionsBatting.xlsx')
    DragonsBatting=pd.read_excel('DragonsBatting.xlsx')
    RakutenBatting=pd.read_excel('RakutenBatting.xlsx')
    GuardiansBatting=pd.read_excel('GuardiansBatting.xlsx')
    st.write(GuardiansBatting) 
    st.header('數據分析')
    plt.plot(BrothersBatting.年度, BrothersBatting.打擊率, color='yellow')
    plt.plot(UnilionsBatting.年度, UnilionsBatting.打擊率, color='darkorange')
    plt.plot(DragonsBatting.年度, DragonsBatting.打擊率, color='red')
    plt.plot(GuardiansBatting.年度, GuardiansBatting.打擊率, color='darkblue')
    plt.plot(RakutenBatting.年度, RakutenBatting.打擊率, color='maroon')
    plt.xlabel('Season') # 設定x軸標題
    plt.xticks(BrothersBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(UnilionsBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(RakutenBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    plt.xticks(GuardiansBatting.年度, rotation='vertical') # 設定x軸label以及垂直顯示
    #plt.xticks(DragonsBatting.年度, rotation='vertical') # 會影響x座標軸數值更動
    plt.title('Guardians Batting Avg VS Other Teams ') # 設定圖表標題
    plt.legend(labels=["BrothersBatting", "UnilionsBatting","DragonsBatting","GuardiansBatting","RakutenBatting"], loc = 'best')
    st.pyplot(plt)
  else:
    st.header('守備成績')
    GuardiansDefense=pd.read_excel('GuardiansDefense.xlsx')
    st.write(GuardiansDefense)  

