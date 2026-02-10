import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# タイトル
st.set_page_config(page_title="線画変換ツール")
st.title("🌲 レーザー加工用・線画ジェネレーター")

# APIキーの読み込み
if "GEMINI_API_KEY" not in st.secrets:
    st.error("SecretsにGEMINI_API_KEYが設定されていません。")
    st.stop()

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

uploaded_file = st.file_uploader("写真をアップロードしてください", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    # 修正ポイント：.convert('RGB') を追加して形式を整える
    image = Image.open(uploaded_file).convert('RGB') 
    st.image(image, caption='元の画像', use_container_width=True)

    if st.button('線画を生成する'):
        with st.spinner('Geminiが線を引いています...'):
            try:
                prompt = "この画像を、レーザーカッターで加工しやすいシンプルな黒の線画に変換してください。背景や影は不要です。"
                response = model.generate_content([prompt, image])
                
                # 結果の表示
                st.success("生成完了！")
                st.write(response.text)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
