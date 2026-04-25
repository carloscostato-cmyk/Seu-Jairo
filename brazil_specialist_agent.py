"""
Brazil Specialist Agent - Agente Especialista em Mercado Brasileiro
Foca em vagas do mercado brasileiro e fontes locais
"""

import re
from typing import Dict, List, Tuple
from urllib.parse import urlparse

class BrazilSpecialistAgent:
    """
    Agente especialista que prioriza vagas do mercado brasileiro
    e valida fontes locais
    """
    
    def __init__(self):
        # Fontes brasileiras prioritárias
        self.brazilian_sources = {
            "gupy": 25,      # Prioridade máxima
            "catho": 25,     # Prioridade máxima  
            "indeed": 20,    # Alta prioridade
            "brasiltech": 20, # Alta prioridade
            "linkedin": 15,  # Média prioridade (muita vaga internacional)
            "arbeitnow": 5,  # Baixa prioridade (alemã)
            "remotive": 5,   # Baixa prioridade (internacional)
            "freelance": 3,  # Muito baixa prioridade
        }
        
        # Indicadores de mercado brasileiro
        self.brazilian_indicators = [
            "brasil", "brazil", "são paulo", "sao paulo", "rio de janeiro",
            "belo horizonte", "curitiba", "porto alegre", "recife", "fortaleza",
            "campinas", "brasília", "brasilia", "salvador", "manaus",
            "rj", "sp", "mg", "pr", "rs", "pe", "ce", "df", "ba", "am",
            "home office", "remoto brasil", "remote brazil", "trabalho remoto",
            "clt", "pj", "mei", "estágio", "trainee", "júnior", "pleno",
            "sênior", "senior", "especialista", "coordenador", "gerente",
            "r$", "reais", "salário", "benefícios", "vr", "va", "auxílio"
        ]
        
        # Empresas brasileiras conhecidas
        self.brazilian_companies = [
            "magazine luiza", "magalu", "americanas", "via", "lojas americanas",
            "carrefour", "pão de açúcar", "grupo pão de açúcar", "assai",
            "itau", "itaú", "bradesco", "santander", "banco do brasil", "caixa",
            "petrobras", "vale", "embraer", "eletrobras", "copel", "cemig",
            "vivo", "claro", "tim", "oi", "algar", "telefonica brasil",
            "google brasil", "microsoft brasil", "ibm brasil", "oracle brasil",
            "totvs", "linx", "neurotech", "ci&t", "locaweb", "hostnet",
            "stone", "pagseguro", "mercadopago", "nucont", "gerencianet",
            "nubank", "inter", "c6 bank", "original", "neon", "banco pan"
        ]
        
        # Domínios brasileiros
        self.brazilian_domains = [
            ".com.br", ".br", ".gov.br", ".mil.br", ".org.br", ".net.br"
        ]
        
        # Termos de busca em português para fontes brasileiras
        self.portuguese_search_terms = {
            "gupy": [
                "gerente de projetos", "gerente de ti", "coordenador de ti",
                "gerente de tecnologia", "head de tecnologia", "tech lead",
                "arquiteto de software", "engenheiro de software sênior",
                "cybersecurity", "segurança da informação", "analista de segurança"
            ],
            "catho": [
                "gerente-de-projetos", "gerente-de-ti", "coordenador-ti",
                "gerente-tecnologia", "head-tecnologia", "tech-lead",
                "arquiteto-software", "engenheiro-software-senior",
                "cybersecurity", "seguranca-informacao", "analista-seguranca"
            ],
            "indeed": [
                "gerente+de+projetos", "gerente+de+ti", "coordenador+ti",
                "cybersecurity+manager", "seguranca+da+informacao",
                "tech+lead+brasil", "arquiteto+de+software+brasil"
            ]
        }
    
    def is_brazilian_company(self, company: str, url: str = "") -> bool:
        """
        Verifica se a empresa é brasileira
        """
        company_lower = company.lower()
        
        # Verificar na lista de empresas brasileiras
        for brazilian_company in self.brazilian_companies:
            if brazilian_company in company_lower:
                return True
        
        # Verificar domínio brasileiro
        if url:
            domain = urlparse(url).netloc.lower()
            for brazilian_domain in self.brazilian_domains:
                if brazilian_domain in domain:
                    return True
        
        return False
    
    def calculate_brazil_score(self, title: str, description: str, company: str, url: str, source: str) -> int:
        """
        Calcula score de prioridade para mercado brasileiro
        """
        score = 0
        text = f"{title} {description} {company}".lower()
        
        # Bônus para fonte brasileira
        source_lower = source.lower()
        for src, bonus in self.brazilian_sources.items():
            if src in source_lower:
                score += bonus
                break
        
        # Bônus para indicadores brasileiros
        brazilian_count = sum(1 for indicator in self.brazilian_indicators if indicator in text)
        score += min(brazilian_count * 3, 30)  # Até +30 pontos
        
        # Bônus para empresa brasileira
        if self.is_brazilian_company(company, url):
            score += 20
        
        # Bônus para termos específicos do mercado brasileiro
        brazilian_terms = ["clt", "pj", "r$", "reais", "vr", "va", "home office brasil"]
        term_count = sum(1 for term in brazilian_terms if term in text)
        score += min(term_count * 5, 25)  # Até +25 pontos
        
        # Penalidade para indicadores estrangeiros fortes
        foreign_indicators = ["united states", "europe", "uk", "canada", "australia"]
        foreign_count = sum(1 for indicator in foreign_indicators if indicator in text)
        score -= min(foreign_count * 10, 20)  # Até -20 pontos
        
        # Penalidade para salário em dólar sem menção de Brasil
        if "$" in text and "brasil" not in text and "brazil" not in text:
            score -= 15
        
        return max(-20, min(100, score))
    
    def get_source_priority(self, source: str) -> int:
        """
        Retorna prioridade da fonte
        """
        source_lower = source.lower()
        for src, priority in self.brazilian_sources.items():
            if src in source_lower:
                return priority
        return 5  # Prioridade padrão baixa
    
    def get_search_terms_for_source(self, source: str) -> List[str]:
        """
        Retorna termos de busca em português para a fonte
        """
        source_lower = source.lower()
        return self.portuguese_search_terms.get(source_lower, [])
    
    def should_prioritize_job(self, title: str, description: str, company: str, url: str, source: str) -> bool:
        """
        Determina se a vaga deve ser priorizada (mercado brasileiro)
        """
        score = self.calculate_brazil_score(title, description, company, url, source)
        return score >= 40  # Threshold para priorização
    
    def get_market_classification(self, title: str, description: str, company: str, url: str, source: str) -> str:
        """
        Classifica o foco de mercado da vaga
        """
        score = self.calculate_brazil_score(title, description, company, url, source)
        
        if score >= 70:
            return "🇧🇷 Mercado Brasileiro Prioritário"
        elif score >= 50:
            return "🇧🇷 Mercado Brasileiro Forte"
        elif score >= 30:
            return "🌐 Misto (Brasil favorecido)"
        elif score >= 10:
            return "🌐 Misto (Internacional)"
        else:
            return "🌐 Mercado Internacional"
    
    def optimize_search_for_brazil(self, source: str) -> List[str]:
        """
        Otimiza termos de busca para mercado brasileiro
        """
        base_terms = self.get_search_terms_for_source(source)
        
        # Adicionar termos específicos do Brasil se não houver
        if not base_terms:
            base_terms = [
                "gerente de projetos brasil", "gerente de ti brasil",
                "cybersecurity brasil", "tech lead brasil",
                "arquiteto de software brasil", "head de tecnologia brasil"
            ]
        
        return base_terms
