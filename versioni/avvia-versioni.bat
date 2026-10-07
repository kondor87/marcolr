@echo off
rem Avvia il sito attuale e le tre versioni grafiche, poi le apre nel browser.
rem Tutte usano gli stessi contenuti (cartella content). -D mostra anche le bozze.
rem Chiudi le finestre nere per fermarle.
start "Sito attuale" /D "%~dp0.." hugo server -D --port 8811 --bind 127.0.0.1
start "V2 Peperino" /D "%~dp0v2-targa" hugo server -D --port 8812 --bind 127.0.0.1
start "V3 Programma" /D "%~dp0v3-programma" hugo server -D --port 8813 --bind 127.0.0.1
start "V4 Cartiglio" /D "%~dp0v4-cartiglio" hugo server -D --port 8814 --bind 127.0.0.1
timeout /t 5 /nobreak >nul
start "" http://localhost:8811/
start "" http://localhost:8812/
start "" http://localhost:8813/
start "" http://localhost:8814/
