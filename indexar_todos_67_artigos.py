#!/usr/bin/env python3
"""
Indexa TODOS os 67 artigos do blog no Google via Indexing API.
"""
import json
import time
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Credentials
TOKEN_FILE = '/Users/felipezanonimini/Desktop/automacoes/credentials/search_console_token.json'
BASE_URL = 'https://blog.agenciacafeonline.com.br/blog/'

def gerar_urls_artigos():
    """Gera lista de URLs de todos os artigos."""
    artigos_dir = 'src/content/blog'
    urls = []

    for filename in sorted(os.listdir(artigos_dir)):
        if filename.endswith('.md'):
            slug = filename.replace('.md', '')
            url = f"{BASE_URL}{slug}/"
            urls.append(url)

    return urls

def indexar_artigos():
    """Indexa todos os artigos no Google."""
    print("\n🚀 Indexando TODOS os 67 artigos do blog...")
    print("=" * 80)

    # Gerar URLs
    urls = gerar_urls_artigos()
    print(f"\n📝 Total de artigos encontrados: {len(urls)}\n")

    # Carregar token OAuth
    with open(TOKEN_FILE, 'r') as f:
        token_data = json.load(f)

    credentials = Credentials(
        token=token_data['token'],
        refresh_token=token_data['refresh_token'],
        token_uri=token_data['token_uri'],
        client_id=token_data['client_id'],
        client_secret=token_data['client_secret'],
        scopes=token_data['scopes']
    )

    service = build('indexing', 'v3', credentials=credentials)

    sucesso = 0
    erros = 0

    for i, url in enumerate(urls, 1):
        try:
            body = {
                "url": url,
                "type": "URL_UPDATED"
            }

            response = service.urlNotifications().publish(body=body).execute()

            # Extrair slug para exibição
            slug = url.split('/blog/')[-1].rstrip('/')
            print(f"✅ {i:2d}/67 - {slug[:60]}")

            sucesso += 1

            # Rate limit: ~2 req/s (Google permite ~200/min)
            if i % 10 == 0:
                time.sleep(1)
            else:
                time.sleep(0.3)

        except Exception as e:
            slug = url.split('/blog/')[-1].rstrip('/')
            print(f"❌ {i:2d}/67 - {slug[:60]}")
            print(f"   Erro: {str(e)[:80]}")
            erros += 1

    # Resumo final
    print("\n" + "=" * 80)
    print(f"\n📊 RESULTADO:")
    print(f"  ✅ Sucesso: {sucesso}/{len(urls)} artigos")
    print(f"  ❌ Erros: {erros}/{len(urls)} artigos")

    if sucesso > 0:
        print(f"\n🎉 {sucesso} artigos submetidos ao Google Indexing API!")
        print("⏱️  Indexação acontece em 24-48h (geralmente mais rápido)")
        print("📊  Acompanhe em: https://search.google.com/search-console")

    print()

if __name__ == '__main__':
    indexar_artigos()
