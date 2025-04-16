import lmstudio as lms
import streamlit as st

title = st.text_input("prompt", "")
model = lms.llm("mistral-nemo-instruct-2407")
result = model.respond(title)

st.title(result)
#start server: streamlit run /Users/dominicchan/PycharmProjects/webInterface/file.py