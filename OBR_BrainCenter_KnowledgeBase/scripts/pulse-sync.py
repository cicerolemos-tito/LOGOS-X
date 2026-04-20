# -*- coding: utf-8 -*-
import json
import os

PULSE_PATH = r'C:\Users\Cicero\LOGOS-X\OBR_BrainCenter_KnowledgeBase\MEMORY\SSOT_PULSE.json'

def get_current_pulse():
    if not os.path.exists(PULSE_PATH):
        return {"version": "UNKNOWN", "current_mandate": "RESTORE PULSE"}
    with open(PULSE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def inject_context():
    pulse = get_current_pulse()
    print("--- [TELEPATHIC INJECTION START] ---")
    print(f"SYSTEM_VERSION: {pulse.get('version', 'N/A')}")
    print(f"CURRENT_MANDATE: {pulse.get('current_mandate', 'N/A')}")
    print(f"LAST_SYNC: {pulse.get('last_sync', 'N/A')}")
    print("--- [TELEPATHIC INJECTION COMPLETE] ---")
    print("Status: Context synchronized with SSOT Core.")
    return pulse

if __name__ == '__main__':
    inject_context()
