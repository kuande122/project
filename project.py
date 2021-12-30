import streamlit as st  
from st_aggrid import AgGrid
import pandas as pd
data = pd.read_csv('2020.csv')
st.write("## THE DATA BEING USED")
data
