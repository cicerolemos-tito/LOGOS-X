import os
import time
import fal_client
from dotenv import load_dotenv

# Carregar chaves do .env
load_dotenv(dotenv_path='C:/Users/Cicero/LOGOS-X/.env')
os.environ["FAL_KEY"] = os.getenv("FAL_KEY")

def render_and_open():
    print("🚀 [LOGOS-X] Iniciando Renderização 4K Padrão Cinema...")
    
    # Parâmetros do Despacho Cinematográfico
    prompt = (
        "Cinematic video 16:9, 90s — Two hero sisters: Antonia (11) and Estela (8). "
        "Antonia playing grand piano, soundwaves emitting in teal light. "
        "Estela manipulating golden light filaments. High-tech urban dojo, sunset lighting, "
        "Unreal Engine 5 style, 4K, highly detailed, photorealistic."
    )
    
    try:
        # Chamada para o motor Kling 1.5 via API FAL
        print("📡 Enviando manifesto para a nuvem (Kling 1.5)...")
        handler = fal_client.submit(
            "fal-ai/kling-video/v1.5/pro/image-to-video",
            arguments={
                "prompt": prompt,
                "image_url": "C:/Users/Cicero/LOGOS-X/RESEARCH/ASSETS/fotos-meninas.jpeg",
                "duration": "10" # Gerando preview de alta fidelidade para abertura
            }
        )
        
        result = handler.get()
        video_url = result['video']['url']
        
        # Download do arquivo final
        output_path = "C:/Users/Cicero/LOGOS-X/RESEARCH/SINFONIA_SONIS_FINAL.mp4"
        print(f"✅ Renderização concluída! Baixando vídeo para: {output_path}")
        
        import requests
        r = requests.get(video_url)
        with open(output_path, 'wb') as f:
            f.write(r.content)
            
        # Abrir o arquivo automaticamente no Windows
        print("🎬 Abrindo a Versão Final para o Mestre...")
        os.startfile(output_path)
        
    except Exception as e:
        print(f"❌ Erro no Maestro de Renderização: {e}")

if __name__ == "__main__":
    render_and_open()
