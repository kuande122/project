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
 st.write('營運管理：富邦金控')
 st.write('管理與維護：富邦運動場館股份有限公司')
 st.write('營運與使用：富邦育樂股份有限公司')

with col2:
 # add marker for Liberty Bell
 m = folium.Map(location=[25.04054,121.44768], zoom_start=20)
 tooltip = "新北新莊棒球場"
 folium.Marker([25.04054,121.44768], popup="新北市立新莊棒球場", tooltip=tooltip
    ).add_to(m)

 # call to render Folium map in Streamlit
 folium_static(m)
col1, col2 = st.columns(2)
with col1:
 image = Image.open('新莊全景.jpg')
 st.image(image)
with col2:
 image = Image.open('新莊棒球場座位圖.jpg')
 st.image(image)


m1 = folium.Map(location=[24.19978, 120.68498], zoom_start=16)

 # add marker for Liberty Bell
tooltip = "臺中洲際棒球場"
folium.Marker([24.19978, 120.68498], popup="臺中洲際棒球場", tooltip=tooltip
    ).add_to(m1)

 # call to render Folium map in Streamlit
folium_static(m1)
m2 = folium.Map(location=[25.00054,121.20038], zoom_start=16)

 # add marker for Liberty Bell
tooltip = "桃園國際棒球場"
folium.Marker([25.00054,121.20038], popup="桃園國際棒球場", tooltip=tooltip
    ).add_to(m2)

 # call to render Folium map in Streamlit
folium_static(m2)
m3 = folium.Map(location=[22.98043, 120.2062], zoom_start=16)

 # add marker for Liberty Bell
tooltip = "臺南市立棒球場"
folium.Marker([22.98043, 120.2062], popup="臺南市立棒球場", tooltip=tooltip
    ).add_to(m3)

 # call to render
folium_static(m3)

m4 = folium.Map(location=[23.7171965, 120.5362392], zoom_start=16)

 # add marker for Liberty Bell
tooltip = "雲林斗六棒球場"
folium.Marker([23.7171965, 120.5362392], popup="雲林斗六棒球場", tooltip=tooltip
    ).add_to(m4)

 # call to render
folium_static(m4)


m5 = folium.Map(location=[25.11374, 121.53345], zoom_start=16)

 # add marker for Liberty Bell
tooltip = "臺北天母棒球場"
folium.Marker([25.11374, 121.53345], popup="臺北天母棒球場", tooltip=tooltip
    ).add_to(m5)

 # call to render
folium_static(m5)
