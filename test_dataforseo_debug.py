import requests
import json

login = "contato@agenciaflip.com.br"
password = "5bbf090558f5620b"

url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"

payload = [{
    "location_code": 2076,  # Brasil
    "language_code": "pt-BR",
    "keywords": ["ia para vendas"]
}]

response = requests.post(
    url,
    auth=(login, password),
    headers={"Content-Type": "application/json"},
    json=payload
)

print(f"Status: {response.status_code}")
print(f"\nResposta completa:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
