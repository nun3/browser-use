# Projeto Browser Use

Este projeto utiliza o Browser Use para automação de navegador com IA, configurado para usar o Google Gemini como modelo de linguagem.

## Configuração

### 1. Ambiente Virtual
O projeto utiliza um ambiente virtual Python (venv) para isolar as dependências.

#### Configuração Automática (Recomendada)
Execute um dos scripts de configuração:

**Windows:**
```bash
setup_venv.bat
```

**Linux/Mac:**
```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

#### Configuração Manual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Instalar navegadores do Playwright
playwright install chromium
```

### 2. Dependências
As dependências estão listadas no arquivo `requirements.txt`:
- `browser-use`: Framework principal
- `playwright`: Para automação do navegador
- `python-dotenv`: Para carregar variáveis de ambiente
- `google-generativeai`: Para Google Gemini
- `openai`: Para DeepSeek e OpenAI
- `anthropic`: Para Claude (opcional)

### 3. Configuração da API
1. Copie o arquivo `config.env` para `.env`
2. Configure suas chaves de API:
   - **Google Gemini:** Substitua `your_gemini_api_key_here` pela sua chave
   - **DeepSeek:** Substitua `your_deepseek_api_key_here` pela sua chave
3. Obtenha suas chaves:
   - **Gemini:** https://aistudio.google.com/app/apikey
   - **DeepSeek:** https://platform.deepseek.com/api_keys

## Como Usar

### Ativar o Ambiente Virtual
```bash
# Windows (Git Bash/PowerShell)
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**Importante:** Sempre ative o ambiente virtual antes de executar os scripts!

### Executar o Agente

#### Opção 1: Agente Universal (escolhe automaticamente)
```bash
python agentUniversal.py
```

#### Opção 2: Agente com Google Gemini
```bash
python agent.py
```

#### Opção 3: Agente com DeepSeek
```bash
python agentDeepSeek.py
```

## Personalização

### Modificar a Tarefa
Edite a variável `task` no arquivo `agent.py`:

```python
task = "Sua tarefa personalizada aqui"
```

### Configurar Modelo Padrão
No arquivo `.env`, defina qual modelo usar por padrão:

```env
# Para usar Gemini (padrão)
DEFAULT_MODEL=gemini

# Para usar DeepSeek
DEFAULT_MODEL=deepseek
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

### Problemas Comuns

- **Chave da API não configurada:** Certifique-se de que as chaves estão corretas no arquivo `.env`
- **Ambiente virtual não ativado:** Sempre ative o ambiente virtual antes de executar:
  ```bash
  # Windows
  venv\Scripts\activate
  # Linux/Mac
  source venv/bin/activate
  ```
- **Dependências não instaladas:** Execute `pip install -r requirements.txt`
- **Playwright:** Se houver problemas, execute: `playwright install chromium`
- **DeepSeek não funciona:** A dependência `openai` já está incluída no requirements.txt


### Verificar Configuração
Execute o script de teste para verificar se as APIs estão funcionando:
```bash
python teste_apis.py
```
