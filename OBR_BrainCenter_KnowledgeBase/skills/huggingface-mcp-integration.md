# SKILL: Hugging Face MCP Integration (V1.0)

Capacidade de orquestração e descoberta de modelos, datasets e Spaces via Model Context Protocol (MCP).

## Capacidades Técnicas (Upgrade V2.0)
- **Multi-Server Integration:** Suporte para consolidar ferramentas de múltiplos servidores MCP em um único contexto de execução.
- **CodeAgent Pattern:** Preferência por execução via código gerado por IA para chamadas de ferramentas complexas.
- **Lifecycle Management:** Uso de gerenciadores de contexto para abertura e fechamento seguro de processos de servidor.
- **Sandboxed Python Executor:** Integração com o ecossistema `smolagents` para execução segura.

## Configuração Mandatória
O servidor deve ser invocado via `npx` com o `HF_TOKEN` protegido em variáveis de ambiente locais.
`npx -y @huggingface/mcp-server`
### Ferramentas Detectadas via NPM:
- **search_models:** Localiza modelos no Hub.
- **search_datasets:** Localiza datasets.
- **search_papers:** Busca artigos no arXiv via HF.
- **gradio_tool:** Invoca qualquer Space como ferramenta.

