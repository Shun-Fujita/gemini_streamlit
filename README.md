# Gemini Streamlit

## Overview
geminiとのチャットボット風Streamlitアプリ

## Requirements
- Windows11
- Python3.11
- Streamlit
- google-generativeai
- dotenv

## Usage

### 1. API Keyの取得

1. 下記へアクセスする

https://ai.google.dev/?hl=en

2. Get API Key in Google AI Studioをクリックし、Google AI Studioが立ち上がったら、Get API KeyからAPI Keyを取得する

3. このリポジトリ内に.streamlitフォルダを作成し、その中にsecrets.tomlファイルを作成する。<br>
secrets.tomlファイルの中身は以下の通りにする。

```
API_KEY="Your API Key"
```

### 実行

```
cd gemini_streamlit
streamlit run gemini_streamlit.py
```

画面下部に質問を入力すると、質問とgeminiの回答が時系列順に表示されます。