"""
Agente Browser Use com configuração correta para Google Gemini
"""

import os
from dotenv import load_dotenv
from browser_use import Agent
import asyncio

# Carrega as variáveis de ambiente
load_dotenv()

async def main():
    """
    Função principal com configuração correta do Google Gemini
    """
    try:
        # Verifica se a chave da API está configurada
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key or api_key == 'your_gemini_api_key_here':
            print("❌ Erro: GEMINI_API_KEY não configurada no arquivo .env")
            return
        
        print(f"🔑 Usando chave da API: {api_key[:10]}...")
        
        # Configura a variável de ambiente para a biblioteca google-genai
        os.environ['GOOGLE_API_KEY'] = api_key
        
        # Importa e configura o ChatGoogle após definir a variável de ambiente
        from browser_use import ChatGoogle
        
        # Configura o LLM usando Google Gemini
        llm = ChatGoogle(model="gemini-2.0-flash-exp")
        
        # Define uma tarefa simples para teste
        task = "Vá até o Google e pesquise por 'Python automation'"
        
        print(f"🎯 Tarefa: {task}")
        
        # Cria o agente com a tarefa e o LLM
        agent = Agent(task=task, llm=llm)
        
        print("🚀 Iniciando o agente...")
        
        # Executa o agente
        result = await agent.run()
        
        print("✅ Agente executado com sucesso!")
        print(f"📋 Resultado: {result}")
        
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")
        print(f"📄 Tipo do erro: {type(e).__name__}")
        
        # Sugestões específicas baseadas no erro
        if "API key" in str(e).lower():
            print("\n💡 Sugestões para erro de API key:")
            print("   1. Verifique se GOOGLE_API_KEY está definida corretamente")
            print("   2. Certifique-se de que a chave está ativa no Google AI Studio")
            print("   3. Tente gerar uma nova chave da API")
        elif "model" in str(e).lower():
            print("\n💡 Sugestões para erro de modelo:")
            print("   1. Tente usar 'gemini-2.0-flash' em vez de 'gemini-2.0-flash-exp'")
            print("   2. Verifique se o modelo está disponível na sua região")
        else:
            print("\n💡 Sugestões gerais:")
            print("   1. Verifique sua conexão com a internet")
            print("   2. Tente executar novamente em alguns minutos")

if __name__ == "__main__":
    asyncio.run(main())
