
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  LineChart, Line 
} from 'recharts';
import { LayoutDashboard, TrendingUp, Users, Activity, Package } from 'lucide-react';

const API_BASE = "http://localhost:8000/api";

export default function App() {
  const [salesData, setSalesData] = useState([]);
  const [projections, setProjections] = useState([]);
  const [squadStatus, setSquadStatus] = useState(null);

  useEffect(() => {
    // Fetch data from FastAPI backend
    const fetchData = async () => {
      try {
        const [history, projs, status] = await Promise.all([
          axios.get(`${API_BASE}/sales/history`),
          axios.get(`${API_BASE}/sales/projections`),
          axios.get(`${API_BASE}/squad/status`)
        ]);
        setSalesData(history.data);
        setProjections(projs.data);
        setSquadStatus(status.data);
      } catch (err) {
        console.error("Erro ao carregar dados do Dashboard", err);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 font-sans">
      {/* Sidebar / Topbar */}
      <header className="border-b border-slate-800 p-4 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div className="flex items-center gap-2">
            <LayoutDashboard className="text-green-500" />
            <h1 className="text-xl font-bold tracking-tight text-slate-100">LOGOS-X <span className="text-green-500">COMMAND CENTER</span></h1>
          </div>
          <div className="flex items-center gap-4 text-sm text-slate-400">
            <div className="flex items-center gap-1">
              <Users size={16} />
              <span>{squadStatus?.agents_active || 0} Agentes Ativos</span>
            </div>
            <div className="h-4 w-px bg-slate-800" />
            <span>Última Sincronização: {squadStatus?.last_sync}</span>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto p-6 space-y-8">
        {/* KPI Cards (Projections) */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {projections.map((proj) => (
            <div key={proj.produto} className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-sm hover:border-green-500/50 transition-all hover:scale-[1.02]">
              <div className="flex justify-between items-start mb-4">
                <span className="text-xs font-bold text-slate-500 uppercase tracking-widest">{proj.produto}</span>
                <TrendingUp className="text-green-500" size={18} />
              </div>
              <div className="space-y-1">
                <p className="text-2xl font-bold text-green-50">Projeção: {Math.round(proj.projetado_total).toLocaleString()}</p>
                <p className="text-sm text-slate-400">Realizado Q1: {proj.realizado_q1.toLocaleString()}</p>
              </div>
              <div className="mt-4 pt-4 border-t border-slate-800 flex justify-between items-center">
                <span className="text-xs text-slate-500">Peso Histórico Q1</span>
                <span className="text-xs font-mono text-green-400">{(proj.peso_historico_q1 * 100).toFixed(2)}%</span>
              </div>
            </div>
          ))}
        </div>

        {/* Sales Chart Section */}
        <section className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-sm">
          <h2 className="text-lg font-semibold mb-6 flex items-center gap-2">
            <Activity className="text-green-500" />
            Tendência de Vendas (Performance Mensal)
          </h2>
          <div className="h-80 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={salesData.filter(d => d.ano >= 2023)}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                <XAxis dataKey="ano" stroke="#64748b" />
                <YAxis stroke="#64748b" />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '8px' }}
                  itemStyle={{ color: '#f8fafc' }}
                />
                <Legend />
                <Bar dataKey="valores.JAN" name="Janeiro" fill="#22c55e" radius={[4, 4, 0, 0]} />
                <Bar dataKey="valores.FEV" name="Fevereiro" fill="#4ade80" radius={[4, 4, 0, 0]} />
                <Bar dataKey="valores.MAR" name="Março" fill="#86efac" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </section>

        {/* Squad Activity */}
        <section className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-sm">
          <h2 className="text-lg font-semibold mb-6 flex items-center gap-2">
            <Package className="text-green-500" />
            Infraestrutura de Esquadrões
          </h2>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
             {squadStatus?.squads.map(s => (
               <div key={s} className="bg-slate-950 p-3 rounded-lg border border-slate-800 text-center text-sm font-medium">
                  {s}
               </div>
             ))}
          </div>
        </section>
      </main>
    </div>
  );
}
