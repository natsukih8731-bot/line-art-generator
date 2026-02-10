import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# タイトル
st.set_page_config(page_title="KIRecub 線画変換ツール")
st.title("🌲 レーザー加工用・線画ジェネレーター")

# APIキーを安全に読み込む（後で設定します）
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

uploaded_file = st.file_uploader("写真をアップロードしてください", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='元の画像', use_container_width=True)

    if st.button('線画を生成する'):
        with st.spinner('変換中...'):
            # レーザー加工に適した指示
            prompt = "この画像を、レーザーカッターで加工しやすいシンプルな黒の線画に変換してください。塗りつぶし、影、背景、色のグラデーションは一切不要です。白い背景に細い黒線のみで構成してください。"
            response = model.generate_content([prompt, image])
            
            # 結果表示（Geminiの応答が画像の場合）
            # ※簡易版のため、ここではAIが作成した「画像としての説明」を表示する仕組みです
            st.success("生成が完了しました！")
            st.write(response.text)
