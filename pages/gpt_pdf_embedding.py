import streamlit as st
from auth import set_user_menu
import requests
import time
import pandas as pd
from streamlit_pdf_reader import pdf_reader

set_user_menu() 
st.sidebar.divider()

side_col1, side_col2 = st.sidebar.columns([2,1])
side_col1.subheader("PDF List")
# col2.button("Refresh")
side_col2.button("Refresh", use_container_width=True)

df = pd.DataFrame(columns=['File name','UpdateAt'])
edited_df = st.sidebar.data_editor(
    data=df, 
    use_container_width=True, 
    column_config={
        "filepath": st.column_config.Column(
            label="파일명"
        ), 
        "username": st.column_config.Column(label="등록자"), 
        # "is_active" : st.column_config.Column(label="사용여부")
    }
)

# def fileupload():
#     pass 

st.title("💬 GPT pdf embedding")
# st.caption("🚀 GPT pdf embedding")

def stream_data(msg:str):
    for word in msg.json().split(" "):
        yield word + " "
        time.sleep(0.1)


main_col2, main_col1  = st.columns([1, 1])

with main_col1: 
    with st.container(border=True) : 
        upload_file = st.file_uploader(label="📃 PDF 파일을 먼저 업로드 해주세요. ")

        if upload_file is not None : 
            # source1='./11107_4.pdf'
            pdf_reader(upload_file)


with main_col2:
    with st.container(border = True) : 

        st.caption("🚀 업로드된 pdf에 대하여 질문하세요.")

        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "PDF 업로드 후 Chating이 가능합니다."}]

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input():

            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            # system role을 추가하여 전달한다. 
            send_msg = st.session_state.messages[:] ## list를 복사해야 한다. **********************************
            send_msg.append({"role": "system", "content": "과학자로서 대답해줘."})

            msg = requests.post("http://localhost:8000/langchain/prompt-sytem-role", 
                                    json=send_msg, 
                                    headers={"Content-Type": "application/json"} )
            st.session_state.messages.append({"role": "assistant", "content": msg.json()})
            # st.chat_message("assistant").write(msg.json())

            st.chat_message("assistant").write_stream(stream_data(msg))



# import PyPDF2
# pdf_reader = PyPDF2.PdfReader(open("11107_4.pdf", "rb"))

# # pdf_data = pdf_reader.getDocumentInfo()
# # print('----Metadata of the file----')
# # for md in pdf_data:
# #     print(md+ ':' +pdf_data[md])
              

# content = ""
# for page in range(len(pdf_reader.pages)):
#         content += pdf_reader.pages(page) # .extractText()
#     # Display the content
# # print(content)
# # st.write(content)