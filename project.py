import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image
data = pd.read_csv('2020.csv')
st.write("## THE DATA BEING USED")
data
option = st.selectbox( '選擇球隊？', ['中信兄弟', '統一7-Eleven獅', '味全龍', '樂天桃猿','富邦悍將'])
if option ==中信兄弟
  st.image(Cpbl-stats-chinatrust-brothers.png)
