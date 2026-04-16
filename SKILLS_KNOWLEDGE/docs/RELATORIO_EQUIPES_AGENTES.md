# Relatório de Estrutura: Equipes e Agentes (LOGOS-X)

Este documento detalha a disposição atual da base de inteligência sintética do ecossistema LOGOS-X, organizada por squads (equipes) e seus respectivos agentes.

---

## 1. Orquestração Central
Gerenciamento supremo do sistema e fluxos de trabalho.

*   **@jarvis (Orquestrador Supremo):** Comanda as operações globais.
    *   *Comandos:* `*ingest`, `*audit-logos`, `*audit-pertinence`, `*process-knowledge`.
*   **AIOX-Master:** Supervisão técnica e governança.
*   **Architect:** Design de sistemas e infraestrutura.

---

## 2. Squads Especializados (Localizados em `squads/`)

### A. Synthetic Intelligence Factory (SIF)
Focado na produção e calibração de modelos e dados sintéticos.
*   **@sif-factory:** Produção principal.
*   **@sif-extractor:** Extração de dados.
*   **@sif-assembler:** Montagem de componentes.
*   **@sif-validator:** Validação de qualidade.
*   **@sif-calibrator:** Ajuste fino de modelos.
*   **@sif-meta:** Inteligência sobre o processo.

### B. Nirvana Squad Creator (NSC)
Responsável pela criação dinâmica e otimização de novas equipes de IA.
*   **@nsc-orchestrator:** Orquestração de criação.
*   **@nsc-analyzer:** Análise de gaps de competência.
*   **@nsc-agent-creator:** Geração de novos agentes.
*   **@nsc-validator:** Validação de squads recém-criados.

### C. Ultimate Landing Page (ULP)
Especializado em conversão, design e desenvolvimento frontend de alta performance.
*   **@ulp-strategist:** Estratégia de conversão.
*   **@ulp-copywriter:** Escrita persuasiva.
*   **@ulp-design-architect:** Design visual e UX.
*   **@ulp-frontend-dev:** Desenvolvimento técnico.
*   **@ulp-reviewer:** Garantia de qualidade visual.

### D. Squads Genius Apex (APEX)
Focado em Context Engineering e destilação de conhecimento de elite.
*   **@apex-orquestrista:** Coordenação de contexto.
*   **@apex-maven:** Arquitetura de conhecimento.
*   **@apex-spark:** Alquimia e inovação.
*   **@apex-trim:** Escultura e compressão de dados (Token Economy).
*   **@apex-vigil:** Vigilância e validação de contexto.

### E. Skeptic Protocol (SKEPTIC)
Defesa cibernética, Red Teaming e auditoria de segurança (Lei 9).
*   **@skeptic-orchestrator:** Comando de defesa.
*   **@skeptic-redteamer:** Testes de invasão e estresse.
*   **@skeptic-predictor:** Previsão de falhas sistêmicas.
*   **@skeptic-tester:** Engenharia de testes rigorosos.
*   **@skeptic-solution:** Implementação de correções críticas.

### F. Flywheel Core (FLYWHEEL)
Aceleração de execução cíclica e inteligência de enxame (Swarm Intelligence).
*   **@fly-architect:** Desenho da flywheel.
*   **@fly-bead-manager:** Gestão de ciclos de execução.
*   **@fly-swarm:** Coordenação de múltiplos agentes em paralelo.
*   **@fly-hardening:** Especialista em robustez de execução.

---

## 3. Equipes de Suporte Técnico (Localizados em `.agents/squads/`)

### Engineering
*   **code-reviewer:** Auditoria de código.
*   **issue-solver:** Resolução de bugs.
*   **test-writer:** Cobertura de testes.

### Intelligence
*   **intel-lead:** Liderança de análise.
*   **intel-eval:** Avaliação de métricas.
*   **intel-critic:** Crítica técnica e lógica.

### Operations & Research
*   **ops-lead:** Gestão de metas e finanças.
*   **goal-tracker:** Monitoramento de objetivos.
*   **analyst / synthesizer:** Pesquisa profunda e síntese de informações.

---

## 4. Braço Executor Externo

### Hermes Agent (@higgins)
O executor de campo para interações fora do ambiente CLI.
*   **Capacidades:** Navegação web, automação de e-mail, geração multimídia, interface de terminal.
*   **Integração:** Invocado via comando `Logos` ou `hermes`.

---

## 5. Leis de Governança (Protocolo PRIME)
1.  **Lei 9 (State Snapshot):** Proteção via commit antes de alterações.
2.  **Lei 10 (Agent Synergy):** Autoridade para invocar Hermes.
3.  **Lei 11 (Atomic Modularity):** Skills isoladas e modulares.
4.  **Lei 12 (Visual Audit):** Diagnóstico via captura de tela/vídeo.

---
*Relatório gerado em 11 de Abril de 2026 para o Mestre Cicero.*
