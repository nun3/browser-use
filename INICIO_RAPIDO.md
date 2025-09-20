# 🚀 Início Rápido

## 1. Configuração Automática (Recomendada)

### Windows
```bash
setup_venv.bat
```

### Linux/Mac
```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

## 2. Configuração Manual

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

# Instalar navegadores
playwright install chromium
```

## 3. Configurar APIs

1. Copie `config.env` para `.env`
2. Configure suas chaves de API no arquivo `.env`

## 4. Testar Configuração

```bash
python test_venv.py
```

## 5. Executar Agentes

```bash
# Sempre ative o ambiente virtual primeiro!
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Depois execute:
python agentUniversal.py    # Agente universal
python agent.py            # Agente Gemini
python agentDeepSeek.py    # Agente DeepSeek
```

## ⚠️ Importante

- **SEMPRE** ative o ambiente virtual antes de executar os scripts
- Se der erro de dependências, execute: `pip install -r requirements.txt`
- Se der erro do Playwright, execute: `playwright install chromium`
