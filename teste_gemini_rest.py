"""
Teste direto da API REST do Google Gemini
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def testar_gemini_rest():
    """Testa a API REST do Google Gemini diretamente"""
    
    # Pega a chave da API do arquivo .env
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == 'your_gemini_api_key_here':
        print("❌ GEMINI_API_KEY não configurada no .env")
        return False
    
    print(f"🔑 Testando chave: {api_key[:10]}...")
    
    # URL da API
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    
    # Headers
    headers = {
        'Content-Type': 'application/json',
        'X-goog-api-key': api_key
    }
    
    # Dados da requisição
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "Explique como a IA funciona em poucas palavras"
                    }
                ]
            }
        ]
    }
    
    try:
        print("🚀 Enviando requisição para a API...")
        response = requests.post(url, headers=headers, json=data)
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API funcionando corretamente!")
            print(f"📝 Resposta: {result['candidates'][0]['content']['parts'][0]['text']}")
            return True
        else:
            print(f"❌ Erro na API: {response.status_code}")
            print(f"📄 Resposta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testando API REST do Google Gemini...\n")
    sucesso = testar_gemini_rest()
    
    if sucesso:
        print("\n🎉 Sua chave da API está funcionando!")
        print("   O problema pode estar na configuração do Browser Use.")
    else:
        print("\n⚠️  Sua chave da API não está funcionando.")
        print("   Verifique se a chave está correta e ativa.")
