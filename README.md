# Projeto Browser Use

Este projeto utiliza o Browser Use para automação de navegador com IA, configurado para usar o Google Gemini como modelo de linguagem.

## Configuração

### 1. Ambiente Virtual
O projeto já está configurado com um ambiente virtual Python 3.12 usando uv.

### 2. Dependências
Todas as dependências já foram instaladas:
- `browser-use`: Framework principal
- `playwright`: Para automação do navegador
- `python-dotenv`: Para carregar variáveis de ambiente

### 3. Configuração da API
1. Edite o arquivo `.env`
2. Substitua `your_gemini_api_key_here` pela sua chave da API do Google Gemini
3. Obtenha sua chave em: https://aistudio.google.com/app/apikey

## Como Usar

### Ativar o Ambiente Virtual
```bash
# Windows (Git Bash)
source .venv/Scripts/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### Executar o Agente
```bash
python agent.py
```

## Personalização

### Modificar a Tarefa
Edite a variável `task` no arquivo `agent.py`:

```python
task = "Sua tarefa personalizada aqui"
```

### Usar Outras APIs
Para usar OpenAI ou Anthropic, descomente as linhas correspondentes no `.env` e modifique o código:

```python
# Para OpenAI
from browser_use import ChatOpenAI
llm = ChatOpenAI(model="gpt-4")

# Para Anthropic
from browser_use import ChatAnthropic
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
```

## Exemplos de Tarefas

- "Encontre o preço atual do Bitcoin"
- "Pesquise por 'Python automation' no Google"
- "Acesse o GitHub e encontre repositórios populares de IA"
- "Navegue até o site de notícias e encontre a manchete principal"

## Troubleshooting

- Certifique-se de que a chave da API está correta no arquivo `.env`
- Verifique se o ambiente virtual está ativado
- Se houver problemas com o Playwright, execute: `uvx playwright install chromium --with-deps`
