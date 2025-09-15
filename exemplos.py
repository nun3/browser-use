"""
Exemplos de uso do Browser Use com diferentes tarefas
"""

from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def exemplo_pesquisa_google():
    """Exemplo: Pesquisar no Google"""
    llm = ChatGoogle(model="gemini-2.0-flash-exp")
    task = "Pesquise por 'Python automation' no Google e me diga os primeiros 3 resultados"
    agent = Agent(task=task, llm=llm)
    await agent.run()

async def exemplo_noticias():
    """Exemplo: Buscar notícias"""
    llm = ChatGoogle(model="gemini-2.0-flash-exp")
    task = "Vá até o site de notícias e encontre a manchete principal de tecnologia"
    agent = Agent(task=task, llm=llm)
    await agent.run()

async def exemplo_github():
    """Exemplo: Navegar no GitHub"""
    llm = ChatGoogle(model="gemini-2.0-flash-exp")
    task = "Acesse o GitHub e encontre os 5 repositórios mais populares relacionados a 'browser automation'"
    agent = Agent(task=task, llm=llm)
    await agent.run()

async def exemplo_criptomoedas():
    """Exemplo: Verificar preços de criptomoedas"""
    llm = ChatGoogle(model="gemini-2.0-flash-exp")
    task = "Encontre o preço atual do Bitcoin e Ethereum"
    agent = Agent(task=task, llm=llm)
    await agent.run()

async def exemplo_show_hn():
    """Exemplo: Verificar Show HN"""
    llm = ChatGoogle(model="gemini-2.0-flash-exp")
    task = "Encontre o post número 1 no Show HN"
    agent = Agent(task=task, llm=llm)
    await agent.run()

async def main():
    """Menu de exemplos"""
    print("Escolha um exemplo para executar:")
    print("1. Pesquisa no Google")
    print("2. Buscar notícias")
    print("3. Navegar no GitHub")
    print("4. Verificar criptomoedas")
    print("5. Verificar Show HN")
    
    escolha = input("Digite o número da opção (1-5): ")
    
    if escolha == "1":
        await exemplo_pesquisa_google()
    elif escolha == "2":
        await exemplo_noticias()
    elif escolha == "3":
        await exemplo_github()
    elif escolha == "4":
        await exemplo_criptomoedas()
    elif escolha == "5":
        await exemplo_show_hn()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    asyncio.run(main())
