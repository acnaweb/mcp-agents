
# MCP-Agent 🚀

**MCP-Agent** é um framework leve e composável para construir agentes de IA usando o **Model Context Protocol (MCP)**. Ele implementa padrões de workflows eficazes ("Building Effective Agents") e oferece suporte multiplataforma, incluindo “Swarm” da OpenAI.

## 📦 Instalação

**Usando `pip`:**
```bash
pip install mcp-agent
```

**Em modo de desenvolvimento:**
```bash
git clone https://github.com/acnaweb/mcp-agents.git
cd mcp-agents
pip install -e .
```

## 🚀 Exemplos práticos

### 1. Quickstart — Finder Agent
Localize e leia arquivos/local ou via URL, e depois resuma ou poste como tweet:

```python
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM
import asyncio

app = MCPApp(name="hello_world_agent")

async def main():
    async with app.run() as m:
        agent = Agent(
            name="finder",
            instruction="Você pode ler arquivos e URLs. Traga o conteúdo.",
            server_names=["filesystem", "fetch"],
        )
        async with agent:
            llm = await agent.attach_llm(OpenAIAugmentedLLM)
            print(await llm.generate_str("Leia README.md e mostre as duas primeiras linhas"))
            print(await llm.generate_str("Resuma isso em um tweet de 128 caracteres"))

if __name__ == "__main__":
    asyncio.run(main())
```

🔧 Certifique-se de configurar `mcp_agent.config.yaml` com parâmetros de execução e servidores MCP.

### 2. Workflows avançados

- **AugmentedLLM**: acesso a MCP servers + LLM
- **Router**, **IntentClassifier**: direção de tarefas com base em embeddings ou LLM
- **Evaluator‑Optimizer**: ciclo de refinamento de saídas
- **Swarm**: orquestração multi‑agentes em paralelo/composição

## 🧱 Estrutura do Projeto

```
mcp-agents/
├─ examples/             # Exemplos de aplicações (incluindo RAG, Gmail, Streamlit)
├─ src/mcp_agent/        # Core: agentes, workflows, MCPApp, conectores
├─ tests/                # Testes automatizados
├─ mcp_agent.config.yaml # Configuração de execução e servidores MCP
├─ pyproject.toml
├─ Makefile
├─ LICENSE
└─ README.md
```

## 🎯 Vantagens

- Totalmente **composável**: combine workflows, LLMs e agentes
- **Ligado ao padrão MCP**, permitindo integração com diversos serviços (filesystem, fetch, Gmail, Qdrant, etc.)
- **Multi‑modelo**: compatível com OpenAI, Anthropic e outros
- **Orquestração avançada**: implementa padrões elaborados como Swarm

## 📚 Exemplos notáveis

- Cliente MCP para **Claude Desktop**
- **Streamlit**: agentes de Gmail e chatbot RAG
- **Marimo**: notebooks reativos com agentes inteligentes
- **CLI “Swarm”**: multi‑agentes para triagem de atendimento

(exemplos disponíveis em `examples/`)

## 💡 Como contribuir

- Abra issues ou pull requests
- Consulte `CONTRIBUTING.md`
- Exemplos são bem-vindos para novos MCP‑servers ou padrões

## 🛣 Roadmap

- **Execução durável** (persistent workflows)
- **Memória de longo prazo**
- **Suporte a streaming incremental**
- Maior número de **capacidades MCP** (notificações, recursos, prompts)

## 📄 Licença

- License: Apache‑2.0
