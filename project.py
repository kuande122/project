import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
win = ['Home Win', 'Away Win', 'Home Lose', 'Away Lose','Home Tie', 'Away Tie']
wind = [11, 15, 18, 13,1,2]
data={"win":win
      ,"wind":wind}
df = pd.DataFrame(win)
df
explode = [0.2, 0, 0, 0,0]
fig ,ax = plt.subplots(figsize=(12,8))
ax.pie(wind,
      labels=win,
      autopct='%.1f%%', # 比例格式
      
     
      ), # 陰影
ax.set_title("haha",fontsize=20)
ax.legend(win, loc=3, fontsize='small')
st.pyplot(plt)


