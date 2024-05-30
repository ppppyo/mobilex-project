import streamlit as st
import requests

# Streamlit 설정
st.title("응원가 제작기")
st.write("가사를 입력하고 'Generate Audio' 버튼을 클릭하세요.")

# 가사 입력
lyrics = st.text_area("가사 입력")

# 서버의 URL
api_url = "http://localhost:8502/api/v1/generate-audio/"


if st.button("Generate Audio"):
    # POST 요청 보내기
    response = requests.post(api_url, json={"inputs": lyrics})
    
    if response.status_code == 200:
        audio_data = response.json()
        
        if "audio_url" in audio_data:
            audio_url = f"http://localhost:8502{audio_data['audio_url']}"
            st.audio(audio_url, format="audio/wav")
        else:
            st.error("Error: Audio URL not found in response.")
    else:
        error_message = response.json().get("detail", response.text)
        st.error(f"Error: {response.status_code}, {error_message}")