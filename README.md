# 🤖 Doutor em RH - Sistema Autônomo de Hunting & Career Management

![GitHub Actions](https://img.shields.io/badge/Automation-GitHub_Actions-blue?style=for-the-badge&logo=github-actions)
![Python](https://img.shields.io/badge/Language-Python_3.9-green?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

O **Doutor em RH** é um agente de inteligência artificial desenvolvido para automatizar a busca e a candidatura a vagas de alta senioridade no mercado de TI (IA, Cybersecurity e Transformação Digital).

## 🚀 Funcionalidades de Elite

- 🔍 **Busca Inteligente Multi-Fonte:** Varredura automática em Remotive, Arbeitnow, LinkedIn público (guest endpoint) e vagas freelance (RemoteOK).
- 🇧🇷 **Foco Brasil + Perfil:** Priorização de vagas aderentes ao perfil de Carlos (Gerência de Projetos, TI, IA, Cybersecurity e Transformação Digital), incluindo buscas em português e contexto Brasil.
- 🦾 **Auto-Apply (Back-end):** Realiza inscrições diretamente via API/ATS, ignorando a necessidade de navegação visual.
- 📲 **Notificações em Tempo Real:** Integração via Telegram Bot para alertas de novas candidaturas.
- 📅 **Relatórios Agendados:** Envio de resumos consolidados às 09:00, 13:00 e 18:00 (Brasília).
- 📊 **Dashboard Técnico com Busca:** Filtro por texto e fonte para localizar vagas rapidamente.

## 🛠️ Arquitetura Técnica

O sistema opera em uma arquitetura 100% Cloud-Native:
1. **Engine de Busca (Python):** Processamento de dados e match de currículo.
2. **Automação (GitHub Actions):** Orquestração dos ciclos de trabalho a cada 4 horas.
3. **Notificador (Telegram API):** Comunicação bidirecional com o usuário.
4. **Persistência (JSON DB):** Armazenamento seguro do histórico de candidaturas.

## ✅ Qualidade e Operação

- Skill operacional versionada em [SKILL.md](SKILL.md).
- Pipeline configurado para falhar quando a notificação no Telegram não for enviada (evita falso positivo).
- Dashboard público para validação visual final: https://carloscostato-cmyk.github.io/Vagas/

## 👤 Desenvolvedor & Beneficiário
**Carlos Costato** - Senior IT Project Manager & AI Specialist.

---
_Este projeto faz parte do ecossistema de elite para gestão de carreira e automação inteligente._
