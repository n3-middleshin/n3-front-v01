import streamlit as st
from auth import set_user_menu
import requests
import time

set_user_menu() 
st.sidebar.divider()

if 'recipe_msg' not in st.session_state:
    st.session_state["recipe_msg"] = None

if 'text_key' not in st.session_state:
    st.session_state["text_key"] = None

def set_recipe_text():
    st.session_state["recipe_msg"] = "너는 요리사야. 내가 가진 재료들을 가지고 만들수 있는 요리를 추천하고, 그 요리의 레시피를 알려줘. 내가 가진 재료는 입력할게." 

def set_peot_text(): 
    st.session_state["recipe_msg"] = """삼행시는 글자 3개로 시를 만드는 거야, 예제는 아래 내용을 참고해 

질문1  : 아이유로 3행시 만들어줘. 
답변1 : 
아: 아이유는
이: 이런 강의를 들을 이
유: 유가 없다.

질문2: 김민수로 삼행시 만들어줘
답변2 : 
김: 김치는 맛있다
민: 민달팽이도 좋아하는 김치!
수: 수억을 줘도 김치는 내꺼!

답변할때는 각 글자마다 행바꿈을 넣어줘. 
"""

def refresh_message():
    st.session_state["recipe_msg"] = st.session_state['text_key']

system_prompt = st.sidebar.text_area("💬 AI System Prompt", 
                    value=st.session_state["recipe_msg"], 
                    placeholder= "system prompt를 입력해 주세요.", 
                    on_change=refresh_message, 
                    key='text_key', 
                    height=200)



col1, col2, col3 = st.sidebar.columns(3) 
col1.button("레시피 알려줘.", on_click=set_recipe_text) # if 문을 사용할 경우 조금 늦는거 같기는 하네..
col2.button("삼행시 지어줘.", on_click=set_peot_text) # if 문을 사용할 경우 조금 늦는거 같기는 하네..

st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "오늘은 무엇을 도와드릴까요? :keycap_star::seven: "}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # system role을 추가하여 전달한다. 
    send_msg = st.session_state.messages[:] ## list를 복사해야 한다. **********************************
    send_msg.append({"role": "system", "content": system_prompt})

    msg = requests.post("http://localhost:8000/langchain/prompt-sytem-role", 
                             json=send_msg, 
                             headers={"Content-Type": "application/json"} )
    st.session_state.messages.append({"role": "assistant", "content": msg.json()})
    # st.chat_message("assistant").write(msg.json())

    def stream_data():
        for word in msg.json().split(" "):
            yield word + " "
            time.sleep(0.1)

    st.chat_message("assistant").write_stream(stream_data)
    
