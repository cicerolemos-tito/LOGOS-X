# -*- coding: utf-8 -*-
import os
import re

OBELISCO = r'C:\Users\Cicero\LOGOS-X\OBR_BrainCenter_KnowledgeBase\MEMORY\Alma_leis.zig'

def get_dna():
    with open(OBELISCO, 'r', encoding='utf-8') as f:
        content = f.read()
        version = re.search(r'versao_kernel = \"(.*?)\"', content).group(1)
        return version

def inject():
    dna = get_dna()
    # Injeta na memoria volatil da sessao
    os.environ['LOGOS_DNA'] = dna
    print(f"--- [QUANTUM INJECTION SUCCESS] ---")
    print(f"DNA projected into Agent Mind: {dna}")

if __name__ == '__main__':
    inject()
