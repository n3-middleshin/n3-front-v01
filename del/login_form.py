import streamlit as st
from  auth import set_user_menu

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
    # 정상 로그인인 경우 default 페이지로 이동한다. 
    # 각각의 페이지에서 메뉴를 설정한다. #(main() 함수 호출)

        # set_user("username", useremail, "my-jwt-token")
        # st.switch_page("pages/default.py")


    # if submitted : 
    #     if username : 
    #         response =service("http://localhost:8000/auth/login",
    #                           {"username": username, "password": password},
    #                           {"Content-Type": "application/json"})

    #         os.system("cls")
    #         print(response.get("username"))
    #         print(response.get("token"))
    #         print(response.get("role"))
    #         # response_headers = _get_websocket_headers()
    #         token = response.get("token")
    #         # st.session_state.role = st.session_state._role

    #         # if token : 
    #         #     st.session_state.role = "admin"
    #         # else :
    #         #     del st.session_state.role  

    #         # access_token = response_headers.get("X-Process-Time")
    #         # st.toast("response time is " + access_token) 
    #         st.toast("response is : " + response["username"], icon='😍' ) 



    # localS = LocalStorage()
    # my_token = "X-my-token"
    # # local_storage_item = localS.getItem(itemKey) 

    # myRole:str = localS.getItem(my_token)



    # myRoleString:str = ''.join(list(myRole)) 

    # print("my roleString is " + myRoleString)

    # # print(type(myRole))

    # # if myRole : 
    # if "role" not in st.session_state : 
    #     st.session_state["role"] = myRole 
    
    # # itemValue = "Tarah-middleshin"
    # # localS.setItem(itemKey, itemValue)

    # #localS.deleteAll()

    
    # st.sidebar.page_link("app.py", label="Login")

    # def set_role():
    #     st.write("role is " + st.session_state.role )
        # localS.setItem(itemKey, st.session_state.role) 
        # Callback function to save the role selection to Session State
        # st.session_state.role = st.session_state._role
        # menu()


    # Selectbox to choose role
    # st.selectbox(
    #     "Select your role:",
    #     [None, "user", "admin", "super-admin"],
    #     key="role", ## session_state로 바로 저장된다. 
    #     on_change=set_role, #상태가 변경되고 제일 하단의 menu()를 호출한다. (menu.py에 함수가 선언되어 있다. )
    # )



    # username = login_form.text_input("User-Email")
    # password = login_form.text_input("Password", type="password")

    # submitted = login_form.form_submit_button("로그인", use_container_width=False)
    # if submitted : 
    #     if username : 
    #         response =service("http://localhost:8000/auth/login",
    #                           {"username": username, "password": password},
    #                           {"Content-Type": "application/json"})

    #         os.system("cls")
    #         print(response.get("username"))
    #         print(response.get("token"))
    #         print(response.get("role"))
    #         # response_headers = _get_websocket_headers()
    #         token = response.get("token")
    #         # st.session_state.role = st.session_state._role

    #         # if token : 
    #         #     st.session_state.role = "admin"
    #         # else :
    #         #     del st.session_state.role  

    #         # access_token = response_headers.get("X-Process-Time")
    #         # st.toast("response time is " + access_token) 
    #         st.toast("response is : " + response["username"], icon='😍' )       



                
