#!/usr/bin/env python3
"""
Script de Pesquisa de Keywords para Blog IA & Automação
Usa DataForSEO API (Brazil pt-BR)
Custo: ~$0.0008 por keyword (R$ 0.004)
"""

import requests
import json
import os
from datetime import datetime
from pytrends.request import TrendReq
import time

class KeywordResearcherBrazil:
    """
    Pesquisador de keywords profissional para Brasil (pt-BR)
    Usa DataForSEO API + Google Trends (grátis)
    """

    def __init__(self, dataforseo_login, dataforseo_password):
        self.login = dataforseo_login
        self.password = dataforseo_password
        self.base_url = "https://api.dataforseo.com/v3"

    def pesquisar_keyword_completa(self, seed_keyword, categoria):
        """
        Pesquisa COMPLETA para 1 artigo

        Retorna:
        - Volume mensal Brasil
        - CPC e Competition
        - Tendência últimos 12 meses
        - Related keywords (top 20)
        - Análise concorrentes SERP
        - Briefing pronto para escrever artigo
        """

        print(f"\n🔍 Pesquisando: {seed_keyword}")
        print(f"📂 Categoria: {categoria}")

        # 1. Dados principais (DataForSEO)
        keyword_data = self.get_keyword_data(seed_keyword)

        # 2. Keywords relacionadas (DataForSEO)
        related = self.get_related_keywords(seed_keyword)

        # 3. Tendência Google Trends (grátis)
        trend = self.get_trend_data(seed_keyword)

        # 4. Análise SERP top 3 (DataForSEO)
        serp_analysis = self.analyze_serp(seed_keyword)

        # 5. Gerar briefing completo
        briefing = self.generate_briefing(
            keyword=seed_keyword,
            data=keyword_data,
            related=related,
            trend=trend,
            serp=serp_analysis,
            categoria=categoria
        )

        return briefing

    def get_keyword_data(self, keyword):
        """
        DataForSEO: Volume + CPC + Competition (Brasil pt-BR)
        """
        url = f"{self.base_url}/keywords_data/google_ads/search_volume/live"

        payload = [{
            "location_code": 2076,  # Brasil
            "language_code": "pt",  # Português (não pt-BR)
            "keywords": [keyword]
        }]

        response = requests.post(
            url,
            auth=(self.login, self.password),
            headers={"Content-Type": "application/json"},
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            if result['tasks'][0]['status_code'] == 20000:
                data = result['tasks'][0]['result'][0]

                return {
                    'keyword': keyword,
                    'volume': data.get('search_volume', 0),
                    'cpc': data.get('cpc', 0),
                    'competition': data.get('competition', 0),
                    'monthly_searches': data.get('monthly_searches', [])
                }

        print(f"⚠️ Erro ao buscar dados: {response.status_code}")
        return None

    def get_related_keywords(self, keyword, limit=20):
        """
        DataForSEO: Keywords relacionadas (sugestões do Google)
        """
        url = f"{self.base_url}/keywords_data/google_ads/keywords_for_keywords/live"

        payload = [{
            "location_code": 2076,  # Brasil
            "language_code": "pt",
            "keywords": [keyword],
            "search_partners": False,
            "sort_by": "search_volume"
        }]

        response = requests.post(
            url,
            auth=(self.login, self.password),
            headers={"Content-Type": "application/json"},
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            if result['tasks'][0]['status_code'] == 20000:
                items = result['tasks'][0]['result'][0]['items']

                # Top 20 por volume
                related = []
                for item in items[:limit]:
                    related.append({
                        'keyword': item['keyword'],
                        'volume': item.get('search_volume', 0),
                        'cpc': item.get('cpc', 0)
                    })

                return related

        return []

    def get_trend_data(self, keyword):
        """
        Google Trends (grátis): Tendência últimos 12 meses
        """
        try:
            pytrends = TrendReq(hl='pt-BR', tz=360)
            pytrends.build_payload([keyword], timeframe='today 12-m', geo='BR')

            interest = pytrends.interest_over_time()

            if len(interest) > 0 and keyword in interest.columns:
                # Calcular crescimento (%)
                primeiro_mes = interest[keyword].iloc[0]
                ultimo_mes = interest[keyword].iloc[-1]

                if primeiro_mes > 0:
                    crescimento = ((ultimo_mes - primeiro_mes) / primeiro_mes) * 100
                    return round(crescimento, 1)

            return 0
        except Exception as e:
            print(f"⚠️ Erro Google Trends: {e}")
            return 0

    def analyze_serp(self, keyword):
        """
        DataForSEO: Análise SERP (top 3 resultados)
        """
        url = f"{self.base_url}/serp/google/organic/live/advanced"

        payload = [{
            "location_code": 2076,  # Brasil
            "language_code": "pt",
            "keyword": keyword,
            "depth": 10  # Top 10 resultados
        }]

        response = requests.post(
            url,
            auth=(self.login, self.password),
            headers={"Content-Type": "application/json"},
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            if result['tasks'][0]['status_code'] == 20000:
                items = result['tasks'][0]['result'][0]['items']

                # Analisar top 3
                analysis = {
                    'top_urls': [],
                    'avg_title_length': 0,
                    'has_featured_snippet': False
                }

                title_lengths = []

                for i, item in enumerate(items[:3]):
                    if item['type'] == 'organic':
                        analysis['top_urls'].append({
                            'position': i + 1,
                            'url': item.get('url', ''),
                            'title': item.get('title', ''),
                            'domain': item.get('domain', '')
                        })
                        title_lengths.append(len(item.get('title', '')))

                    # Verificar featured snippet
                    if item['type'] == 'featured_snippet':
                        analysis['has_featured_snippet'] = True

                if title_lengths:
                    analysis['avg_title_length'] = int(sum(title_lengths) / len(title_lengths))

                return analysis

        return {'top_urls': [], 'avg_title_length': 60, 'has_featured_snippet': False}

    def generate_briefing(self, keyword, data, related, trend, serp, categoria):
        """
        Gera briefing markdown completo para criar artigo
        """

        # Determinar valor comercial
        valor_comercial = "BAIXO"
        if data and data['cpc']:
            if data['cpc'] > 3:
                valor_comercial = "MUITO ALTO"
            elif data['cpc'] > 1.5:
                valor_comercial = "ALTO"
            elif data['cpc'] > 0.5:
                valor_comercial = "MÉDIO"

        # Determinar dificuldade
        dificuldade = "MÉDIA"
        if data and data['competition']:
            if data['competition'] > 0.7:
                dificuldade = "ALTA"
            elif data['competition'] < 0.3:
                dificuldade = "BAIXA"

        # Preparar keywords relacionadas
        related_md = ""
        if related:
            for i, kw in enumerate(related[:10], 1):
                related_md += f"{i}. **{kw['keyword']}** ({kw['volume']:,}/mês, CPC: R$ {kw['cpc']:.2f})\n"

        # Preparar análise SERP
        serp_md = ""
        if serp['top_urls']:
            for url_data in serp['top_urls']:
                serp_md += f"{url_data['position']}. {url_data['domain']} - \"{url_data['title']}\"\n"

        # Gerar briefing
        briefing = f"""# BRIEFING ARTIGO - {categoria}

**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}

---

## 🎯 KEYWORD PRINCIPAL

**"{keyword}"**

---

## 📊 DADOS BRASIL (pt-BR)

| Métrica | Valor | Análise |
|---------|-------|---------|
| **Volume mensal** | {data['volume']:,} buscas/mês | {'ALTO' if data['volume'] > 1000 else 'MÉDIO' if data['volume'] > 300 else 'BAIXO'} |
| **CPC (Google Ads)** | R$ {data['cpc']:.2f} | {valor_comercial} |
| **Competition** | {data['competition']:.2f} | {dificuldade} |
| **Tendência (12m)** | {trend:+.1f}% | {'🔥 CRESCENDO' if trend > 10 else '📈 ESTÁVEL' if trend > -10 else '📉 CAINDO'} |

---

## 💰 VALOR COMERCIAL

**{valor_comercial}**

{'✅ **Keyword QUENTE!** CPC alto indica alto valor comercial. Foque em conversão.' if data['cpc'] > 2 else '⚠️ Keyword informacional. Foque em autoridade e links internos.' if data['cpc'] < 0.5 else '✅ Bom equilíbrio entre volume e valor comercial.'}

---

## 🔑 KEYWORDS SECUNDÁRIAS (LSI - Top 10)

{related_md}

**Estratégia:** Incluir 3-5 dessas keywords naturalmente no artigo (H2, H3, corpo).

---

## 🔍 ANÁLISE SERP (Top 3 Concorrentes)

{serp_md}

**Tamanho médio título:** {serp['avg_title_length']} caracteres
**Featured snippet presente:** {'✅ SIM - Otimizar resposta 40-60 palavras!' if serp['has_featured_snippet'] else '❌ NÃO - Oportunidade de conquistar!'}

---

## ✍️ ESTRUTURA RECOMENDADA

### H1 (Título):
{self._generate_title(keyword, serp['avg_title_length'])}

### H2 (Featured Snippet - 40-60 palavras):
**{keyword}?**

[Resposta direta em lista numerada ou parágrafo conciso]

### H2 (Estrutura do artigo):
1. Por que [tema] é importante em 2025
2. {related[0]['keyword'] if related else 'Principais ferramentas'}
3. Tutorial passo a passo
4. Casos reais (genéricos, sem nomes)
5. Quanto custa (análise financeira)
6. Erros comuns e como evitar

---

## 📝 ESPECIFICAÇÕES

- **Palavra count:** 2.000-2.500 palavras
- **Tom:** Profissional mas acessível
- **Incluir:** Código Python/JavaScript (quando aplicável)
- **Cases:** 2-3 exemplos genéricos com ROI
- **CTA:** Agência Café Online (sutil, no final)

---

## 🎨 META TAGS

**Title (50-60 chars):**
{keyword.title()}: Guia Completo 2025

**Description (150-160 chars):**
Aprenda {keyword} com tutorial passo a passo, código funcional e casos reais (ROI 200%+). Implementação em 3-5 horas.

---

## 🚀 PRÓXIMO PASSO

Criar artigo completo seguindo esta estrutura. Focar em:
- ✅ Resposta featured snippet (topo)
- ✅ Profundidade (cobrir 100% do tópico)
- ✅ Cases reais genéricos
- ✅ Código funcional
- ✅ ROI e custos transparentes

---

**Custo pesquisa:** ~$0.008 (R$ 0.04)
**ROI esperado (12 meses):** {int(data['volume'] * 0.02 * 2000):,} - {int(data['volume'] * 0.05 * 5000):,} reais
"""

        return briefing

    def _generate_title(self, keyword, avg_length):
        """Gera título otimizado baseado na concorrência"""

        base = keyword.title()

        # Se concorrentes usam títulos longos, fazer mais curto
        if avg_length > 60:
            return f"{base}: Guia Completo 2025"
        else:
            return f"Como {base}: Tutorial Passo a Passo com Código Python"


# === SCRIPT PRINCIPAL ===

def processar_lista_topicos(topicos, output_dir="briefings"):
    """
    Processa lista de tópicos e gera briefings

    Args:
        topicos: Lista de dicts com 'seed' e 'categoria'
        output_dir: Diretório para salvar briefings
    """

    # Credenciais DataForSEO (ler de .env.dataforseo)
    from pathlib import Path
    env_file = Path(__file__).parent.parent / '.env.dataforseo'

    login = None
    password = None

    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if line.startswith('DATAFORSEO_LOGIN='):
                    login = line.split('=')[1].strip()
                elif line.startswith('DATAFORSEO_PASSWORD='):
                    password = line.split('=')[1].strip()

    if not login or not password:
        # Tentar variáveis de ambiente
        login = os.getenv("DATAFORSEO_LOGIN")
        password = os.getenv("DATAFORSEO_PASSWORD")

    if not login or not password:
        print("❌ ERRO: Configure credenciais DataForSEO")
        print("\nCrie arquivo .env.dataforseo com:")
        print("DATAFORSEO_LOGIN=seu_email")
        print("DATAFORSEO_PASSWORD=sua_senha")
        return

    # Criar diretório de output
    os.makedirs(output_dir, exist_ok=True)

    # Inicializar pesquisador
    researcher = KeywordResearcherBrazil(login, password)

    # Processar cada tópico
    briefings_criados = []
    custo_total = 0

    for i, topico in enumerate(topicos, 1):
        print(f"\n{'='*60}")
        print(f"📝 Artigo {i}/{len(topicos)}")

        try:
            # Pesquisar
            briefing = researcher.pesquisar_keyword_completa(
                topico['seed'],
                topico['categoria']
            )

            # Salvar briefing
            filename = f"{topico['seed'].replace(' ', '_')}.md"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(briefing)

            briefings_criados.append(filepath)
            custo_total += 0.008  # ~$0.008 por keyword

            print(f"✅ Briefing salvo: {filepath}")

            # Rate limit (respeitar API)
            if i < len(topicos):
                print("⏳ Aguardando 2s...")
                time.sleep(2)

        except Exception as e:
            print(f"❌ Erro: {e}")
            continue

    # Resumo final
    print(f"\n{'='*60}")
    print(f"🎉 CONCLUÍDO!")
    print(f"✅ {len(briefings_criados)} briefings criados")
    print(f"💰 Custo total: ${custo_total:.2f} (R$ {custo_total * 5:.2f})")
    print(f"📂 Salvos em: {output_dir}/")
    print(f"{'='*60}\n")

    return briefings_criados


if __name__ == "__main__":
    # Lista de 50 tópicos (exemplo - personalize depois)
    topicos_exemplo = [
        # IA para Vendas (10)
        {"seed": "ia para vendas whatsapp", "categoria": "Vendas"},
        {"seed": "chatbot vendas ia", "categoria": "Vendas"},
        {"seed": "automação vendas ia", "categoria": "Vendas"},
        {"seed": "gpt-4 vendas b2b", "categoria": "Vendas"},
        {"seed": "ia prospecção vendas", "categoria": "Vendas"},
        {"seed": "chatbot qualificação leads", "categoria": "Vendas"},
        {"seed": "ia para cold email", "categoria": "Vendas"},
        {"seed": "automação follow up vendas", "categoria": "Vendas"},
        {"seed": "ia para crm vendas", "categoria": "Vendas"},
        {"seed": "chatgpt vendas b2c", "categoria": "Vendas"},

        # IA para Marketing (10)
        {"seed": "ia para marketing digital", "categoria": "Marketing"},
        {"seed": "chatgpt marketing conteudo", "categoria": "Marketing"},
        {"seed": "ia para criar anuncios", "categoria": "Marketing"},
        {"seed": "automação marketing ia", "categoria": "Marketing"},
        {"seed": "ferramentas ia marketing", "categoria": "Marketing"},
        {"seed": "ia para email marketing", "categoria": "Marketing"},
        {"seed": "chatbot marketing whatsapp", "categoria": "Marketing"},
        {"seed": "ia para seo", "categoria": "Marketing"},
        {"seed": "gpt-4 copywriting", "categoria": "Marketing"},
        {"seed": "ia para redes sociais", "categoria": "Marketing"},

        # Automação (10)
        {"seed": "automação whatsapp python", "categoria": "Automação"},
        {"seed": "evolution api tutorial", "categoria": "Automação"},
        {"seed": "n8n tutorial português", "categoria": "Automação"},
        {"seed": "zapier vs n8n", "categoria": "Automação"},
        {"seed": "automação atendimento ia", "categoria": "Automação"},
        {"seed": "webhook whatsapp python", "categoria": "Automação"},
        {"seed": "integração openai whatsapp", "categoria": "Automação"},
        {"seed": "chatbot python flask", "categoria": "Automação"},
        {"seed": "automação agenda google", "categoria": "Automação"},
        {"seed": "make vs zapier", "categoria": "Automação"},
    ]

    # Processar primeiros 10 (teste)
    print("🚀 Iniciando pesquisa de keywords...\n")
    briefings = processar_lista_topicos(topicos_exemplo[:3])  # Testar com 3 primeiro

    print(f"\n📚 Próximo passo:")
    print(f"1. Revisar briefings em: briefings/")
    print(f"2. Escolher melhor keyword (volume + valor comercial)")
    print(f"3. Criar artigo seguindo briefing")
