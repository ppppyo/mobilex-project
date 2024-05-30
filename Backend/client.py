import requests

# 서버의 URL
url = "http://localhost:8000/api/v1/generate-audio/"

# 가사 데이터
lyrics = "내가 가사야!"

# POST 요청 보내기
response = requests.post(url, json={"inputs": lyrics})

# 응답에서 오디오 URL 추출
audio_data = response.json()
if "audio_url" in audio_data:
    audio_url = audio_data["audio_url"]
    print(f"Audio URL: {audio_url}")
else:
    print("Error:", audio_data["error"])
