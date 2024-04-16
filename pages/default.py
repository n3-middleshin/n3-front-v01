import streamlit as st
from auth import set_user_menu, get_username 
from service import post, get 

set_user_menu() 

st.title("This page is Default Page")
st.markdown(f"You are currently logged with the role of {get_username()}.")

import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['아이디','이메일','사용여부'])

button_user = st.button("사용자 조회")

if button_user : 
    response =get("http://localhost:8000/users", 
                  {"param1":"value1"}, 
                  {"Content-Type": "application/json"})
    # st.write(response)
    df = pd.json_normalize(response)
    df = df[['id', 'email', 'is_active']] ## 특정칼럼만 적용할거다..
    # st.write(df)

edited_df = st.data_editor(
    data=df, 
    column_config={
        "id": st.column_config.Column(
            label="아이디"
        ), 
        "email": st.column_config.Column(label="이메일"), 
        "is_active" : st.column_config.Column(label="사용여부")
    }
)




    # response =get("http://localhost:8000/users", 
    #               {"param1":"value1"}, 
    #               {"Content-Type": "application/json"})
    # # viewer.dataframe(response)
    # # st.write(response.json())
    # json_data = pd.json_normalize(response)
    # st.data_editor(json_data)


    # print(response)


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