import streamlit as st
# Import the pages
from my_pages import (
    page_Home as home,
    page_California_Housing_Prices as page1,
    page_Location_Information as page2,
    page_Weather_Information as page3,
)

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select a page",
    [
        "🏠 Home",
        "🏡 California Housing Prices",
        "🌍 Location Information",
        "☀️ Weather Information",
    ]
)

if page == "🏠 Home":
    home.home()
elif page == "🏡 California Housing Prices":
    page1.page1()
elif page == "🌍 Location Information":
    page2.page2()
elif page == "☀️ Weather Information":
    page3.page3()