import streamlit as st
from streamlit_local_storage import LocalStorage
from datetime import datetime 

ls = LocalStorage()
token_key = "mytoken"

def set_user(email, username, token): 

    if "email" not in st.session_state : 
        st.session_state["email"] = email 

    if "username" not in st.session_state : 
        st.session_state["username"] = username
    
    ## token update 
    ls.setItem(token_key, token)
    # ls.refreshItems()

def get_username(): ## get_user_info(name:str)으로 대체할 예정임. 
    if "username" not in st.session_state : 
        return None 
    else : 
        return st.session_state.username 

def is_valid_user() : 
    
    token:str = ls.getItem(token_key) #token is valid check 
    if token : 
        print(datetime.now())
        print(" token is " + token)
        return True 
    return False

def del_token() : 
    ls.deleteAll()
    # ls.deleteItem(token_key, "deleteItem")
 
def set_user_menu():    
    # if is_valid_user() == False : 
        # login()
        # st.stop() 
        # st.switch_page("app.py")
    # userInfo = isValidUser() 
    
    # st.slider.write(userInfo.username)
    # isValidUser() # 로그인 정보가 없으면 login 화면으로 이동한다. 

    # st.cache_data 
    with st.sidebar: 
        st.page_link("pages/gpt_chat_prompt.py", label="Langchain GPT Chat Prompt")
        st.page_link("pages/gpt_pdf_embedding.py", label="Langchain GPT PDF Embedding")
        # st.page_link("pages/gpt_sql_search.py", label="Langchain SQL Search")
        st.page_link("pages/default.py", label="Your profile")
        st.page_link("pages/admin.py", label="Manage users")
        st.page_link("pages/super-admin.py", label="Manage admin access" )
        st.page_link("app.py", label="Login")


def login_form() : 

    ## menu setting 
    set_user_menu() 

    # login form setting 

    st.title("N3Cloud & Naver Clova-X Demo")
    st.write("")
    col1, col2, col3  = st.columns([2, 1, 1])
    login_form= col1.form("login_form")
    login_form.subheader("Login page")

    useremail = login_form.text_input("User-Email", placeholder="mymail@example.com")
    password = login_form.text_input("Password", type="password")
    submitted = login_form.form_submit_button("로그인", use_container_width=False)

    if submitted : 
        if useremail and password: 
            pass         