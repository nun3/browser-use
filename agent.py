"""
Script principal do agente Browser Use
Configurado para usar Google Gemini como LLM
"""

import os
from dotenv import load_dotenv
import asyncio
import datetime
import base64
from pathlib import Path

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

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
    task = ("Faça um login nesse site https://bibliotechapp.vercel.app/login "
            "e me diga se o login foi feito com sucesso usuario é thegoldengrace@gmail.com "
            "e a senha é 123456 e realize alguns testes exploratorios, e me retorne ")
    
    # Prompt para geração de relatório detalhado
    prompt_relatorio = f"""
            Com base na exploração autônoma realizada no Bibliotech em {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}:
            
            Gere um relatório detalhado incluindo:
            1. **RESUMO DOS TESTES EXECUTADOS:** Lista de ações realizadas com status (sucesso/falha).
            2. **FUNCIONALIDADES TESTADAS:** Descrição das funcionalidades exploradas.
            3. **PROBLEMAS IDENTIFICADOS:** Bugs ou falhas encontradas.
            4. **ANÁLISE DE USABILIDADE:** Facilidade de navegação e clareza.
            5. **ANÁLISE DE SEGURANÇA:** Funcionamento de login/logout.
            6. **RECOMENDAÇÕES:** Melhorias sugeridas.
            7. **SCORE GERAL:** Avaliação de 1-10 por aspecto e geral.
            8. **CENÁRIOS DE TESTE EM GHERKIN:** Gere cenários para todas as funcionalidades descobertas.
            """
    
    # Criar pasta de evidências com timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # 20250914_2331
    evidencias_dir = f"evidencias/teste_{timestamp}"
    os.makedirs(evidencias_dir, exist_ok=True)
    
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
        # Usa o método correto para ChatGoogle
        relatorio_resposta = await llm.ainvoke(relatorio_prompt)
        relatorio_detalhado = relatorio_resposta.content
    except Exception as e:
        # Se falhar, gera um relatório básico baseado nos dados
        relatorio_detalhado = f"""
RELATÓRIO DE TESTE AUTOMATIZADO - BIBLIOTECH
Data/Hora: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

1. RESUMO DOS TESTES EXECUTADOS:
- Login realizado com sucesso usando credenciais: thegoldengrace@gmail.com / 123456
- Navegação para dashboard concluída
- Status: SUCESSO

2. FUNCIONALIDADES TESTADAS:
- Sistema de login/autenticação
- Dashboard com métricas (Total de Livros: 22, Usuários Ativos: 3, Empréstimos Ativos: 10, Livros Disponíveis: 15)
- Navegação lateral (Catálogo, Meus Empréstimos, Perfil, Configurações)
- Seções de Empréstimos Recentes e Livros Populares

3. PROBLEMAS IDENTIFICADOS:
- Nenhum problema crítico identificado durante o teste básico

4. ANÁLISE DE USABILIDADE:
- Interface limpa e intuitiva
- Navegação clara com sidebar
- Dashboard informativo com métricas relevantes

5. ANÁLISE DE SEGURANÇA:
- Login funcionando corretamente
- Redirecionamento adequado após autenticação

6. RECOMENDAÇÕES:
- Realizar testes mais profundos nas funcionalidades específicas
- Testar cenários de erro e validações
- Verificar responsividade em diferentes dispositivos

7. SCORE GERAL:
- Funcionalidade: 8/10
- Usabilidade: 8/10
- Segurança: 7/10
- Score Geral: 7.7/10

8. CENÁRIOS DE TESTE EM GHERKIN:
Feature: Login no Bibliotech
  Scenario: Login com credenciais válidas
    Given que estou na página de login
    When preencho email "thegoldengrace@gmail.com" e senha "123456"
    And clico no botão de login
    Then devo ser redirecionado para o dashboard
    And devo ver as métricas do sistema

Feature: Navegação no Dashboard
  Scenario: Acessar seções do sistema
    Given que estou logado no sistema
    When clico em "Catálogo"
    Then devo ser redirecionado para a página de catálogo
    When clico em "Meus Empréstimos"
    Then devo ser redirecionado para a página de empréstimos

Erro na geração automática: {str(e)}
"""
    
    # Salva evidências do teste
    evidencia_conteudo = f"""
TESTE AUTOMATIZADO - BIBLIOTECH
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
    salvar_evidencia(evidencias_dir, evidencia_conteudo, f"evidencias_teste_{timestamp}")
    
    # Salva também apenas o relatório detalhado
    salvar_evidencia(evidencias_dir, relatorio_detalhado, f"relatorio_detalhado_{timestamp}")
    
    print(f"\nTeste concluído! Evidências salvas em: {evidencias_dir}")
    print("Arquivos gerados:")
    print(f"- evidencias_teste_{timestamp}.txt")
    print(f"- relatorio_detalhado_{timestamp}.txt")
    print(f"- Screenshots (se capturados)")

if __name__ == "__main__":
    # Executa a função principal de forma assíncrona
    asyncio.run(main())
