import requests
from config import ELEVENLABS_API_KEY, VOICE_ID

def generate_audio(script):
    """Generate speech audio from ElevenLabs API."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}", "Content-Type": "application/json"}
    data = {"text": script, "model_id": "eleven_turbo", "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}}
    
    response = requests.post(url, json=data, headers=headers)
    audio_path = "generated/audio/dialogue.mp3"
    with open(audio_path, "wb") as f:
        f.write(response.content)
    return audio_path

