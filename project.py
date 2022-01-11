import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import base64
file_ = open("rr.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="rr gif">',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
col1.metric("季冠軍🏆", "1  次")
col2.metric("年度冠軍🏆", "10  次")
labels = 'Home Win', 'Away Win','Home Lose', 'Away Lose','Home Tie', 'Away Tie'
sizes = [11, 15, 18, 13,1,2]
explode = (0,0,0.2 ,0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
	shadow=True, startangle=90,textprops = {"fontsize" : 7})
plt.title("Pie chart of 2021 Full Year Record", {"fontsize" : 18})
plt.legend(loc = "best")   
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
     np.random.randn(1, 2) /[50, 50]+[24.19971, 120.68533],
     columns=['lat', 'lon'])

st.map(df)
