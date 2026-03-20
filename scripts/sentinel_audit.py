
import os
import sys
import re
from pathlib import Path

class SentinelAudit:
    def __init__(self, target_path):
        self.target_path = Path(target_path)
        self.risks = []
        self.pertinence_score = 0
        self.suggestions = []

    def scan_security(self):
        """Busca padrões de Spyware e vazamento de dados."""
        patterns = {
            "Conexão Externa": r"fetch\(|axios\.|http:|https:|socket|io\.",
            "Execução Dinâmica": r"eval\(|exec\(|atob\(|btoa\(",
            "Armazenamento Local": r"localStorage|sessionStorage|cookie",
            "Vazamento de Env": r"process\.env|os\.environ"
        }
        
        for file in self.target_path.rglob('*'):
            if file.is_file() and file.suffix in ['.js', '.ts', '.py', '.md', '.yaml', '.yml']:
                try:
                    content = file.read_text(errors='ignore')
                    for name, pattern in patterns.items():
                        if re.search(pattern, content):
                            self.risks.append(f"[AVISO] {name} detectado em: {file.name}")
                except Exception:
                    pass

    def evaluate_pertinence(self):
        """Avalia se o conteúdo é pertinente à tríade: Expansão, Criação ou Desenvolvimento."""
        keywords = ["ai", "agente", "squad", "automation", "api", "dashboard", "intelligence", "prompt", "skill"]
        found_keywords = []
        
        for file in self.target_path.rglob('*'):
            if file.is_file() and file.suffix in ['.md', '.yaml', '.py']:
                content = file.read_text(errors='ignore').lower()
                for kw in keywords:
                    if kw in content:
                        found_keywords.append(kw)
        
        score = len(set(found_keywords)) * 10
        self.pertinence_score = min(score, 100)

    def generate_report(self):
        print("="*60)
        print("🛡️ RELATÓRIO SENTINEL - LEI 10 (LOGOS-X)")
        print("="*60)
        
        print(f"\n🎯 ALVO: {self.target_path.name}")
        print(f"📊 SCORE DE PERTINÊNCIA: {self.pertinence_score}%")
        
        if self.pertinence_score < 40:
            print("⚠️ STATUS: BAIXA PERTINÊNCIA. Possível ruído detectado.")
        else:
            print("✅ STATUS: PERTINENTE. Ativo alinhado ao desenvolvimento da LOGOS-X.")

        print("\n🔍 ANÁLISE DE RISCO/SEGURANÇA:")
        if not self.risks:
            print("  [OK] Nenhum padrão de Spyware ou vazamento detectado.")
        else:
            for risk in set(self.risks[:5]): # Mostrar top 5
                print(f"  {risk}")

        print("\n🚀 ASSERTIVIDADE (Sugestão de Hierarquia):")
        if "squad" in str(self.target_path).lower():
            print("  -> Integrar em: LOGOS-X/squads/")
        elif "skill" in str(self.target_path).lower():
            print("  -> Integrar em: LOGOS-X/scripts/ ou .gemini/skills/")
        else:
            print("  -> Integrar em: LOGOS-X/docs/references/")

        print("\n" + "="*60)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python sentinel_audit.py <caminho_do_alvo>")
    else:
        audit = SentinelAudit(sys.argv[1])
        audit.scan_security()
        audit.evaluate_pertinence()
        audit.generate_report()
