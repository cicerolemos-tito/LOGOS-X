# -*- coding: utf-8 -*-
import json
import os

PULSE_PATH = r'C:\Users\Cicero\LOGOS-X\OBR_BrainCenter_KnowledgeBase\MEMORY\SSOT_PULSE.json'

def get_pulse():
    with open(PULSE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def project():
    pulse = get_pulse()
    # Projeta a versao para o ambiente do Agente
    os.environ['LOGOS_VERSION'] = pulse['version']
    os.environ['LOGOS_MANDATE'] = pulse['current_mandate']
    print(f"--- [TELEPATHIC FIELD ACTIVE] ---")
    print(f"Projecting Version: {pulse['version']}")
    print(f"Target: ALL AGENTS & FILES")

if __name__ == '__main__':
    project()
