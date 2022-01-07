import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

labels = 'Home Win', 'Away Win','Home Lose', 'Away Lose','Home Tie', 'Away Tie'
sizes = [11, 15, 18, 13,1,2]
explode = (0,0,0.1 ,0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
	shadow=True, startangle=90)
plt.legend(loc = "best")   
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
