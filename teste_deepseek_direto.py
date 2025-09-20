"""
Teste direto da API DeepSeek usando requests
"""

import requests
import json
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
load_dotenv('config.env')

def testar_deepseek_direto():
    """Testa a API DeepSeek diretamente"""
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key or api_key == 'your_deepseek_api_key_here':
        print("❌ DEEPSEEK_API_KEY não configurada")
        return False
    
    print(f"🔑 Testando chave: {api_key[:10]}...")
    
    # URL da API DeepSeek
    url = "https://api.deepseek.com/v1/chat/completions"
    
    # Headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    # Dados da requisição
    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": "Olá! Você está funcionando? Responda apenas 'Sim, estou funcionando!'"
            }
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    try:
        print("🚀 Enviando requisição para a API DeepSeek...")
        response = requests.post(url, headers=headers, json=data)
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API DeepSeek funcionando corretamente!")
            print(f"📝 Resposta: {result['choices'][0]['message']['content']}")
            return True
        else:
            print(f"❌ Erro na API: {response.status_code}")
            print(f"📄 Resposta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testando API DeepSeek diretamente...")
    print("=" * 50)
    
    sucesso = testar_deepseek_direto()
    
    print("=" * 50)
    if sucesso:
        print("🎉 DeepSeek está funcionando perfeitamente!")
    else:
        print("❌ Problema com a configuração da DeepSeek")


