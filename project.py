
import streamlit as st
st.subheader('1.讀入資料')
df = pd.read_csv('https://github.com/kuande122/project/blob/main/2020.csv')
st.dataframe(df)
