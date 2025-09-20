# 🚀 Configuração do DeepSeek no Browser Use

## 📋 Visão Geral
Este guia explica como configurar e usar o DeepSeek como modelo de IA no projeto Browser Use.

## 🔑 Obter Chave da API

### 1. Acesse a Plataforma DeepSeek
- Vá para: https://platform.deepseek.com/api_keys
- Faça login ou crie uma conta

### 2. Criar Nova Chave
- Clique em "Create API Key"
- Dê um nome para sua chave (ex: "Browser Use Project")
- Copie a chave gerada

## ⚙️ Configuração

### 1. Instalar Dependências
```bash
pip install openai
```

### 2. Configurar Variáveis de Ambiente
Edite o arquivo `config.env`:
```env
# DeepSeek
DEEPSEEK_API_KEY=sua_chave_aqui

# Modelo padrão
DEFAULT_MODEL=deepseek
```

### 3. Copiar para .env
```bash
cp config.env .env
```

## 🎯 Como Usar

### Opção 1: Agente Universal (Automático)
```bash
python agentUniversal.py
```
O agente escolherá automaticamente baseado na configuração `DEFAULT_MODEL`.

### Opção 2: Agente Exclusivo DeepSeek
```bash
python agentDeepSeek.py
```
Usa exclusivamente o DeepSeek.

## 🧪 Testar Configuração
```bash
python teste_apis.py
```

## 📊 Vantagens do DeepSeek

- **Custo-benefício:** Preços competitivos
- **Performance:** Boa qualidade de resposta
- **Compatibilidade:** API compatível com OpenAI
- **Disponibilidade:** Alta disponibilidade

## 🔧 Configurações Avançadas

### Personalizar Parâmetros
No arquivo `agentDeepSeek.py`, você pode ajustar:

```python
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.7,        # Criatividade (0-1)
    max_tokens=4000,        # Tamanho da resposta
    timeout=30              # Timeout em segundos
)
```

### Modelos Disponíveis
- `deepseek-chat` (recomendado)
- `deepseek-coder` (para código)

## 🚨 Troubleshooting

### Erro: "ChatOpenAI não disponível"
```bash
pip install openai
```

### Erro: "API Key inválida"
- Verifique se a chave está correta
- Confirme se a conta tem créditos
- Teste a chave em: https://platform.deepseek.com/api_keys

### Timeout de Conexão
- Verifique sua conexão com a internet
- Tente aumentar o timeout na configuração

## 📈 Monitoramento

### Verificar Uso da API
- Acesse: https://platform.deepseek.com/usage
- Monitore créditos e custos

### Logs de Execução
Os logs são salvos em:
```
evidencias/teste_deepseek_YYYYMMDD_HHMMSS/
├── evidencias_teste_deepseek_YYYYMMDD_HHMMSS.txt
└── relatorio_detalhado_deepseek_YYYYMMDD_HHMMSS.txt
```

## 🔄 Alternando Entre Modelos

### Para usar Gemini:
```env
DEFAULT_MODEL=gemini
```

### Para usar DeepSeek:
```env
DEFAULT_MODEL=deepseek
```

## 💡 Dicas

1. **Teste primeiro:** Use `python teste_apis.py` antes de executar tarefas complexas
2. **Monitore custos:** Acompanhe o uso da API regularmente
3. **Backup de chaves:** Mantenha suas chaves seguras
4. **Ambiente virtual:** Sempre use ambiente virtual para isolamento

## 🆘 Suporte

- **Documentação DeepSeek:** https://platform.deepseek.com/docs
- **Issues do Projeto:** Abra uma issue no repositório
- **Comunidade:** Discord/Telegram do DeepSeek


