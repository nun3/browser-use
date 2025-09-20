@echo off
echo ========================================
echo    Configuracao do Ambiente Virtual
echo ========================================
echo.

REM Verifica se Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo Instale o Python 3.8+ em: https://python.org
    pause
    exit /b 1
)

echo Python encontrado!
python --version

echo.
echo Criando ambiente virtual...
python -m venv venv

if errorlevel 1 (
    echo ERRO: Falha ao criar ambiente virtual
    pause
    exit /b 1
)

echo.
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo.
echo Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Instalando navegadores do Playwright...
playwright install chromium

echo.
echo ========================================
echo    Configuracao Concluida!
echo ========================================
echo.
echo Para ativar o ambiente virtual:
echo   venv\Scripts\activate.bat
echo.
echo Para desativar:
echo   deactivate
echo.
pause
