# [SCHEMA DEFINITION: Knowledge Beads v1.0]

Este schema define como as informações são indexadas no Núcleo de Memória.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `bead_id` | UUID | Identificador único da pérola. |
| `content` | String | O sinal puro da informação (máx 500 tokens). |
| `squad_source` | Enum | Qual squad gerou a informação. |
| `confidence` | Float | Score de veracidade (0.0 a 1.0). |
| `tags` | List | Etiquetas semânticas para indexação. |
| `timestamp` | ISO8601 | Data e hora da criação. |
| `law_compliance` | List | Quais leis do Protocolo PRIME validaram a Bead. |

## ## Regras de Integridade
1. Proibida a entrada de duplicatas (Hash Check).
2. Cada Bead deve ser atômica (um único conceito).
3. A fonte (URL/Documento) deve estar presente nos metadados.
