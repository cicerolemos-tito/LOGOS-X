import os
import hashlib
import json
import subprocess
from pathlib import Path

# --- CONFIGURAÇÃO DE CAMINHOS ---
LOGOS_X_ROOT = Path(r"C:\Users\Cicero\LOGOS-X")
GEMINI_SKILLS_DIR = Path(r"C:\Users\Cicero\.gemini\skills")
CODEX_SKILLS_DIR = LOGOS_X_ROOT / ".codex" / "skills"
MANIFEST_PATH = LOGOS_X_ROOT / ".aiox-core" / "install-manifest.yaml"

def get_file_hash(file_path):
    """Gera o hash SHA256 de um arquivo."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_skill_drifts():
    """Compara skills entre o diretório global do Gemini e o local do Codex."""
    print("🔍 Analisando drifts de skills...")
    drifts = []
    
    # Mapear skills globais
    global_skills = {d.name: d for d in GEMINI_SKILLS_DIR.iterdir() if d.is_dir()}
    # Mapear skills locais
    local_skills = {d.name: d for d in CODEX_SKILLS_DIR.iterdir() if d.is_dir()}
    
    for name, path in global_skills.items():
        if name in local_skills:
            # Comparação simplificada por existência de arquivos principais
            # Poderia ser expandida para hash de cada arquivo .py/.md
            pass
        else:
            print(f"⚠️ Skill '{name}' presente no Global mas ausente no Local.")
            drifts.append(name)
            
    return drifts

def validate_and_heal_manifest():
    """Executa a validação do manifesto e tenta a auto-cura se falhar (Lei 17)."""
    print("🛡️ Validando integridade do manifesto...")
    try:
        # Tenta rodar o script de validação oficial
        result = subprocess.run(
            ["node", str(LOGOS_X_ROOT / "scripts" / "validate-manifest.js")],
            cwd=str(LOGOS_X_ROOT),
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("❌ Manifesto corrompido ou desatualizado. Iniciando Auto-Healing (Lei 17)...")
            # Executa a regeneração do manifesto
            heal_result = subprocess.run(
                ["node", str(LOGOS_X_ROOT / "scripts" / "generate-install-manifest.js")],
                cwd=str(LOGOS_X_ROOT),
                capture_output=True,
                text=True
            )
            if heal_result.returncode == 0:
                print("✅ Manifesto regenerado com sucesso.")
            else:
                print(f"🔥 Falha crítica na regeneração: {heal_result.stderr}")
        else:
            print("💎 Manifesto íntegro.")
            
    except Exception as e:
        print(f"🚨 Erro durante a validação/cura: {str(e)}")

def main():
    print("--- AIOX Skill Integrity Protector (v1.0) ---")
    check_skill_drifts()
    validate_and_heal_manifest()
    print("--- Operação concluída ---")

if __name__ == "__main__":
    main()
