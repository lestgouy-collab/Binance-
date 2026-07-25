import os
import requests
import random
import time

random.seed(int(time.time()))

# 1. Obtener una noticia de última hora de la API gratuita de CryptoPanic (o respaldo automático)
try:
    url_news = "https://cryptopanic.com/api/v1/posts/?auth_token=free&public=true&kind=news"
    res_news = requests.get(url_news, timeout=8).json()
    resultados = res_news.get('results', [])
    if resultados:
        noticia_obj = random.choice(resultados[:10]) # Elegir entre las 10 más recientes
        titular_noticia = noticia_obj.get('title', 'Actualidad relevante en el mercado cripto')
        fuente_noticia = noticia_obj.get('source', {}).get('title', 'Crypto Market')
    else:
        titular_noticia = "Alta volatilidad y movimientos clave sacuden el mercado de derivados."
        fuente_noticia = "Binance Feed"
except:
    titular_noticia = "Actualización en tiempo real sobre el flujo de capital en criptomonedas."
    fuente_noticia = "Mercado Global"

# 2. Obtener 2 criptomonedas al azar del mercado de futuros de Binance en tiempo real
try:
    url_fapi = "https://fapi.binance.com/fapi/v1/ticker/24hr"
    response = requests.get(url_fapi, timeout=8).json()
    pares_usdt = [item for item in response if item['symbol'].endswith('USDT') and '_' not in item['symbol']]
    
    s = random.sample(pares_usdt, 2)
    t1_nom, val1, pct1 = s[0]['symbol'].replace('USDT', ''), float(s[0]['lastPrice']), float(s[0]['priceChangePercent'])
    t2_nom, val2, pct2 = s[1]['symbol'].replace('USDT', ''), float(s[1]['lastPrice']), float(s[1]['priceChangePercent'])
except:
    t1_nom, val1, pct1 = "BTC", 65000.0, 1.2
    t2_nom, val2, pct2 = "ETH", 3500.0, -0.5

# 3. Estructura que integra la noticia real con los datos de futuros en vivo
mensaje_final = (
    f"📰 [NOTICIA DE ÚLTIMA HORA]\n"
    f"Fuente: {fuente_noticia}\n\n"
    f"\"{titular_noticia}\"\n\n"
    f"📊 Impacto en derivados:\n"
    f"• ${t1_nom}: ${val1:,.4f} ({pct1:+.2f}%)\n"
    f"• ${t2_nom}: ${val2:,.4f} ({pct2:+.2f}%)\n\n"
    f"¿Cómo afectará esto a tus posiciones en futuros? Déjanos tu opinión 👇\n\n"
    f"#BinanceSquare #CryptoNews #Trading #${t1_nom} #${t2_nom}"
)

# Envío oficial a la API de Binance Square
url_binance = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
api_key = os.environ.get("BINANCE_KEY")

headers = {
    "X-Square-OpenAPI-Key": api_key,
    "Content-Type": "application/json",
    "clienttype": "binanceSkill"
}

payload = {
    "bodyTextOnly": mensaje_final
}

respuesta = requests.post(url_binance, headers=headers, json=payload)
print("Respuesta de Binance:", respuesta.text)
