"""
Teste simples da DeepSeek para verificar se está funcionando
"""

import os
from dotenv import load_dotenv
import asyncio

# Carrega variáveis de ambiente
load_dotenv()
load_dotenv('config.env')

async def teste_simples():
    """Teste simples da DeepSeek"""
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key or api_key == 'your_deepseek_api_key_here':
        print("❌ DEEPSEEK_API_KEY não configurada")
        return
    
    try:
        from browser_use import ChatOpenAI
        print("🤖 Testando DeepSeek...")
        
        llm = ChatOpenAI(
            model="deepseek-chat",
            api_key=api_key,
            base_url="https://api.deepseek.com",
            temperature=0.7
        )
        
        # Teste simples
        print("📝 Enviando pergunta simples...")
        resposta = await llm.ainvoke("Olá! Você está funcionando? Responda apenas 'Sim, estou funcionando!'")
        
        # Verifica o tipo da resposta
        if hasattr(resposta, 'content'):
            print(f"✅ Resposta da DeepSeek: {resposta.content}")
        elif hasattr(resposta, 'text'):
            print(f"✅ Resposta da DeepSeek: {resposta.text}")
        else:
            print(f"✅ Resposta da DeepSeek: {resposta}")
        print("🎉 DeepSeek está funcionando perfeitamente!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    asyncio.run(teste_simples())
