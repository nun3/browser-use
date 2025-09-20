import os
from dotenv import load_dotenv
import asyncio
import datetime
from pathlib import Path

# Carrega variáveis de ambiente
load_dotenv()
load_dotenv('config.env')  # Carrega também o arquivo de configuração

def salvar_evidencia(evidencias_dir, conteudo, nome_arquivo):
    arquivo_evidencia = Path(evidencias_dir) / f"{nome_arquivo}.txt"
    with open(arquivo_evidencia, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def configurar_llm():
    """
    Configura o modelo de linguagem baseado nas variáveis de ambiente
    """
    modelo_padrao = os.getenv('DEFAULT_MODEL', 'gemini').lower()
    
    if modelo_padrao == 'gpt':
        return configurar_gpt()
    else:
        return configurar_gemini()

def configurar_gemini():
    """
    Configura o Google Gemini
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == 'your_gemini_api_key_here':
        print("❌ GEMINI_API_KEY não configurada no config.env")
        return None
    
    os.environ['GOOGLE_API_KEY'] = api_key
    from browser_use import ChatGoogle
    modelo = os.getenv('BROWSER_USE_MODEL', 'gemini-2.0-flash-exp')
    print(f"🤖 Usando Google Gemini: {modelo}")
    return ChatGoogle(model=modelo)

def configurar_gpt():
    """
    Configura o OpenAI GPT
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("❌ OPENAI_API_KEY não configurada no config.env")
        return None
    
    try:
        from browser_use import ChatOpenAI
        modelo = os.getenv('OPENAI_MODEL', 'gpt-4o')
        print(f"🤖 Usando OpenAI GPT: {modelo}")
        return ChatOpenAI(
            model=modelo,
            api_key=api_key,
            temperature=0.7
        )
    except ImportError:
        print("❌ Erro: ChatOpenAI não disponível. Instale: pip install openai")
        return None

async def main():
    # Configura o modelo de linguagem
    llm = configurar_llm()
    if not llm:
        print("❌ Não foi possível configurar nenhum modelo de IA")
        return
    
    from browser_use import Agent
    
    task = ("pesquise por 'Python automation' no Google. ")
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    evidencias_dir = f"evidencias/teste_{timestamp}"
    os.makedirs(evidencias_dir, exist_ok=True)
    
    agent = Agent(task=task, llm=llm)
    resultado = await agent.run()
    
    relatorio_prompt = f"""Gere relatório conciso sobre teste no Bibliotech:
1. Ações executadas e status
2. Funcionalidades testadas
3. Problemas encontrados
4. Score geral (1-10)
5. Recomendações principais

Dados: {resultado}"""
    
    try:
        relatorio_resposta = await llm.ainvoke(relatorio_prompt)
        relatorio_detalhado = relatorio_resposta.content
    except Exception:
        try:
            import google.generativeai as genai
            genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(relatorio_prompt)
            relatorio_detalhado = response.text
        except Exception as e:
            relatorio_detalhado = f"Erro ao gerar relatório: {str(e)}"
    
    evidencia_conteudo = f"""TESTE BIBLIOTECH - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

TAREFA: {task}
RESULTADO: {resultado}
RELATÓRIO: {relatorio_detalhado}"""
    
    salvar_evidencia(evidencias_dir, evidencia_conteudo, f"evidencias_teste_{timestamp}")
    salvar_evidencia(evidencias_dir, relatorio_detalhado, f"relatorio_detalhado_{timestamp}")
    
    print(f"Teste concluído - Evidências: {evidencias_dir}")

if __name__ == "__main__":
    asyncio.run(main())
