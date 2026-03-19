
import pandas as pd
import numpy as np
from pathlib import Path

# Constantes de caminho (Vou referenciar o seu arquivo de planilha original)
EXCEL_PATH = r"C:\Users\Cicero\Desktop\DOCS\PLANILHA\Atual.LANER (CONTROLE)17.03.2026.xlsx"

class ExcelService:
    def __init__(self):
        self.df = pd.read_excel(EXCEL_PATH, sheet_name='consolidado')

    def extract_section(self, start_row: int, end_row: int, name: str):
        # A lógica que usamos na análise anterior, agora estruturada para API
        data = self.df.iloc[start_row:end_row+1, 1:14].copy()
        data.columns = ['Ano', 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
        data['Nome'] = name
        data = data.dropna(subset=['Ano'])
        data['Ano'] = pd.to_numeric(data['Ano'], errors='coerce').astype(int)
        return data

    def get_all_data(self):
        slings = self.extract_section(0, 8, 'SLING')
        big_bags = self.extract_section(10, 18, 'BIG BAG')
        lavanderia = self.extract_section(31, 35, 'LAVANDERIA')
        return pd.concat([slings, big_bags, lavanderia])

class ProjectionService:
    @staticmethod
    def calculate_projection(data: pd.DataFrame, name_pattern: str):
        subset = data[data['Nome'].str.contains(name_pattern, na=False, case=False)]
        
        subset_2026 = subset[subset['Ano'] == 2026]
        if subset_2026.empty:
            return None

        # Realizado JAN-MAR 2026
        actual_2026_q1 = pd.to_numeric(subset_2026.iloc[0, 1:4], errors='coerce').fillna(0).sum()
        
        # Sazonalidade histórica (2022-2025)
        hist = subset[(subset['Ano'] < 2026) & (subset['Ano'] >= 2022)]
        
        weights = []
        for _, row in hist.iterrows():
            full_year_total = pd.to_numeric(row[1:13], errors='coerce').fillna(0).sum()
            if full_year_total > 0:
                q1_total = pd.to_numeric(row[1:4], errors='coerce').fillna(0).sum()
                weights.append(q1_total / full_year_total)
        
        avg_weight = np.mean(weights) if weights else 0.25
        projected_total = actual_2026_q1 / avg_weight if avg_weight > 0 else 0
        
        return {
            "produto": name_pattern.upper(),
            "realizado_q1": float(actual_2026_q1),
            "projetado_total": float(projected_total),
            "peso_historico_q1": float(avg_weight)
        }
