import os
import requests
import random

tokens = [
    ("BTCUSDT", "Bitcoin", "$BTC", 65000.0, 1.2),
    ("ETHUSDT", "Ethereum", "$ETH", 3500.0, -0.8),
    ("SOLUSDT", "Solana", "$SOL", 140.0, 3.5),
    ("BNBUSDT", "Binance Coin", "$BNB", 580.0, 0.5),
    ("XRPUSDT", "XRP", "$XRP", 0.55, 2.1),
    ("ADAUSDT", "Cardano", "$ADA", 0.45, -1.0),
    ("DOGEUSDT", "Dogecoin", "$DOGE", 0.12, 4.2),
    ("AVAXUSDT", "Avalanche", "$AVAX", 25.0, 1.8),
    ("DOTUSDT", "Polkadot", "$DOT", 6.5, -0.3),
    ("LINKUSDT", "Chainlink", "$LINK", 14.2, 2.7)
]

t1, t2 = random.sample(tokens, 2)

# Intentamos obtener datos reales de Binance de forma segura
try:
    r1 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={t1[0]}", timeout=5).json()
    val1 = float(r1.get('lastPrice', t1[3]))
    pct1 = float(r1.get('priceChangePercent', t1[4]))
except:
    val1, pct1 = t1[3], t1[4]

try:
    r2 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={t2[0]}", timeout=5).json()
    val2 = float(r2.get('lastPrice', t2[3]))
    pct2 = float(r2.get('priceChangePercent', t2[4]))
except:
    val2, pct2 = t2[3], t2[4]

textos_generados = [
    (
        f"🎯 [SEÑAL DE TRADING EN VIVO]\n\n"
        f"El movimiento actual de los activos digitales exige atención milimétrica:\n"
        f"🔹 {t1[2]} ({t1[1]}): ${val1:,.4f} | Cambio: {pct1:+.2f}%\n"
        f"🔹 {t2[2]} ({t2[1]}): ${val2:,.4f} | Cambio: {pct2:+.2f}%\n\n"
        f"¿Estás operando en corto o esperas un rebote? Déjamelo saber en los comentarios 👇\n\n"
        f"#Crypto #BinanceSquare {t1[2]} {t2[2]} #Trading"
    ),
    (
        f"🔥 [INFORME TÉCNICO DE ÚLTIMA HORA]\n\n"
        f"Analizando el comportamiento de las principales altcoins en este bloque:\n"
        f"• {t1[2]} marca ${val1:,.4f} con un rendimiento del {pct1:+.2f}%\n"
        f"• {t2[2]} se sitúa en ${val2:,.4f} variando un {pct2:+.2f}%\n\n"
        f"La gestión de riesgo es clave en estos niveles de volatilidad. ¿Cómo va tu cartera hoy? 🧠💰\n\n"
        f"#Crypto #BinanceSquare {t1[2]} {t2[2]} #Altcoins"
    ),
    (
        f"⚡️ [MONITOREO DE MERCADO]\n\n"
        f"Nuevos datos revelados en el gráfico de 1H para:\n"
        f"1️⃣ {t1[1]} ({t1[2]}): ${val1:,.4f} ({pct1:+.2f}%)\n"
        f"2️⃣ {t2[1]} ({t2[2]}): ${val2:,.4f} ({pct2:+.2f}%)\n\n"
        f"¿Hacia dónde crees que se inclinará la balanza hoy? ¡Te leo abajo! 📊\n\n"
        f"#Crypto #BinanceSquare {t1[2]} {t2[2]} #Analisis"
    )
]

publicacion_final = random.choice(textos_generados)

url = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
api_key = os.environ.get("BINANCE_KEY")

headers = {
    "X-Square-OpenAPI-Key": api_key,
    "Content-Type": "application/json",
    "clienttype": "binanceSkill"
}

payload = {
    "bodyTextOnly": publicacion_final
}

respuesta = requests.post(url, headers=headers, json=payload)
print("Respuesta de Binance:", respuesta.text)
