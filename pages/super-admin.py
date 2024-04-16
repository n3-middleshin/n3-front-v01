import streamlit as st

from auth import set_user_menu, get_username 
set_user_menu() 

st.title("This page is Super-admin page ")
st.markdown(f"You are currently logged with the role of {get_username()}.")
del_button = st.button("delete")

if del_button : 
    pass 
    # del_token() 

