import requests
import json

url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4lcv85jkMB4w"
headers = {
    "xi-api-key": "b437a118944cc4635b0eed19ee509d023047133d1c9901ebfc8c73289ccfa68f",
    "Content-Type": "application/json"
}
data = {
    "text": "Saudações, Mestre Cícero. O sistema LOGOS-X está agora com voz ativa.",
    "model_id": "eleven_multilingual_v2"
}

try:
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open(r"C:\Users\Cicero\LOGOS-X\RESEARCH\test_voice.mp3", "wb") as f:
            f.write(response.content)
        print("PASS: Audio gerado com sucesso.")
    else:
        print(f"FAIL: Erro na API. Status: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"FAIL: Erro de conexão: {str(e)}")
