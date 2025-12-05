import requests
import json
from datetime import datetime
from pytrends.request import TrendReq

login = "contato@agenciaflip.com.br"
password = "5bbf090558f5620b"

keyword = "ia para vendas whatsapp"

# 1. Volume + CPC
url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
payload = [{
    "location_code": 2076,
    "language_code": "pt",
    "keywords": [keyword]
}]

response = requests.post(url, auth=(login, password), json=payload)
data = response.json()['tasks'][0]['result'][0]

volume = data.get('search_volume', 0)
cpc = data.get('cpc', 0)
competition = data.get('competition', 0) if isinstance(data.get('competition'), (int, float)) else 0.5

# 2. Google Trends
pytrends = TrendReq(hl='pt-BR', tz=360)
pytrends.build_payload([keyword], timeframe='today 12-m', geo='BR')
interest = pytrends.interest_over_time()

if len(interest) > 0 and keyword in interest.columns:
    primeiro = interest[keyword].iloc[0]
    ultimo = interest[keyword].iloc[-1]
    crescimento = ((ultimo - primeiro) / primeiro * 100) if primeiro > 0 else 0
else:
    crescimento = 0

# Gerar briefing
briefing = f"""# BRIEFING - ia para vendas whatsapp

## DADOS BRASIL

- **Volume:** {volume:,}/mês
- **CPC:** R$ {cpc:.2f}
- **Competition:** {competition:.2f}
- **Tendência:** {crescimento:+.1f}%

## ANÁLISE

Valor comercial: {"ALTO" if cpc > 2 else "MÉDIO"}
Dificuldade: {"ALTA" if competition > 0.7 else "MÉDIA" if competition > 0.3 else "BAIXA"}

## ESTRUTURA ARTIGO

H1: Como Usar IA para Vendas no WhatsApp: Guia Completo 2025

H2: O que é IA para vendas no WhatsApp? (40-60 palavras)

H2: Por que usar IA em vendas WhatsApp

H2: 5 ferramentas de IA para vendas

H2: Tutorial passo a passo (código Python)

H2: 3 casos reais (ROI 200%+)

H2: Custos e ROI

---

**Custo pesquisa:** $0.0008
**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}
"""

print(briefing)

# Salvar
with open("briefings/ia_para_vendas_whatsapp.md", "w") as f:
    f.write(briefing)

print("\n✅ Briefing salvo em: briefings/ia_para_vendas_whatsapp.md")
