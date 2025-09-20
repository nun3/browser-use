"""
Agente Browser Use com suporte completo para OpenAI GPT
Versão especializada para usar exclusivamente o OpenAI GPT
"""

import os
from dotenv import load_dotenv
import asyncio
import datetime
import base64
from pathlib import Path

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
load_dotenv('config.env')

def salvar_evidencia(evidencias_dir, conteudo, nome_arquivo):
    """
    Salva evidências em arquivo txt
    """
    arquivo_evidencia = Path(evidencias_dir) / f"{nome_arquivo}.txt"
    with open(arquivo_evidencia, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    print(f"Evidência salva: {arquivo_evidencia}")

def salvar_screenshot(evidencias_dir, screenshot_data, nome_arquivo):
    """
    Salva screenshot em arquivo PNG
    """
    if screenshot_data:
        # Remove o prefixo data:image/png;base64, se existir
        if ',' in screenshot_data:
            screenshot_data = screenshot_data.split(',')[1]
        
        # Decodifica base64 e salva
        screenshot_bytes = base64.b64decode(screenshot_data)
        arquivo_screenshot = Path(evidencias_dir) / f"{nome_arquivo}.png"
        with open(arquivo_screenshot, 'wb') as f:
            f.write(screenshot_bytes)
        print(f"Screenshot salvo: {arquivo_screenshot}")

def configurar_gpt():
    """
    Configura o OpenAI GPT exclusivamente
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("❌ OPENAI_API_KEY não configurada no config.env")
        print("📝 Configure sua chave da OpenAI em: https://platform.openai.com/api-keys")
        return None
    
    try:
        from browser_use import ChatOpenAI
        print("🤖 Configurando OpenAI GPT...")
        print(f"🔑 Chave encontrada: {api_key[:10]}...")
        
        modelo = os.getenv('OPENAI_MODEL', 'gpt-4o')
        llm = ChatOpenAI(
            model=modelo,
            api_key=api_key,
            temperature=0.7
        )
        print(f"✅ OpenAI GPT configurado com sucesso! Modelo: {modelo}")
        return llm
        
    except ImportError:
        print("❌ Erro: ChatOpenAI não disponível")
        print("📦 Instale com: pip install openai")
        return None
    except Exception as e:
        print(f"❌ Erro ao configurar OpenAI GPT: {e}")
        return None

async def main():
    """
    Função principal que executa o agente com OpenAI GPT
    """
    print("🚀 Iniciando agente Browser Use com OpenAI GPT...")
    
    # Configura o OpenAI GPT
    llm = configurar_gpt()
    if not llm:
        print("❌ Não foi possível configurar o OpenAI GPT")
        return
    
    from browser_use import Agent
    
    # Define a tarefa que o agente deve executar
    task = ("Analise completamente a aplicação Bibliotech em https://bibliotechapp.vercel.app/login "
            "Realize login com email: thegoldengrace@gmail.com e senha: 123456 "
            "Explore todas as funcionalidades disponíveis: navegação, empréstimos, devoluções, reservas, perfil do usuário, etc. "
            "Teste diferentes cenários: buscar livros, filtrar, ordenar, paginar, etc. "
            "Identifique todas as funcionalidades e fluxos da aplicação "
            "Gere cenários de teste em formato Gherkin (Given-When-Then) para cada funcionalidade descoberta "
            "Inclua cenários positivos e negativos para cada feature "
            "Organize os cenários por funcionalidade (Login, Busca de Livros, Empréstimo, Devolução, Reserva, Perfil, etc.) "
            "Seja detalhado e cubra todos os casos de uso possíveis ")
    
    # Prompt para geração de relatório detalhado
    prompt_relatorio = f"""
            Com base na exploração autônoma realizada no Bibliotech em {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}:
            
            Gere um relatório detalhado incluindo:
            1. **RESUMO DOS TESTES EXECUTADOS:** Lista de ações realizadas com status (sucesso/falha).
            2. **FUNCIONALIDADES DESCOBERTAS:** Descrição detalhada de todas as funcionalidades encontradas.
            3. **FLUXOS IDENTIFICADOS:** Mapeamento dos principais fluxos de usuário.
            4. **PROBLEMAS IDENTIFICADOS:** Bugs ou falhas encontradas.
            5. **ANÁLISE DE USABILIDADE:** Facilidade de navegação e clareza.
            6. **ANÁLISE DE SEGURANÇA:** Funcionamento de login/logout e proteções.
            7. **CENÁRIOS GHERKIN COMPLETOS:** Gere cenários detalhados em formato Gherkin para TODAS as funcionalidades descobertas, incluindo:
               - Cenários positivos (happy path)
               - Cenários negativos (edge cases)
               - Cenários de erro
               - Cenários de validação
               - Organize por funcionalidade (Login, Busca, Empréstimo, Devolução, Reserva, Perfil, etc.)
            8. **COBERTURA DE TESTES:** Mapeamento de quais funcionalidades precisam de mais testes.
            9. **RECOMENDAÇÕES:** Melhorias sugeridas baseadas na análise.
            10. **SCORE GERAL:** Avaliação de 1-10 por aspecto e geral.
            """
    
    # Criar pasta de evidências com timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    evidencias_dir = f"evidencias/teste_gpt_{timestamp}"
    os.makedirs(evidencias_dir, exist_ok=True)
    
    print(f"📁 Evidências serão salvas em: {evidencias_dir}")
    print(f"🎯 Tarefa: {task[:100]}...")
    
    # Cria o agente com a tarefa e o LLM
    agent = Agent(task=task, llm=llm)
    
    # Executa o agente e captura o resultado
    resultado = await agent.run()
    
    # Gera relatório detalhado usando o LLM
    print("\nGerando relatório detalhado...")
    relatorio_prompt = f"""
{prompt_relatorio}

DADOS DA EXECUÇÃO:
- Tarefa: {task}
- Resultado: {resultado}
- Data/Hora: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

Por favor, gere um relatório completo baseado nos dados acima.
"""
    
    # Gera o relatório usando o LLM
    try:
        relatorio_resposta = await llm.ainvoke(relatorio_prompt)
        relatorio_detalhado = relatorio_resposta.content
    except Exception as e:
        relatorio_detalhado = f"Erro ao gerar relatório: {str(e)}"
    
    # Salva evidências do teste
    evidencia_conteudo = f"""
TESTE AUTOMATIZADO - BIBLIOTECH COM OPENAI GPT
Data/Hora: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Timestamp: {timestamp}

TAREFA EXECUTADA:
{task}

RESULTADO DA EXECUÇÃO:
{resultado}

RELATÓRIO DETALHADO:
{relatorio_detalhado}

PROMPT DE RELATÓRIO ORIGINAL:
{prompt_relatorio}
"""
    
    # Salva as evidências em arquivo txt
    salvar_evidencia(evidencias_dir, evidencia_conteudo, f"evidencias_teste_gpt_{timestamp}")
    
    # Salva também apenas o relatório detalhado
    salvar_evidencia(evidencias_dir, relatorio_detalhado, f"relatorio_detalhado_gpt_{timestamp}")
    
    print(f"\nTeste concluído! Evidências salvas em: {evidencias_dir}")
    print("Arquivos gerados:")
    print(f"- evidencias_teste_gpt_{timestamp}.txt")
    print(f"- relatorio_detalhado_gpt_{timestamp}.txt")
    print(f"- Screenshots (se capturados)")

if __name__ == "__main__":
    # Executa a função principal de forma assíncrona
    asyncio.run(main())
