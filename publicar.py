import os
import requests
import random

# Lista base con tokens orientados a futuros (puedes agregar los que quieras)
tokens = [
    ("BTCUSDT", "Bitcoin", "$BTC", 65000.0, 1.2),
    ("ETHUSDT", "Ethereum", "$ETH", 3500.0, -0.8),
    ("SOLUSDT", "Solana", "$SOL", 140.0, 3.5),
    ("BNBUSDT", "Binance Coin", "$BNB", 580.0, 0.5),
    ("XRPUSDT", "XRP", "$XRP", 0.55, 2.1)
]

t1, t2 = random.sample(tokens, 2)

# Consulta directa al endpoint oficial de FUTUROS de Binance (/fapi/)
try:
    r1 = requests.get(f"https://fapi.binance.com/fapi/v1/ticker/24hr?symbol={t1[0]}", timeout=5).json()
    val1 = float(r1.get('lastPrice', t1[3]))
    pct1 = float(r1.get('priceChangePercent', t1[4]))
except:
    val1, pct1 = t1[3], t1[4]

try:
    r2 = requests.get(f"https://fapi.binance.com/fapi/v1/ticker/24hr?symbol={t2[0]}", timeout=5).json()
    val2 = float(r2.get('lastPrice', t2[3]))
    pct2 = float(r2.get('priceChangePercent', t2[4]))
except:
    val2, pct2 = t2[3], t2[4]

# Formatos de texto dinámicos y variados enfocados en derivados
opciones = [
    (
        f"📊 [INFORME FLASH DE FUTUROS]\n\n"
        f"Movimientos clave detectados en el mercado de derivados:\n"
        f"• {t1[1]} ({t1[2]}): ${val1:,.4f} ({pct1:+.2f}%)\n"
        f"• {t2[1]} ({t2[2]}): ${val2:,.4f} ({pct2:+.2f}%)\n\n"
        f"¿Cuál de estos dos activos liderará el próximo impulso con apalancamiento? Coméntalo 🚀\n\n"
        f"#BinanceSquare #CryptoFutures #Trading {t1[2]} {t2[2]}"
    ),
    (
        f"💡 [RADAR DE OPORTUNIDADES - DERIVADOS]\n\n"
        f"Analizando la fuerza de tendencia en temporalidad corta:\n"
        f"- {t1[2]} cotiza en ${val1:,.4f} con una variación de {pct1:+.2f}%\n"
        f"- {t2[2]} se posiciona en ${val2:,.4f} con un cambio de {pct2:+.2f}%\n\n"
        f"Mantén tu gestión de riesgo clara y opera con responsabilidad. ¿Posicionado en long o short? 📈\n\n"
        f"#BinanceSquare #Futures #MercadoCripto {t1[2]} {t2[2]}"
    )
]

mensaje_final = random.choice(opciones)

url = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
api_key = os.environ.get("BINANCE_KEY")

headers = {
    "X-Square-OpenAPI-Key": api_key,
    "Content-Type": "application/json",
    "clienttype": "binanceSkill"
}

payload = {
    "bodyTextOnly": mensaje_final
}

respuesta = requests.post(url, headers=headers, json=payload)
print("Respuesta de Binance:", respuesta.text)

