import streamlit as st 
import os  
os.system("cls")  ## console clear 

## 실행 시 parameter를 받는다. 운영/개발에 대한 구분으로 사용된다. 띄어쓰기로 구분한다. 
# streamlit run app.py dev || -prod 
import sys

if __name__ == '__main__': 
    if len(sys.argv) < 2:
        print("Insufficient arguments")
        sys.exit()

    print(sys.argv[0]) # 첫번째 parameter 
    print(sys.argv[1]) # 두번째 parameter 
    # print(sys.argv[2]) # 세번째 parameter 


## app.py에서 한번만 호출한다. 
st.set_page_config(
    page_title="N3Demo page", 
    page_icon="🧊",
    layout="wide", 
    menu_items={
    'About': 'N3Cloud - https://www.n3cloud.co.kr/', 
    # 'Streamlit': "https://streamlit.io/",
    # 'About': "# This is a header. This is an *extremely* cool app!" 
    }
)

# st.switch_page("login/login.py")
from auth import login_form
login_form() 


# if "role" in st.session_state:
#     del st.session_state["role"]


# Initialize st.session_state.role to None
# if "role" not in st.session_state:
#     st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
## 초기값 설정이다. 
# st.session_state._role = st.session_state.role

# def set_role():
#     print("role is " + st.session_state._role )
#     # Callback function to save the role selection to Session State
#     st.session_state.role = st.session_state._role
#     menu()

# st.sidebar.page_link("app.py", label="Login")

# # Selectbox to choose role
# st.selectbox(
#     "Select your role:",
#     [None, "user", "admin", "super-admin"],
#     key="_role", ## session_state로 바로 저장된다. 
#     on_change=set_role, #상태가 변경되고 제일 하단의 menu()를 호출한다. (menu.py에 함수가 선언되어 있다. )
# )

# if "role" in st.session_state:
#     menu() # Render the dynamic menu!



