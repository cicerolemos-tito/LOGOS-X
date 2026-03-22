# AGENTS.md - Synkra AIOX

Este arquivo configura o comportamento esperado de agentes no Codex CLI neste repositorio.

## Constitution

Siga `.aiox-core/constitution.md` como fonte de verdade:
- CLI First
- Agent Authority
- Story-Driven Development
- No Invention
- Quality First
- Absolute Imports
- **Lei 10: Governança Proativa (Filtragem e Assertividade)**

## Workflow Obrigatorio

1. Inicie por uma story em `docs/stories/`
2. Implemente apenas o que os acceptance criteria pedem
3. Atualize checklist (`[ ]` -> `[x]`) e file list
4. Execute quality gates antes de concluir

## Quality Gates

```bash
npm run lint
npm run typecheck
npm test
```

## Estrutura Principal

- Core framework: `.aiox-core/`
- CLI: `bin/`
- Pacotes: `packages/`
- Testes: `tests/`
- Documentacao: `docs/`

## IDE/Agent Sync

- Sincronizar regras/agentes: `npm run sync:ide`
- Validar drift: `npm run sync:ide:check`
- Rodar paridade multi-IDE (Claude/Codex/Gemini): `npm run validate:parity`
- Sync Claude Code: `npm run sync:ide:claude`
- Sincronizar Gemini CLI: `npm run sync:ide:gemini`
- Validar Codex sync/integration: `npm run validate:codex-sync && npm run validate:codex-integration`
- Gerar skills locais do Codex: `npm run sync:skills:codex`
- Este repositorio usa **local-first**: prefira `.codex/skills` versionado no projeto
- Use `sync:skills:codex:global` apenas para testes fora deste repo

## Agent Shortcuts (Codex)

Preferencia de ativacao no Codex CLI:
1. Use `/skills` e selecione `aiox-<agent-id>` vindo de `.codex/skills` (ex.: `aiox-architect`)
2. Se preferir, use os atalhos abaixo (`@architect`, `/architect`, etc.)

Quando a mensagem do usuario for um atalho de agente, carregue o arquivo correspondente em `.aiox-core/development/agents/` (fallback: `.codex/agents/`), renderize o greeting via `generate-greeting.js` e assuma a persona ate receber `*exit`.

### Core Orchestration
- `@jarvis`, `/jarvis` -> O Orquestrador Supremo.
  - Commands: `*ingest`, `*audit-logos`, `*audit-pertinence`, `*process-knowledge`.

Atalhos aceitos por agente:
- `@aiox-master`, `/aiox-master`, `/aiox-master.md` -> `.aiox-core/development/agents/aiox-master.md`
- `@analyst`, `/analyst`, `/analyst.md` -> `.aiox-core/development/agents/analyst.md`
- `@architect`, `/architect`, `/architect.md` -> `.aiox-core/development/agents/architect.md`
- `@data-engineer`, `/data-engineer`, `/data-engineer.md` -> `.aiox-core/development/agents/data-engineer.md`
- `@dev`, `/dev`, `/dev.md` -> `.aiox-core/development/agents/dev.md`
- `@devops`, `/devops`, `/devops.md` -> `.aiox-core/development/agents/devops.md`
- `@pm`, `/pm`, `/pm.md` -> `.aiox-core/development/agents/pm.md`
- `@po`, `/po`, `/po.md` -> `.aiox-core/development/agents/po.md`
- `@qa`, `/qa`, `/qa.md` -> `.aiox-core/development/agents/qa.md`
- `@sm`, `/sm`, `/sm.md` -> `.aiox-core/development/agents/sm.md`
- `@squad-creator`, `/squad-creator`, `/squad-creator.md` -> `.aiox-core/development/agents/squad-creator.md`
- `@ux-design-expert`, `/ux-design-expert`, `/ux-design-expert.md` -> `.aiox-core/development/agents/ux-design-expert.md`

### Squad: Synthetic Intelligence Factory (SIF)
- `@sif-factory`, `/sif-factory` -> `squads/synthetic-intelligence-factory/agents/factory.md`
- `@sif-extractor`, `/sif-extractor` -> `squads/synthetic-intelligence-factory/agents/extractor.md`
- `@sif-assembler`, `/sif-assembler` -> `squads/synthetic-intelligence-factory/agents/assembler.md`
- `@sif-validator`, `/sif-validator` -> `squads/synthetic-intelligence-factory/agents/validator.md`
- `@sif-calibrator`, `/sif-calibrator` -> `squads/synthetic-intelligence-factory/agents/calibrator.md`
- `@sif-meta`, `/sif-meta` -> `squads/synthetic-intelligence-factory/agents/meta.md`

### Squad: Nirvana Squad Creator (NSC)
- `@nsc-orchestrator`, `/nsc-orchestrator` -> `squads/nirvana-squad-creator/agents/squad-orchestrator.md`
- `@nsc-analyzer`, `/nsc-analyzer` -> `squads/nirvana-squad-creator/agents/squad-analyzer.md`
- `@nsc-agent-creator`, `/nsc-agent-creator` -> `squads/nirvana-squad-creator/agents/squad-agent-creator.md`
- `@nsc-validator`, `/nsc-validator` -> `squads/nirvana-squad-creator/agents/squad-validator.md`

### Squad: Ultimate Landing Page (ULP)
- `@ulp-strategist`, `/ulp-strategist` -> `squads/ultimate-landingpage/agents/lp-strategist.md`
- `@ulp-copywriter`, `/ulp-copywriter` -> `squads/ultimate-landingpage/agents/lp-copywriter.md`
- `@ulp-design-architect`, `/ulp-design-architect` -> `squads/ultimate-landingpage/agents/lp-design-architect.md`
- `@ulp-frontend-dev`, `/ulp-frontend-dev` -> `squads/ultimate-landingpage/agents/lp-frontend-dev.md`
- `@ulp-reviewer`, `/ulp-reviewer` -> `squads/ultimate-landingpage/agents/lp-reviewer.md`

### Squad: Squads Genius Apex (APEX)
Focado em Context Engineering e Destilação de Conhecimento de Elite.
- `@apex-orquestrista`, `/apex-orquestrista` -> `squads/squads-genius-apex/agents/apex-orquestrista.md`
- `@apex-maven`, `/apex-maven` -> `squads/squads-genius-apex/agents/maven-arquiteta.md`
- `@apex-spark`, `/apex-spark` -> `squads/squads-genius-apex/agents/spark-alquimista.md`
- `@apex-trim`, `/apex-trim` -> `squads/squads-genius-apex/agents/trim-escultor.md`
- `@apex-vigil`, `/apex-vigil` -> `squads/squads-genius-apex/agents/vigil-validadora.md`

### Squad: Skeptic Protocol (SKEPTIC)
Red Teaming, Validação de Falhas e Robustez Extrema.
- `@skeptic-orchestrator`, `/skeptic-orchestrator` -> `squads/skeptic-protocol/agents/skeptic-orchestrator.md`
- `@skeptic-redteamer`, `/skeptic-redteamer` -> `squads/skeptic-protocol/agents/red-teamer.md`
- `@skeptic-predictor`, `/skeptic-predictor` -> `squads/skeptic-protocol/agents/failure-predictor.md`
- `@skeptic-tester`, `/skeptic-tester` -> `squads/skeptic-protocol/agents/test-engineer.md`
- `@skeptic-solution`, `/skeptic-solution` -> `squads/skeptic-protocol/agents/solution-implementer.md`

### Technical Skills: Squad Engine
- `squad-loader` -> `scripts/squad-loader/skills/squad-loader/SKILL.md`
- `squad-parser` -> `scripts/squad-loader/lib/squad-parser.ts`
- `agent-adapter` -> `scripts/squad-loader/lib/agent-adapter.ts`

Resposta esperada ao ativar atalho:
1. Confirmar agente ativado
2. Mostrar 3-6 comandos principais (`*help`, etc.)
3. Seguir na persona do agente

---

## LOGOS-X Integration (Hermes & Gemini)

### Executor Externo: Hermes Agent
O Hermes Agent opera como o braço executor do LOGOS-X para interações fora do CLI.
- **Comando:** `Logos` (PowerShell Alias) ou `hermes` (Direct)
- **Localização:** `~/.hermes/` e `%LOCALAPPDATA%/hermes/hermes-agent`
- **Capacidades:** Web Browsing, E-mail Automation, Terminal UI, Multimedia generation.

### Leis do Sistema LOGOS-X (Protocolo Prime)
As seguintes leis governam a interação entre o Agente (Gemini), o Executor (Hermes) e o Usuário:

- **Lei 9: State Snapshot:** Instalações críticas exigem `git commit` prévio ("PRE-INSTALL LOCK").
- **Lei 10: Agent Synergy:** O LOGOS-X tem autoridade para invocar Skills do Hermes.
- **Lei 11: Atomic Modularity:** Novas skills devem ser módulos isolados (estilo `gemini-skills`).
- **Lei 12: Visual Audit (Logos-Vision):** Autorização para captura de tela/vídeo para diagnóstico visual.

### Upgrade Status (360 Analysis)
- **Fundação:** `aistudio-repository-template` assimilado (Modularidade).
- **Skills:** `gemini-skills` mapeado para integração futura.
- **Visão:** `veo-3-nano-banana` habilitou a Lei 12.
