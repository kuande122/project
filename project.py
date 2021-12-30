import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image
data = pd.read_csv('2020.csv')
st.write("## THE DATA BEING USED")
data
selected_data = st.selectbox('Select a Player', options=records,
        format_func=lambda record: f'{record["full_name"]}')
