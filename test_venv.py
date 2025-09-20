#!/usr/bin/env python3
"""
Script para testar se o ambiente virtual está configurado corretamente
"""

import sys
import os
import subprocess
from pathlib import Path

def verificar_python():
    """Verifica se está usando Python do ambiente virtual"""
    print("🐍 Verificando Python...")
    
    # Verifica se está em ambiente virtual
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    
    if in_venv:
        print(f"✅ Ambiente virtual ativo: {sys.prefix}")
        return True
    else:
        print("❌ Ambiente virtual não está ativo!")
        print("   Ative com: venv\\Scripts\\activate (Windows) ou source venv/bin/activate (Linux/Mac)")
        return False

def verificar_dependencias():
    """Verifica se as dependências estão instaladas"""
    print("\n📦 Verificando dependências...")
    
    dependencias = [
        'browser_use',
        'playwright', 
        'dotenv',
        'google.generativeai',
        'openai'
    ]
    
    todas_ok = True
    
    for dep in dependencias:
        try:
            __import__(dep)
            print(f"✅ {dep}")
        except ImportError:
            print(f"❌ {dep} - não instalado")
            todas_ok = False
    
    return todas_ok

def verificar_playwright():
    """Verifica se o Playwright está configurado"""
    print("\n🎭 Verificando Playwright...")
    
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            # Verifica se o Chromium está instalado
            try:
                browser = p.chromium.launch(headless=True)
                browser.close()
                print("✅ Playwright Chromium configurado")
                return True
            except Exception as e:
                print(f"❌ Chromium não instalado: {e}")
                print("   Execute: playwright install chromium")
                return False
    except ImportError:
        print("❌ Playwright não instalado")
        return False

def verificar_apis():
    """Verifica configuração das APIs"""
    print("\n🔑 Verificando configuração das APIs...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    apis_ok = []
    
    # Verifica Gemini
    gemini_key = os.getenv('GEMINI_API_KEY')
    if gemini_key and gemini_key != 'your_gemini_api_key_here':
        print("✅ Google Gemini configurado")
        apis_ok.append('gemini')
    else:
        print("❌ Google Gemini não configurado")
    
    # Verifica DeepSeek
    deepseek_key = os.getenv('DEEPSEEK_API_KEY')
    if deepseek_key and deepseek_key != 'your_deepseek_api_key_here':
        print("✅ DeepSeek configurado")
        apis_ok.append('deepseek')
    else:
        print("❌ DeepSeek não configurado")
    
    return len(apis_ok) > 0

def main():
    print("=" * 50)
    print("   TESTE DE CONFIGURAÇÃO DO AMBIENTE VIRTUAL")
    print("=" * 50)
    
    # Verificações
    python_ok = verificar_python()
    deps_ok = verificar_dependencias()
    playwright_ok = verificar_playwright()
    apis_ok = verificar_apis()
    
    print("\n" + "=" * 50)
    print("   RESUMO DOS TESTES")
    print("=" * 50)
    
    print(f"Python/Venv: {'✅' if python_ok else '❌'}")
    print(f"Dependências: {'✅' if deps_ok else '❌'}")
    print(f"Playwright: {'✅' if playwright_ok else '❌'}")
    print(f"APIs: {'✅' if apis_ok else '❌'}")
    
    if all([python_ok, deps_ok, playwright_ok, apis_ok]):
        print("\n🎉 Tudo configurado corretamente!")
        print("   Você pode executar os agentes agora.")
    else:
        print("\n⚠️  Alguns problemas encontrados.")
        print("   Consulte o README.md para instruções de configuração.")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
