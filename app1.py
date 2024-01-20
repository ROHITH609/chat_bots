import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config("Gemini Chatbot")
st.header("Gemini Chat Bot")



genai.configure(api_key=os.getenv("api_key"))
model1=genai.GenerativeModel('gemini-pro')


if 'chats' not in st.session_state:
    st.session_state.chats=model1.start_chat(history=[])


for i in st.session_state.chats.history:
    st.chat_message("assistant" if i.role=="model" else i.role).markdown(i.parts[0].text)

if input:=st.chat_input("Enter some thing Bro"):
    st.chat_message("user").markdown(input)
    res=st.session_state.chats.send_message(input)
    st.chat_message("assistant").markdown(res.text)

