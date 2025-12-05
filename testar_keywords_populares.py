import requests

login = "contato@agenciaflip.com.br"
password = "5bbf090558f5620b"

keywords_testar = [
    "chatbot whatsapp",
    "ia para vendas",
    "automação whatsapp",
    "chatgpt para marketing",
    "inteligência artificial vendas",
    "como criar chatbot",
    "whatsapp business automação"
]

url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
payload = [{
    "location_code": 2076,
    "language_code": "pt",
    "keywords": keywords_testar
}]

response = requests.post(url, auth=(login, password), json=payload)
results = response.json()['tasks'][0]['result']

print("🔍 KEYWORDS POPULARES (Brasil):\n")
print(f"{'Keyword':<40} {'Volume':<12} {'CPC':<10} {'Competition'}")
print("-" * 80)

# Ordenar por volume
sorted_results = sorted(results, key=lambda x: x.get('search_volume', 0), reverse=True)

for item in sorted_results:
    kw = item['keyword']
    vol = item.get('search_volume', 0)
    cpc = item.get('cpc', 0)
    comp = item.get('competition', 'N/A')
    
    print(f"{kw:<40} {vol:>10,}/mês  R$ {cpc:>6.2f}  {comp}")

print("\n✅ Use as keywords com VOLUME > 500 e CPC > 1.50")
