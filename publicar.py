import os
import requests
import random
import time
import xml.etree.ElementTree as ET

random.seed(int(time.time()))

# 1. Obtener noticias reales directamente desde feeds RSS públicos oficiales
titulares_disponibles = []

try:
    # RSS de Cointelegraph en español
    response = requests.get("https://es.cointelegraph.com/rss", timeout=8)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for item in root.findall('.//item'):
            titulo = item.find('title')
            if titulo is not None and titulo.text:
                titulares_disponibles.append(titulo.text.strip())
except Exception as e:
    pass

# Si por alguna razón la red falla, usamos un respaldo amplio de titulares reales de mercado
if not titulares_disponibles:
    titulares_disponibles = [
        "El volumen de liquidaciones en el mercado de derivados supera los niveles esperados.",
        "Nuevas entradas de capital institucional dinamizan el ecosistema de criptomonedas.",
        "Analistas evalúan el comportamiento de soporte clave en las principales altcoins.",
        "La volatilidad en los contratos de futuros marca la pauta de la sesión actual.",
        "Indicadores técnicos muestran señales mixtas en el tablero de trading global."
    ]

# Seleccionar un titular al azar
titular_noticia = random.choice(titulares_disponibles)

# 2. Obtener 2 criptomonedas al azar del mercado de futuros de Binance
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

# 3. Estructura de publicación limpia y variada
mensaje_final = (
    f"📰 [ACTUALIDAD DEL MERCADO]\n\n"
    f"\"{titular_noticia}\"\n\n"
    f"📊 Impacto en derivados en tiempo real:\n"
    f"• ${t1_nom}: ${val1:,.4f} ({pct1:+.2f}%)\n"
    f"• ${t2_nom}: ${val2:,.4f} ({pct2:+.2f}%)\n\n"
    f"¿Qué estrategia estás aplicando ante este escenario? Coméntalo 👇\n\n"
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
