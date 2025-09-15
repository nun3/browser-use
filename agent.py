"""
Script principal do agente Browser Use
Configurado para usar Google Gemini como LLM
"""

import os
from dotenv import load_dotenv
import asyncio

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

async def main():
    """
    Função principal que executa o agente
    """
    # Configura a variável de ambiente para a biblioteca google-genai
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key:
        os.environ['GOOGLE_API_KEY'] = api_key
    
    # Importa o ChatGoogle após definir a variável de ambiente
    from browser_use import Agent, ChatGoogle
    
    # Configura o LLM usando Google Gemini
    llm = ChatGoogle(model="gemini-2.0-flash-exp")
    
    # Define a tarefa que o agente deve executar
    task = "Faça um login nesse site https://bibliotechapp.vercel.app/login e me diga se o login foi feito com sucesso usuario é thegoldengrace@gmail.com e a senha é 123456"
    
    # Cria o agente com a tarefa e o LLM
    agent = Agent(task=task, llm=llm)
    
    # Executa o agente
    await agent.run()

if __name__ == "__main__":
    # Executa a função principal de forma assíncrona
    asyncio.run(main())
