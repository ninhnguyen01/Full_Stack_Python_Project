# Listing 1.1 Using tabs in Streamlit

import streamlit as st

tab1, tab2, tab3 = st.tabs(["Mission", "About Us", "Career"])

with tab1:
    st.header("Our Mission")
    st.write("Our Mission is to teach people to make web apps in Python.")

with tab2:
    st.header("About Us")
    st.write("We are a group of Python enthusiasts.")

with tab3:
    st.header("Careers")
    st.write("We are hiring! Apply today!")
    
# In terminal or command line (depending on your OS), enter "streamlit run filename.py"
# The file "filename.py" is a placeholder example of whatever your python file name is.
# If error, check Streamlit documentation on their website.
# Website Link (Last updated: July 6, 2026): https://docs.streamlit.io/get-started/tutorials/create-an-app

