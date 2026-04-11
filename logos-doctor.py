#!/usr/bin/env python3
"""
🛡️ LOGOS-X DOCTOR -- Ferramenta de Diagnóstico e Integridade Sistêmica
Inspirado em Claw Code | Protocolo LOGOS-X Prime Directives
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Configurações de Cores (ANSI)
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

class LogosDoctor:
    def __init__(self):
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "status": "PASS",
            "checks": []
        }
        self.logos_root = Path(r"C:\Users\Cicero\LOGOS-X")

    def log(self, level, msg):
        prefix = {
            "PASS": f"{GREEN}[✓]{RESET}",
            "WARN": f"{YELLOW}[?]{RESET}",
            "FAIL": f"{RED}[✗]{RESET}",
            "INFO": f"{CYAN}[i]{RESET}"
        }
        print(f"{prefix.get(level, '   ')} {msg}")

    def check_env_vars(self):
        """Nível 2: Validação de Chaves de API"""
        critical_keys = ["GOOGLE_API_KEY", "ANTHROPIC_API_KEY", "ELEVENLABS_API_KEY"]
        missing = []
        for key in critical_keys:
            if not os.environ.get(key):
                missing.append(key)
        
        if not missing:
            self.log("PASS", "Chaves de API Críticas detectadas e carregadas.")
        else:
            self.log("WARN", f"Chaves ausentes no ambiente: {', '.join(missing)}")

    def check_tools(self):
        """Nível 1: Binários e Compiladores"""
        tools = [
            ("git", "--version"),
            ("python", "--version"),
            ("node", "--version"),
            ("rustc", "--version")
        ]
        for name, cmd in tools:
            try:
                subprocess.run([name, cmd], capture_output=True, check=True)
                self.log("PASS", f"Ferramenta detectada: {name.capitalize()}")
            except:
                self.log("FAIL", f"Ferramenta NÃO encontrada ou erro: {name.capitalize()}")

    def check_memory_palace(self):
        """Nível 3: Status da Memória Infinita (MemPalace)"""
        palace_path = self.logos_root / "MEMORY" / "PALACE"
        if palace_path.exists():
            self.log("PASS", "Palácio de Memória detectado e acessível.")
        else:
            self.log("WARN", "Diretório de Memória (PALACE) não encontrado.")

    def check_security_higiene(self):
        """Nível 4: Proteção de Dados (Lei 1)"""
        gitignore = self.logos_root / ".gitignore"
        if gitignore.exists():
            try:
                content = gitignore.read_text(encoding="utf-8")
                if ".env" in content and "node_modules" in content:
                    self.log("PASS", "Higiene de Segurança (.gitignore) validada.")
                else:
                    self.log("WARN", ".gitignore incompleto (pode vazar .env).")
            except Exception as e:
                self.log("FAIL", f"Erro ao ler .gitignore: {str(e)}")
        else:
            self.log("FAIL", ".gitignore AUSENTE. Segurança em risco!")

    def run_all(self):
        print(f"\n{BOLD}{CYAN}=== LOGOS-X DOCTOR: DIAGNÓSTICO 360° ==={RESET}")
        print(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        self.log("INFO", "Iniciando Varredura Nível 1 (Binários)...")
        self.check_tools()
        
        print("-" * 40)
        self.log("INFO", "Iniciando Varredura Nível 2 (Ambiente/Auth)...")
        self.check_env_vars()
        
        print("-" * 40)
        self.log("INFO", "Iniciando Varredura Nível 3 (Memória/Arquitetura)...")
        self.check_memory_palace()
        
        print("-" * 40)
        self.log("INFO", "Iniciando Varredura Nível 4 (Segurança/Lei 1)...")
        self.check_security_higiene()
        
        print(f"\n{BOLD}{CYAN}=== DIAGNÓSTICO CONCLUÍDO ==={RESET}\n")

if __name__ == "__main__":
    doctor = LogosDoctor()
    doctor.run_all()
