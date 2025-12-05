import requests
import json

login = "contato@agenciaflip.com.br"
password = "5bbf090558f5620b"

url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"

payload = [{
    "location_code": 2076,  # Brasil
    "language_code": "pt",  # FIX: pt ao invés de pt-BR
    "keywords": ["ia para vendas", "chatbot whatsapp", "automação python"]
}]

response = requests.post(
    url,
    auth=(login, password),
    headers={"Content-Type": "application/json"},
    json=payload
)

result = response.json()

if result['tasks'][0]['status_code'] == 20000:
    print("✅ SUCESSO! Dados retornados:")
    for item in result['tasks'][0]['result']:
        print(f"\nKeyword: {item['keyword']}")
        print(f"  Volume: {item.get('search_volume', 0):,}/mês")
        print(f"  CPC: R$ {item.get('cpc', 0):.2f}")
        print(f"  Competition: {item.get('competition', 0):.2f}")
else:
    print(f"❌ Erro: {result['tasks'][0]['status_message']}")
    print(json.dumps(result, indent=2, ensure_ascii=False))
