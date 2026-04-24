# 🚀 Guia Definitivo: Seu Bot no Telegram 24/7 (De Graça!)

Bem-vindo(a) ao seu guia passo a passo! Aqui você vai aprender a colocar o seu **Agente de Carreira do Telegram** rodando na nuvem, de graça, para você poder mandar os comandos `/start`, `/rh` ou qualquer outro a hora que quiser, sem precisar deixar o seu computador ligado.

Nós vamos usar duas ferramentas gratuitas e muito fáceis para iniciantes:
1. **Render** (Onde o seu código vai morar)
2. **UptimeRobot** (O "despertador" que vai impedir o Render de dormir)

---

## 🛠️ Passo 0: O Truque do "Servidor Web"
Como o **Render** gratuito exige que a nossa aplicação seja um "Site" (Web Service) para nos dar a hospedagem grátis, nós precisamos adicionar um pequeno servidor de mentirinha junto com o seu bot. 

Não se preocupe, é muito simples! **No seu projeto no GitHub**, crie um arquivo chamado `app.py` e coloque esse código dentro dele:

```python
import os
import threading
from flask import Flask
from telegram_agent import TelegramCareerAgent

app = Flask(__name__)

# Essa é a página que o Render vai acessar para saber que estamos "vivos"
@app.route('/')
def home():
    return "Bot de Carreira está rodando 24/7!"

def run_bot():
    agent = TelegramCareerAgent()
    agent.run_forever()

if __name__ == "__main__":
    # Inicia o bot em segundo plano
    threading.Thread(target=run_bot).start()
    
    # Inicia o servidor web na porta exigida pelo Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

> **IMPORTANTE:** Certifique-se de que o seu arquivo `requirements.txt` tem a biblioteca `Flask` e a `requests` escritas lá dentro.
> *Exemplo do seu `requirements.txt`:*
> ```text
> Flask==3.0.0
> requests==2.31.0
> ```

Depois de criar/atualizar esses arquivos, faça o **Commit e Push** para o seu GitHub!

---

## ☁️ Passo 1: Hospedando no Render

Agora vamos colocar seu bot na nuvem!

1. Acesse o site **[Render.com](https://render.com/)** e faça login com a sua conta do **GitHub**.
2. No painel inicial (Dashboard), clique no botão **"New +"** no canto superior direito e escolha **"Web Service"**.

![Passo 2 do Render](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Cursor_arrow.png/20px-Cursor_arrow.png) *Imagem ilustrativa: O botão fica bem destacado.*

3. Na tela seguinte, escolha **"Build and deploy from a Git repository"** e clique em *Next*.
4. Conecte o seu repositório `Vagas` que está no seu GitHub.
5. Agora, preencha as configurações do seu servidor exatamente assim:
   * **Name:** `bot-carreira-telegram` (ou o nome que quiser)
   * **Region:** Escolha `Ohio (US East)` ou qualquer uma.
   * **Branch:** `main`
   * **Runtime:** `Python 3`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `python app.py`
   * **Instance Type:** Escolha o plano **Free ($0/month)**.

### 🔑 Configurando as Senhas (Environment Variables)
Ainda na mesma página de configuração, role para baixo e clique em **"Advanced"**, depois clique em **"Add Environment Variable"**. Adicione os tokens do seu bot aqui para mantê-los seguros:

| Key | Value |
| :--- | :--- |
| `TELEGRAM_BOT_TOKEN` | *Cole aqui o token do seu BotFather* |
| `TELEGRAM_CHAT_ID` | *Cole aqui o seu ID do Telegram* |

6. Role até o fim e clique no botão **"Create Web Service"**.
7. Aguarde alguns minutos. Quando aparecer a mensagem verde `==> Your service is live 🎉`, o seu bot já estará rodando!
8. **Copie a URL do seu serviço** (Fica logo abaixo do nome, algo como `https://bot-carreira-telegram.onrender.com`). Vamos usar isso no próximo passo.

---

## ⏰ Passo 2: Mantendo o Bot Acordado 24/7 (UptimeRobot)

O plano gratuito do Render "dorme" se não receber visitas a cada 15 minutos. Vamos usar o UptimeRobot para ficar acessando o seu bot de mentirinha a cada 5 minutos!

1. Acesse **[UptimeRobot.com](https://uptimerobot.com/)** e crie uma conta gratuita.
2. No painel, clique no botão verde **"Add New Monitor"**.
3. Preencha o formulário dessa forma:
   * **Monitor Type:** `HTTP(s)`
   * **Friendly Name:** `Manter Bot Acordado`
   * **URL (or IP):** *Cole aqui aquela URL do Render que você copiou no Passo 1! (Ex: `https://bot-carreira-telegram.onrender.com`)*
   * **Monitoring Interval:** Escolha `5 minutes`.
4. Deixe o resto como está e clique no botão azul **"Create Monitor"**. (Ele vai pedir para clicar duas vezes para confirmar).

---

## 🎉 Pronto! Tudo configurado!

Agora o seu bot é verdadeiramente imortal e 100% gratuito:
1. O **Render** está rodando o seu código na nuvem.
2. O servidor do **Render** iria dormir, mas o **UptimeRobot** "cutuca" ele a cada 5 minutos.
3. O seu script `telegram_agent.py` fica rodando em segundo plano ouvindo as suas mensagens o tempo todo.

Vá até o seu aplicativo do Telegram e digite `/start` ou `/rh`. Ele vai responder na mesma hora! 🚀
