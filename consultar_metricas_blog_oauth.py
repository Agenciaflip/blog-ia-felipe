#!/usr/bin/env python3
"""
Consulta métricas de tráfego do blog no Google Search Console.
"""
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Credentials OAuth
TOKEN_FILE = '/Users/felipezanonimini/Desktop/automacoes/credentials/search_console_token.json'
SITE_URL = 'sc-domain:agenciacafeonline.com.br'

def consultar_metricas():
    """Consulta métricas dos últimos 7 dias."""
    print("\n📊 Consultando métricas Google Search Console...")
    print(f"Property: {SITE_URL}\n")

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

    service = build('searchconsole', 'v1', credentials=credentials)

    # Período: últimos 7 dias
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)

    # Query para métricas gerais
    request = {
        'startDate': str(start_date),
        'endDate': str(end_date),
        'dimensions': ['page'],
        'rowLimit': 25
    }

    try:
        response = service.searchanalytics().query(
            siteUrl=SITE_URL, body=request
        ).execute()

        if 'rows' not in response:
            print("⚠️ Sem dados de tráfego nos últimos 7 dias\n")
            print("Possíveis motivos:")
            print("  • Blog muito novo (precisa 2-4 semanas para aparecer)")
            print("  • Artigos ainda não indexados pelo Google")
            print("  • Nenhum clique/impressão neste período")
            return

        # Calcular totais
        total_clicks = sum(row.get('clicks', 0) for row in response['rows'])
        total_impressions = sum(row.get('impressions', 0) for row in response['rows'])

        print(f"📅 Período: {start_date} até {end_date} (últimos 7 dias)\n")
        print(f"🎯 TOTAIS:")
        print(f"  • Cliques: {total_clicks}")
        print(f"  • Impressões: {total_impressions}")

        if total_impressions > 0:
            ctr = (total_clicks / total_impressions) * 100
            print(f"  • CTR: {ctr:.2f}%")

        print(f"\n📄 Top páginas com tráfego:")
        print("-" * 90)

        for i, row in enumerate(response['rows'][:15], 1):
            url = row['keys'][0]
            clicks = row.get('clicks', 0)
            impressions = row.get('impressions', 0)
            ctr = row.get('ctr', 0) * 100
            position = row.get('position', 0)

            # Extrair slug do artigo
            if '/blog/' in url:
                slug = url.split('/blog/')[-1].rstrip('/')
            else:
                slug = 'home' if url.endswith('.com.br/') else url.split('/')[-1]

            print(f"{i:2d}. {slug[:65]:<65}")
            print(f"    Cliques: {clicks:3d} | Impressões: {impressions:4d} | CTR: {ctr:5.1f}% | Pos: {position:4.1f}")
            print()

    except Exception as e:
        print(f"❌ Erro ao consultar: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    consultar_metricas()
