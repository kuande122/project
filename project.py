import streamlit as st
from streamlit_folium import folium_static
import folium
 # center on Liberty Bell
m = folium.Map(location=[25.04054,121.44768], zoom_start=16)

 # add marker for Liberty Bell
tooltip = "新北新莊棒球場"
folium.Marker([25.04054,121.44768], popup="新北新莊棒球場", tooltip=tooltip
    ).add_to(m)

 # call to render Folium map in Streamlit
folium_static(m)
m1 = folium.Map(location=[24.19978, 120.68498], zoom_start=16)

 # add marker for Liberty Bell
tooltip = "台中洲際棒球場"
folium.Marker([24.19978, 120.68498], popup="台中洲際棒球場", tooltip=tooltip
    ).add_to(m)

 # call to render Folium map in Streamlit
folium_static(m)
