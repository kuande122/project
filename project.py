import streamlit as st
from streamlit_folium import folium_static
import folium
 # center on Liberty Bell
m = folium.Map(location=[25.04054,121.44768], zoom_start=16)

 # add marker for Liberty Bell
tooltip = "全富武裝"
folium.Marker([25.04054,121.44768], popup="全富武裝", tooltip=tooltip
    ).add_to(m)

 # call to render Folium map in Streamlit
folium_static(m)
