# Script para iniciar o bot Telegram localmente 24/7
# Execute este script no PowerShell para iniciar o bot

Write-Host "🤖 Iniciando Bot de Carreira Telegram 24/7..." -ForegroundColor Green

# Configurar variáveis de ambiente
$env:TELEGRAM_BOT_TOKEN="7696538175:AAE-5hquTYBzos0ab8gfJxjpon4NXrXHaIw"
$env:TELEGRAM_CHAT_ID="5881090650"

Write-Host "✅ Variáveis de ambiente configuradas" -ForegroundColor Green
Write-Host "🔧 Iniciando agente Telegram..." -ForegroundColor Yellow

# Iniciar o bot em segundo plano
Start-Job -ScriptBlock {
    $env:TELEGRAM_BOT_TOKEN="7696538175:AAE-5hquTYBzos0ab8gfJxjpon4NXrXHaIw"
    $env:TELEGRAM_CHAT_ID="5881090650"
    Set-Location "c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Vagas"
    python telegram_agent.py
} -Name "TelegramBot"

Write-Host "🚀 Bot iniciado em background!" -ForegroundColor Green
Write-Host "💡 Use os comandos no Telegram:" -ForegroundColor Cyan
Write-Host "   /start - Iniciar bot" -ForegroundColor White
Write-Host "   /help - Ver comandos" -ForegroundColor White
Write-Host "   /rh - Buscar vagas" -ForegroundColor White
Write-Host "   /ciclo - Executar ciclo completo" -ForegroundColor White
Write-Host "   /status - Ver status" -ForegroundColor White
Write-Host ""
Write-Host "⚠️  Mantenha esta janela aberta para o bot continuar rodando" -ForegroundColor Yellow
Write-Host "🛑 Para parar: Get-Job | Stop-Job | Remove-Job" -ForegroundColor Red

# Manter script rodando
try {
    while ($true) {
        Start-Sleep -Seconds 60
        $job = Get-Job -Name "TelegramBot" -ErrorAction SilentlyContinue
        if (-not $job -or $job.State -eq "Failed" -or $job.State -eq "Stopped") {
            Write-Host "❌ Bot parou. Reiniciando..." -ForegroundColor Red
            Start-Job -ScriptBlock {
                $env:TELEGRAM_BOT_TOKEN="7696538175:AAE-5hquTYBzos0ab8gfJxjpon4NXrXHaIw"
                $env:TELEGRAM_CHAT_ID="5881090650"
                Set-Location "c:\Users\Carlos Costato\OneDrive - HITSS DO BRASIL SERVIÇOS TECNOLOGICOS LTDA\Documents\GitHub\Vagas"
                python telegram_agent.py
            } -Name "TelegramBot"
            Write-Host "✅ Bot reiniciado!" -ForegroundColor Green
        }
    }
} catch {
    Write-Host "🛂 Encerrando script..." -ForegroundColor Yellow
    Get-Job | Stop-Job | Remove-Job
}
