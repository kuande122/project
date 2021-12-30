import streamlit as st  
from st_aggrid import AgGrid
import pandas as pd
st.sucess('如以下這是你的表格')
df=pd.read_csv('2020.csv')
AgGrid(df)
