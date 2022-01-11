import setuptools

setuptools.setup(
    name="streamlit_folium",
    version="0.4.0",
    author="Randy Zwitch",
    author_email="randy@streamlit.io",
    description="Render Folium objects in Streamlit",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/randyzwitch/streamlit-folium",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=["streamlit>=0.79", "folium>=0.11"],
)




import streamlit as st

st.set_page_config(page_title="streamlit-folium documentation")

"# streamlit-folium"

with st.echo():

    import streamlit as st
    from streamlit_folium import folium_static
    import folium

    page = st.radio("Select map type", ["Single map", "Dual map"], index=0)

    # center on Liberty Bell
    if page == "Single map":
        m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    elif page == "Dual map":
        m = folium.plugins.DualMap(location=[39.949610, -75.150282], zoom_start=16)

    # add marker for Liberty Bell
    tooltip = "Liberty Bell"
    folium.Marker(
        [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)

