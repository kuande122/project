import streamlit as st
from streamlit_folium import folium_static
import folium
from PIL import Image 
 # center on Liberty Bell
col1, col2 = st.columns(2)
with col1:
 st.header('新北新莊棒球場')
 st.write('全名：新北市立新莊棒球場（XinZhuang Baseball Stadium）')
 st.write('地址：新北市新莊區立德里和興街66號')
 st.write('草皮：天然草皮（百慕達草）')
 st.write('螢幕：外野：LED大螢幕（左）、LED螢幕（右）內野：環狀屏LED')
 st.write('觀眾席數：12,150人 內野數：8,150人 外野數：4,000人')
 st.write('全壘打牆距離：左外野：325英呎 中外野：400英呎 右外野：325英呎')
 
with col2:
 # add marker for Liberty Bell
 m = folium.Map(location=[25.04054,121.44768], zoom_start=20)
 tooltip = "新北新莊棒球場"
 folium.Marker([25.04054,121.44768], popup="新北市立新莊棒球場", tooltip=tooltip
    ).add_to(m)

 # call to render Folium map in Streamlit
 folium_static(m)
with col1:
 image = Image.open('123.png')
 st.image(image)
with col2:
 image = Image.open('Rakuten.png')
 st.image(image)
