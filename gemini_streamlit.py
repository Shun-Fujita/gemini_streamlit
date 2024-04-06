import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv


st.title("Gemini Chat on Streamlit")

# Google Generative APIのAPIキーを.streamlit/secrets.tomlから読み込む
load_dotenv()
API_KEY = os.getenv(st.secrets["API_KEY"])

# Gemini-proモデルの利用開始
genai.configure(api_key=API_KEY)

# チャットログを保存したセッション情報を初期化
if "chat_ai" not in st.session_state:
    model = genai.GenerativeModel(model_name="gemini-pro")
    st.session_state["chat_ai"] = model.start_chat(history=[])
    st.session_state.chat_log = []


prompt = st.chat_input("geminiに聞きたいことを入力してください")

# 入力が送信された場合に実行
if prompt:
    # 前回までのチャット履歴を表示
    for chat_log in st.session_state.chat_log:
        message_log = st.chat_message(chat_log["role"])
        message_log.markdown(chat_log["content"])
    
    # 入力した内容を出力
    message = st.chat_message("user")
    message.markdown(prompt)

    # geminiからの回答を出力
    response = st.session_state["chat_ai"].send_message(prompt)
    message_reply = st.chat_message("assistant")
    message_reply.markdown(response.text)
    
    # 自分のチャット内容とGeminiの回答をチャットログに記録する
    st.session_state.chat_log.append({"role":"user", "content": prompt})
    st.session_state.chat_log.append({"role":"assistant", "content": response.text})
