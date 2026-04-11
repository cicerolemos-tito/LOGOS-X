import sqlite3
import json
from datetime import datetime

# --- CONFIGURAÇÃO ---
DB_PATH = r"C:\Users\Cicero\LOGOS-X\.synapse\memory_nucleus.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge_beads (
            bead_id TEXT PRIMARY KEY,
            content TEXT,
            squad_source TEXT,
            confidence REAL,
            tags TEXT,
            timestamp TEXT,
            law_compliance TEXT
        )
    ''')
    conn.commit()
    return conn

def ingest_bead(conn, bead_id, content, squad, confidence, tags, laws):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO knowledge_beads VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (bead_id, content, squad, confidence, json.dumps(tags), datetime.now().isoformat(), json.dumps(laws)))
    conn.commit()

# --- EXECUÇÃO DE INGESTÃO (Fase 1) ---
conn = init_db()

# Bead 1: ElevenLabs Integration
ingest_bead(conn, "BEAD-001", "Integração de áudio via ElevenLabs concluída para narração atmosférica.", "Research", 1.0, ["audio", "elevenlabs"], ["Lei 12"])

# Bead 2: Logos-Vision
ingest_bead(conn, "BEAD-002", "Capacidade de Visão Computacional (Logos-Vision) ativa para auditoria de UI.", "Research", 1.0, ["vision", "audit"], ["Lei 12"])

# Bead 3: Lei 15 Rigor
ingest_bead(conn, "BEAD-003", "Adoção da Lei 15 (Flywheel Rigor): Proibida escrita de código sem Plan Space.", "Engineering", 1.0, ["law", "flywheel"], ["Lei 15"])

# Bead 4: Five Vitals
ingest_bead(conn, "BEAD-004", "Skill 'Five Vitals' instalada para diagnóstico de integridade estrutural.", "Intelligence", 1.0, ["integrity", "skill"], ["Lei 18"])

# Bead 5: EVA Genesis
ingest_bead(conn, "BEAD-005", "Design System EVA GENESIS PRO (OKLCH/Tailwind v4) estabelecido como padrão.", "Product", 1.0, ["design", "ui"], ["Lei 12"])

conn.close()
print("💎 Fase 1: 5 Knowledge Beads ingeridas com sucesso no Núcleo de Memória.")
