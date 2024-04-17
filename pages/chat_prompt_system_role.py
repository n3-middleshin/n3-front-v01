import streamlit as st
from service import post, get 
from auth import set_user_menu, get_username 
import requests

set_user_menu() 

st.sidebar.divider()
system_prompt = st.sidebar.text_area("💬 AI System Prompt", height=200)


st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "오늘은 무엇을 도와드릴까요?"}]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # system role을 추가하여 전달한다. 
    send_msg = st.session_state.messages[:] ## list를 복사해야 한다. 
    send_msg.append({"role": "system", "content": system_prompt})

    msg = requests.post("http://localhost:8000/langchain/prompt-sytem-role", 
                             json=send_msg, 
                             headers={"Content-Type": "application/json"} )
    st.session_state.messages.append({"role": "assistant", "content": msg.json()})
    st.chat_message("assistant").write(msg.json())
