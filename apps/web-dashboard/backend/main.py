
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from pydantic import BaseModel
from services.excel_service import ExcelService, ProjectionService
import pandas as pd

app = FastAPI(title="LOGOS-X Sales Dashboard API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "online", "message": "LOGOS-X Sales API ready"}

@app.get("/api/sales/history")
async def get_sales_history():
    excel = ExcelService()
    df = excel.get_all_data()
    # Converte para JSON amigável para o Frontend
    result = []
    for _, row in df.iterrows():
        result.append({
            "nome": row['Nome'],
            "ano": int(row['Ano']),
            "valores": row[['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']].to_dict()
        })
    return result

@app.get("/api/sales/projections")
async def get_projections():
    excel = ExcelService()
    df = excel.get_all_data()
    
    ps = ProjectionService()
    result = []
    for prod in ['SLING', 'BIG BAG', 'LAVANDERIA']:
        proj = ps.calculate_projection(df, prod)
        if proj:
            result.append(proj)
    return result

@app.get("/api/squad/status")
async def get_squad_status():
    return {
        "squads": ["Main", "SIF"],
        "agents_active": 15,
        "last_sync": "2026-03-19"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
