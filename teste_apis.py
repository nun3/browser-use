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

def testar_deepseek():
    """Testa a API do DeepSeek"""
    try:
        from browser_use import ChatOpenAI
        api_key = os.getenv('DEEPSEEK_API_KEY')
        if not api_key or api_key == 'your_deepseek_api_key_here':
            print("❌ DEEPSEEK_API_KEY não configurada no config.env")
            return False
        
        print(f"🔑 Chave DeepSeek encontrada: {api_key[:10]}...")
        llm = ChatOpenAI(
            model="deepseek-chat",
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        print("✅ DeepSeek configurado com sucesso!")
        return True
    except ImportError:
        print("❌ Erro: ChatOpenAI não disponível. Instale: pip install openai")
        return False
    except Exception as e:
        print(f"❌ Erro com DeepSeek: {e}")
        return False

def testar_openai():
    """Testa a API do OpenAI"""
    try:
        from browser_use import ChatOpenAI
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or api_key == 'your_openai_api_key_here':
            print("❌ OPENAI_API_KEY não configurada no .env")
            return False
        
        print(f"🔑 Chave OpenAI encontrada: {api_key[:10]}...")
        llm = ChatOpenAI(model="gpt-4")
        print("✅ OpenAI configurado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro com OpenAI: {e}")
        return False

def testar_anthropic():
    """Testa a API do Anthropic"""
    try:
        from browser_use import ChatAnthropic
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key or api_key == 'your_anthropic_api_key_here':
            print("❌ ANTHROPIC_API_KEY não configurada no .env")
            return False
        
        print(f"🔑 Chave Anthropic encontrada: {api_key[:10]}...")
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
        print("✅ Anthropic configurado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro com Anthropic: {e}")
        return False

def main():
    print("🧪 Testando configurações de API...\n")
    
    print("1. Testando Google Gemini:")
    gemini_ok = testar_gemini()
    print()
    
    print("2. Testando DeepSeek:")
    deepseek_ok = testar_deepseek()
    print()
    
    print("3. Testando OpenAI:")
    openai_ok = testar_openai()
    print()
    
    print("4. Testando Anthropic:")
    anthropic_ok = testar_anthropic()
    print()
    
    print("📊 Resumo:")
    print(f"   Google Gemini: {'✅' if gemini_ok else '❌'}")
    print(f"   DeepSeek: {'✅' if deepseek_ok else '❌'}")
    print(f"   OpenAI: {'✅' if openai_ok else '❌'}")
    print(f"   Anthropic: {'✅' if anthropic_ok else '❌'}")
    
    if not any([gemini_ok, deepseek_ok, openai_ok, anthropic_ok]):
        print("\n⚠️  Nenhuma API configurada corretamente!")
        print("   Configure pelo menos uma API no arquivo config.env")
    else:
        print("\n🎉 Pelo menos uma API está funcionando!")

if __name__ == "__main__":
    main()
