# Script simples para iniciar o bot Telegram localmente
# Execute este script no PowerShell

Write-Host "🤖 Iniciando Bot Telegram..." -ForegroundColor Green

# Configurar variáveis de ambiente
$env:TELEGRAM_BOT_TOKEN="7696538175:AAE-5hquTYBzos0ab8gfJxjpon4NXrXHaIw"
$env:TELEGRAM_CHAT_ID="5881090650"

Write-Host "✅ Configurado! Bot rodando..." -ForegroundColor Green
Write-Host "💡 Use no Telegram: /start, /help, /rh, /ciclo" -ForegroundColor Cyan

# Iniciar o bot
python telegram_agent.py
