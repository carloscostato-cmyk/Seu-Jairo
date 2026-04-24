"""
Aplicação Flask para hospedar o bot Telegram 24/7 em serviços como Render.
Permite manter o bot ativo enquanto responde a comandos do Telegram.
"""

import os
import threading
from flask import Flask
from telegram_agent import TelegramCareerAgent

app = Flask(__name__)

# Rota principal para health check
@app.route('/')
def home():
    return "🤖 Bot de Carreira Telegram está online 24/7!"

# Rota de status para monitoramento
@app.route('/status')
def status():
    return {
        "status": "online",
        "service": "Telegram Career Bot",
        "message": "Bot respondendo comandos normalmente"
    }

def run_bot():
    """Executa o bot Telegram em segundo plano."""
    try:
        agent = TelegramCareerAgent()
        agent.run_forever()
    except Exception as e:
        print(f"Erro no bot: {e}")
        # Tentar reiniciar após 30 segundos se houver erro
        import time
        time.sleep(30)
        run_bot()

if __name__ == "__main__":
    # Inicia o bot em uma thread separada
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    print("🤖 Bot Telegram iniciado em background")
    print("🌐 Servidor web iniciado para health checks")
    
    # Inicia o servidor web (necessário para serviços como Render)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, use_reloader=False)
