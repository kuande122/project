pip install streamlit
import streamlit as st
st.subheader('1.讀入資料')
df = pd.read_csv('2020.csv')
st.dataframe(df)
