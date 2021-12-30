import csv
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
from statsmodels.nonparametric.smoothers_lowess import lowess
st.subheader('1.讀入資料')
df = pd.read_csv('https://github.com/kuande122/project/blob/main/2020.csv')
st.dataframe(df)
