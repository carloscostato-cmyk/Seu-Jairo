"""
Language Specialist Agent - Agente Especialista em Idioma
Prioriza vagas em português e gerencia scoring de idioma
"""

import re
from typing import Dict, List, Tuple

class LanguageSpecialistAgent:
    """
    Agente especialista que analisa e prioriza vagas em português
    """
    
    def __init__(self):
        # Indicadores fortes de português
        self.portuguese_keywords = [
            "vaga", "vagas", "emprego", "empregos", "oportunidade", "oportunidades",
            "contratação", "contratações", "seleção", "recrutamento", "candidato",
            "candidatos", "curriculum", "currículo", "entrevista", "salário", "benefícios",
            "pj", "clt", "home office", "home-office", "remoto", "presencial", "híbrido",
            "são paulo", "rio de janeiro", "brasil", "brasileiro", "brasileira",
            "gerente de projetos", "gerente de ti", "analista", "coordenador",
            "desenvolvedor", "engenheiro", "arquiteto", "consultor"
        ]
        
        # Indicadores de inglês (para penalização)
        self.english_indicators = [
            "we are looking for", "we are seeking", "requirements", "qualifications",
            "responsibilities", "skills", "experience", "education", "benefits",
            "salary", "full-time", "part-time", "remote", "hybrid", "on-site",
            "bachelor's degree", "master's degree", "phd", "university",
            "company", "team", "position", "role", "job", "career", "opportunity"
        ]
        
        # Padrões de português
        self.portuguese_patterns = [
            r'\b(é|são|tem|têm|para|com|sem|não|sim|mas|por|que|onde|quando|como)\b',
            r'\b(gestão|desenvolvimento|implementação|coordenação|análise|planejamento)\b',
            r'\[.*\]\s*\(',  # Padrão brasileiro: [São Paulo] (SP)
            r'R\$\s*\d+',   # Salário em reais
            r'\d+\s*anos',   # "X anos" de experiência
        ]
        
        # Padrões de inglês
        self.english_patterns = [
            r'\b(is|are|has|have|for|with|without|not|yes|but|by|why|where|when|how)\b',
            r'\b(management|development|implementation|coordination|analysis|planning)\b',
            r'\$[\d,]+',     # Salário em dólar
            r'\d+\s+years?',  # "X years" de experiência
        ]
    
    def detect_language_ratio(self, text: str) -> Tuple[float, float]:
        """
        Detecta a proporção de português vs inglês no texto
        Retorna: (portuguese_ratio, english_ratio)
        """
        text_lower = text.lower()
        
        # Contar palavras em português
        portuguese_count = 0
        for keyword in self.portuguese_keywords:
            portuguese_count += len(re.findall(rf'\b{re.escape(keyword)}\b', text_lower))
        
        # Contar indicadores de inglês
        english_count = 0
        for indicator in self.english_indicators:
            english_count += len(re.findall(rf'\b{re.escape(indicator)}\b', text_lower))
        
        total_words = len(text.split())
        if total_words == 0:
            return 0.0, 0.0
        
        portuguese_ratio = portuguese_count / total_words
        english_ratio = english_count / total_words
        
        return portuguese_ratio, english_ratio
    
    def analyze_portuguese_patterns(self, text: str) -> int:
        """
        Analisa padrões específicos do português brasileiro
        Retorna score de 0 a 10
        """
        score = 0
        text_lower = text.lower()
        
        for pattern in self.portuguese_patterns:
            if re.search(pattern, text_lower):
                score += 2
        
        return min(score, 10)
    
    def analyze_english_patterns(self, text: str) -> int:
        """
        Analisa padrões específicos do inglês
        Retorna score de 0 a 10
        """
        score = 0
        text_lower = text.lower()
        
        for pattern in self.english_patterns:
            if re.search(pattern, text_lower):
                score += 2
        
        return min(score, 10)
    
    def calculate_language_score(self, title: str, description: str) -> int:
        """
        Calcula score de idioma para a vaga
        - Positivo para português
        - Negativo para inglês predominante
        """
        full_text = f"{title} {description}"
        
        # Detectar proporções
        pt_ratio, en_ratio = self.detect_language_ratio(full_text)
        
        # Analisar padrões
        pt_pattern_score = self.analyze_portuguese_patterns(full_text)
        en_pattern_score = self.analyze_english_patterns(full_text)
        
        # Calcular score final
        score = 0
        
        # Bônus para português
        if pt_ratio > 0.1:  # Pelo menos 10% de palavras em português
            score += int(pt_ratio * 30)  # Até +30 pontos
        
        score += pt_pattern_score * 2  # Até +20 pontos
        
        # Penalidade para inglês predominante
        if en_ratio > 0.3:  # Mais de 30% em inglês
            score -= int(en_ratio * 20)  # Até -20 pontos
        
        score -= en_pattern_score  # Até -10 pontos
        
        # Bônus especial para vagas claramente em português
        if pt_ratio > 0.5 and en_ratio < 0.1:
            score += 15  # Bônus significativo
        
        # Penalidade severa para vagas 100% em inglês
        if en_ratio > 0.7 and pt_ratio < 0.05:
            score -= 25  # Penalidade severa
        
        return max(-30, min(30, score))  # Limitar entre -30 e +30
    
    def get_language_classification(self, title: str, description: str) -> str:
        """
        Classifica o idioma predominante da vaga
        """
        score = self.calculate_language_score(title, description)
        
        if score >= 15:
            return "🇧🇷 Português Prioritário"
        elif score >= 5:
            return "🇧🇷/🇺🇸 Misto (Português favorecido)"
        elif score >= -5:
            return "🇺🇸/🇧🇷 Misto (Inglês predominante)"
        else:
            return "🇺🇸 Inglês Predominante"
    
    def should_prioritize_job(self, title: str, description: str) -> bool:
        """
        Determina se a vaga deve ser priorizada (português)
        """
        classification = self.get_language_classification(title, description)
        return "Português" in classification
