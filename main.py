# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st


# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("hi!")
# print(result)

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()


st.title('테스트')
content = st.text_input("시의 주제를 제시해주세요")
if st.button('시 작성 요청하기'):
    with st.spinner('시 작성중...'):
        result=chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)



