# SKILL: Hugging Face MCP Integration (V1.0)

Capacidade de orquestração e descoberta de modelos, datasets e Spaces via Model Context Protocol (MCP).

## Capacidades Técnicas
- **Model Search:** Busca semântica e por tags em 1.2M+ de modelos.
- **Dataset Explorer:** Análise de estruturas de dados e metadados de datasets.
- **Space Discovery:** Interação com aplicativos Gradio como ferramentas funcionais.
- **Safe Python Execution:** Execução local segura de scripts gerados por IA via `smolagents`.

## Configuração Mandatória
O servidor deve ser invocado via `npx` com o `HF_TOKEN` protegido em variáveis de ambiente locais.
`npx -y @huggingface/mcp-server`
### Ferramentas Detectadas via NPM:
- **search_models:** Localiza modelos no Hub.
- **search_datasets:** Localiza datasets.
- **search_papers:** Busca artigos no arXiv via HF.
- **gradio_tool:** Invoca qualquer Space como ferramenta.

