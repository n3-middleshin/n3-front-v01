import streamlit as st
from pages.main import set_menu 
from auth import get_username 

set_menu() # init or refresh sidebar menu 

st.title("This page is Default Page")
st.markdown(f"You are currently logged with the role of {get_username()}.")
st.markdown(f"You are currently logged with the role of {get_username()}.")
st.markdown(f"You are currently logged with the role of {get_username()}.")
st.markdown(f"You are currently logged with the role of {get_username()}.")
st.markdown(f"You are currently logged with the role of {get_username()}.")
st.markdown(f"You are currently logged with the role of {get_username()}.")
st.markdown(f"You are currently logged with the role of {get_username()}.")

# st.sidebar.page_link("pages/user.py", label="Your profile")
# st.sidebar.page_link("app.py", label="Logout")
