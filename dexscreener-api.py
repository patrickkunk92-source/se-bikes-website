#!/usr/bin/env python3
"""
DexScreener API Client
Fetch real-time trading data for tokens
"""

import requests
import json

DEXSCREENER_API = "https://api.dexscreener.com/latest/dex"

def search_token(query):
    """Search for tokens by name or address"""
    url = f"{DEXSCREENER_API}/search/?q={query}"
    response = requests.get(url)
    return response.json()

def get_token_pairs(chain, address):
    """Get all pairs for a specific token"""
    url = f"{DEXSCREENER_API}/tokens/{chain}/{address}"
    response = requests.get(url)
    return response.json()

def analyze_token(data):
    """Analyze token data and extract key metrics"""
    if not data.get('pairs'):
        return {"error": "No pairs found"}

    pair = data['pairs'][0]  # Primary pair

    analysis = {
        "name": pair.get('baseToken', {}).get('name'),
        "symbol": pair.get('baseToken', {}).get('symbol'),
        "price_usd": pair.get('priceUsd'),
        "liquidity_usd": pair.get('liquidity', {}).get('usd'),
        "fdv": pair.get('fdv'),
        "volume_24h": pair.get('volume', {}).get('h24'),
        "price_change_24h": pair.get('priceChange', {}).get('h24'),
        "txns_24h_buys": pair.get('txns', {}).get('h24', {}).get('buys'),
        "txns_24h_sells": pair.get('txns', {}).get('h24', {}).get('sells'),
        "dex": pair.get('dexId'),
        "pair_address": pair.get('pairAddress'),
        "url": pair.get('url')
    }

    # Calculate risk score
    liquidity = float(analysis['liquidity_usd'] or 0)
    volume = float(analysis['volume_24h'] or 0)

    risk_score = 10
    if liquidity > 100000: risk_score -= 2
    if liquidity > 500000: risk_score -= 2
    if volume > liquidity * 0.5: risk_score -= 2
    if analysis['txns_24h_buys'] > analysis['txns_24h_sells']: risk_score -= 1

    analysis['risk_score'] = max(1, risk_score)

    return analysis

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python dexscreener-api.py <contract_address_or_name>")
        sys.exit(1)

    query = sys.argv[1]

    # Try to search first
    print(f"Searching for: {query}")
    results = search_token(query)

    if results.get('pairs'):
        analysis = analyze_token(results)
        print(json.dumps(analysis, indent=2))
    else:
        print(json.dumps({"error": "No results found"}, indent=2))
