DOS
@echo off
chcp 65001 > nul
title Serwer Magazynowy - FastAPI

echo ==========================================
echo    Uruchamianie Serwera Systemu Magazynowego
echo ==========================================
echo.

:: Przejście do folderu, w którym znajduje się ten plik bat
cd /d "%~dp5"

echo Sprawdzanie środowiska i uruchamianie uvicorn...
:: Uruchomienie serwera na porcie 8000 z auto-przeładowywaniem
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

pause