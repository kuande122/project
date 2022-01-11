import streamlit as st
import folium # 匯入 folium 套件

import datetime

unsafe_allow_html=True

# 建立地圖與設定位置
fmap = folium.Map(location=[35.709635, 139.810851], zoom_start=16)
fmap  # 在notebook中顯示地圖
