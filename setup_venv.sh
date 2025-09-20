#!/bin/bash

echo "========================================"
echo "   Configuração do Ambiente Virtual"
echo "========================================"
echo

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python3 não encontrado!"
    echo "Instale o Python 3.8+ em: https://python.org"
    exit 1
fi

echo "Python encontrado!"
python3 --version

echo
echo "Criando ambiente virtual..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao criar ambiente virtual"
    exit 1
fi

echo
echo "Ativando ambiente virtual..."
source venv/bin/activate

echo
echo "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo
echo "Instalando navegadores do Playwright..."
playwright install chromium

echo
echo "========================================"
echo "   Configuração Concluída!"
echo "========================================"
echo
echo "Para ativar o ambiente virtual:"
echo "  source venv/bin/activate"
echo
echo "Para desativar:"
echo "  deactivate"
echo
