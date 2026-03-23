import os
import requests
from dotenv import load_dotenv

# Carregar chaves do .env
load_dotenv(dotenv_path='C:/Users/Cicero/LOGOS-X/.env')
api_key = os.getenv("ELEVENLABS_API_KEY")

def generate_voice(text, filename):
    print(f"🎙️ Gerando voz para: {text}")
    # Voice ID para uma voz feminina jovem/infantil (Rachel ou similar)
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.5,
            "use_speaker_boost": True
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        output_dir = "C:/Users/Cicero/LOGOS-X/RESEARCH/AUDIO"
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"✅ Arquivo salvo em: {file_path}")
        return file_path
    else:
        print(f"❌ Erro na API ElevenLabs: {response.text}")
        return None

if __name__ == "__main__":
    # Grito de Guerra das Irmãs
    script_text = "Antonia: Sinfonia Sonis... ATIVAR! Estela: Luz Estelar... BRILHAR! Ambas: União das Irmãs!"
    generate_voice(script_text, "vozes_sisters_final.mp3")
