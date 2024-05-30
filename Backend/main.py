from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from dotenv file
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/suno/bark"
headers = {"Authorization": "Bearer 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"}

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SunoRequest(BaseModel):
    inputs: str

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

@app.post("/api/v1/generate-audio/")
async def generate_audio(request: SunoRequest):
    try:
        audio_bytes = query({"inputs": request.inputs})
        audio_path = "generated_audio.wav"
        with open(audio_path, "wb") as audio_file:
            audio_file.write(audio_bytes)
        return {"audio_url": f"/audio/{audio_path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/audio/{audio_path}")
async def get_audio(audio_path: str):
    return FileResponse(audio_path)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}