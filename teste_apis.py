"""
Script para testar diferentes APIs do Browser Use
"""

import os
from dotenv import load_dotenv

load_dotenv()

def testar_gemini():
    """Testa a API do Google Gemini"""
    try:
        from browser_use import ChatGoogle
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key or api_key == 'your_gemini_api_key_here':
            print("❌ GEMINI_API_KEY não configurada no .env")
            return False
        
        print(f"🔑 Chave Gemini encontrada: {api_key[:10]}...")
        llm = ChatGoogle(model="gemini-2.0-flash-exp")
        print("✅ Google Gemini configurado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro com Google Gemini: {e}")
        return False

def testar_openai():
    """Testa a API do OpenAI GPT"""
    try:
        from browser_use import ChatOpenAI
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or api_key == 'your_openai_api_key_here':
            print("❌ OPENAI_API_KEY não configurada no config.env")
            return False
        
        print(f"🔑 Chave OpenAI encontrada: {api_key[:10]}...")
        llm = ChatOpenAI(
            model="gpt-4o",
            api_key=api_key
        )
        print("✅ OpenAI GPT configurado com sucesso!")
        return True
    except ImportError:
        print("❌ Erro: ChatOpenAI não disponível. Instale: pip install openai")
        return False
    except Exception as e:
        print(f"❌ Erro com OpenAI GPT: {e}")
        return False

def main():
    print("🧪 Testando configurações de API...\n")
    
    print("1. Testando Google Gemini:")
    gemini_ok = testar_gemini()
    print()
    
    print("2. Testando OpenAI GPT:")
    openai_ok = testar_openai()
    print()
    
    print("📊 Resumo:")
    print(f"   Google Gemini: {'✅' if gemini_ok else '❌'}")
    print(f"   OpenAI GPT: {'✅' if openai_ok else '❌'}")
    
    if not any([gemini_ok, openai_ok]):
        print("\n⚠️  Nenhuma API configurada corretamente!")
        print("   Configure pelo menos uma API no arquivo config.env")
    else:
        print("\n🎉 Pelo menos uma API está funcionando!")

if __name__ == "__main__":
    main()