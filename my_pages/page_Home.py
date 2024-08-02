import streamlit as st

def home():
    """Homepage renderer."""
    st.title("Welcome to the Streamlit App")
    st.write("""
        ## Introduction
        Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.
        Setting up our first APP.
    """)


if __name__ == "__main__":
    home()
