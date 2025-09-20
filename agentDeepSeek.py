"""
Agente Browser Use com suporte completo para DeepSeek
Versão especializada para usar exclusivamente o DeepSeek
"""

import os
from dotenv import load_dotenv
import asyncio
import datetime
from pathlib import Path

# Carrega variáveis de ambiente
load_dotenv()
load_dotenv('config.env')

def salvar_evidencia(evidencias_dir, conteudo, nome_arquivo):
    """Salva evidências em arquivo de texto"""
    arquivo_evidencia = Path(evidencias_dir) / f"{nome_arquivo}.txt"
    with open(arquivo_evidencia, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def configurar_deepseek():
    """
    Configura o DeepSeek exclusivamente
    """
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key or api_key == 'your_deepseek_api_key_here':
        print("❌ DEEPSEEK_API_KEY não configurada no config.env")
        print("📝 Configure sua chave da DeepSeek em: https://platform.deepseek.com/api_keys")
        return None
    
    try:
        from browser_use import ChatOpenAI
        print("🤖 Configurando DeepSeek...")
        print(f"🔑 Chave encontrada: {api_key[:10]}...")
        
        llm = ChatOpenAI(
            model="deepseek-chat",
            api_key=api_key,
            base_url="https://api.deepseek.com",
            temperature=0.7,
            response_format=None
        )
        print("✅ DeepSeek configurado com sucesso!")
        return llm
        
    except ImportError:
        print("❌ Erro: ChatOpenAI não disponível")
        print("📦 Instale com: pip install openai")
        return None
    except Exception as e:
        print(f"❌ Erro ao configurar DeepSeek: {e}")
        return None

async def main():
    """
    Função principal que executa o agente com DeepSeek
    """
    print("🚀 Iniciando agente Browser Use com DeepSeek...")
    
    # Configura o DeepSeek
    llm = configurar_deepseek()
    if not llm:
        print("❌ Não foi possível configurar o DeepSeek")
        return
    
    from browser_use import Agent
    
    # Define a tarefa que o agente deve executar
    task = ("Execute login em https://bibliotechapp.vercel.app/login com email: thegoldengrace@gmail.com e senha: 123456. "
            "Realize emprestimos de livros, devolva os livros e confirme se foi realizado com sucesso. "
            "E reserve um livro para ver se foi realizado com sucesso. "
            "Seja autônomo e tome decisões inteligentes durante a navegação. "
            "Essa aplicação não é muito responsiva, talvez seja necessário realizar scroll para baixo ou para o lado para encontrar o que deseja.")
    
    # Criar pasta de evidências com timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    evidencias_dir = f"evidencias/teste_deepseek_{timestamp}"
    os.makedirs(evidencias_dir, exist_ok=True)
    
    print(f"📁 Evidências serão salvas em: {evidencias_dir}")
    print(f"🎯 Tarefa: {task[:100]}...")
    
    # Cria e executa o agente
    agent = Agent(task=task, llm=llm)
    
    try:
        print("🔄 Executando agente...")
        resultado = await agent.run()
        
        # Gera relatório usando DeepSeek
        relatorio_prompt = f"""Gere um relatório detalhado sobre o teste realizado no Bibliotech em {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}:

1. **RESUMO DOS TESTES EXECUTADOS:** Lista de ações realizadas com status (sucesso/falha)
2. **FUNCIONALIDADES TESTADAS:** Descrição das funcionalidades exploradas
3. **PROBLEMAS IDENTIFICADOS:** Bugs ou falhas encontradas
4. **ANÁLISE DE USABILIDADE:** Facilidade de navegação e clareza
5. **ANÁLISE DE SEGURANÇA:** Funcionamento de login/logout
6. **RECOMENDAÇÕES:** Melhorias sugeridas
7. **SCORE GERAL:** Avaliação de 1-10 por aspecto e geral
8. **CENÁRIOS DE TESTE EM GHERKIN:** Gere cenários para todas as funcionalidades descobertas

Dados do teste: {resultado}"""
        
        print("📊 Gerando relatório detalhado...")
        try:
            relatorio_resposta = await llm.ainvoke(relatorio_prompt)
            relatorio_detalhado = relatorio_resposta.content
        except Exception as e:
            relatorio_detalhado = f"Erro ao gerar relatório: {str(e)}"
        
        # Salva evidências
        evidencia_conteudo = f"""TESTE BIBLIOTECH COM DEEPSEEK - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

TAREFA: {task}
RESULTADO: {resultado}
RELATÓRIO: {relatorio_detalhado}"""
        
        salvar_evidencia(evidencias_dir, evidencia_conteudo, f"evidencias_teste_deepseek_{timestamp}")
        salvar_evidencia(evidencias_dir, relatorio_detalhado, f"relatorio_detalhado_deepseek_{timestamp}")
        
        print(f"✅ Teste concluído com sucesso!")
        print(f"📁 Evidências salvas em: {evidencias_dir}")
        print(f"📄 Relatório: {relatorio_detalhado[:200]}...")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        evidencia_erro = f"""ERRO NO TESTE DEEPSEEK - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

TAREFA: {task}
ERRO: {str(e)}"""
        salvar_evidencia(evidencias_dir, evidencia_erro, f"erro_teste_deepseek_{timestamp}")

if __name__ == "__main__":
    asyncio.run(main())
