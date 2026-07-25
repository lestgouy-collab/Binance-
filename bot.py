import os
import requests
import random

# Lista masiva de criptomonedas para alternar al azar
criptos_disponibles = [
    ("BTCUSDT", "Bitcoin", "$BTC"),
    ("ETHUSDT", "Ethereum", "$ETH"),
    ("SOLUSDT", "Solana", "$SOL"),
    ("BNBUSDT", "Binance Coin", "$BNB"),
    ("XRPUSDT", "XRP", "$XRP"),
    ("ADAUSDT", "Cardano", "$ADA"),
    ("DOGEUSDT", "Dogecoin", "$DOGE"),
    ("AVAXUSDT", "Avalanche", "$AVAX"),
    ("DOTUSDT", "Polkadot", "$DOT"),
    ("LINKUSDT", "Chainlink", "$LINK")
]

try:
    # Seleccionar 2 criptomonedas al azar
    seleccionadas = random.sample(criptos_disponibles, 2)
    c1_symbol, c1_name, c1_tag = seleccionadas[0]
    c2_symbol, c2_name, c2_tag = seleccionadas[1]

    # Consultar datos en tiempo real con timeout controlado
    res1 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={c1_symbol}", timeout=15).json()
    res2 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={c2_symbol}", timeout=15).json()
    
    p1 = float(res1['lastPrice'])
    ch1 = float(res1['priceChangePercent'])
    
    p2 = float(res2['lastPrice'])
    ch2 = float(res2['priceChangePercent'])
    
    estado1 = "EN TENDENCIA ALCISTA 📈" if ch1 >= 0 else "ZONA DE SOPORTE / BAJISTA 📉"
    estado2 = "EN TENDENCIA ALCISTA 📈" if ch2 >= 0 else "ZONA DE SOPORTE / BAJISTA 📉"

    # Bancos masivos de títulos completamente diferentes y llamativos
    titulares = [
        "⚡️ [RADAR CRIPTO] Movimientos clave en vivo:",
        "🔥 [INFORME EXCLUSIVO] Análisis de volatilidad instantánea:",
        "🎯 [ALERTA DE TRADING] ¿Qué están haciendo estas altcoins?:",
        "📊 [SEGUIMIENTO EN TIEMPO REAL] Radiografía del mercado actual:",
        "💡 [actualización RÁPIDA] Oportunidades detectadas en el gráfico:"
    ]

    # Estilos de redacción y formatos de texto variados para los cuerpos del análisis
    cuerpos = [
        (
            f"• Activo analizado -> {c1_tag}: ${p1:,.4f} USD (Variación 24h: {ch1:+.2f}% | {estado1})\n"
            f"• Activo analizado -> {c2_tag}: ${p2:,.4f} USD (Variación 24h: {ch2:+.2f}% | {estado2})\n\n"
            f"El comportamiento del order book muestra actividad interesante. ¿Operas en corto o en largo hoy?"
        ),
        (
            f"📉 Reporte técnico express:\n"
            f"1. {c1_tag} marca un precio de ${p1:,.4f} ({ch1:+.2f}%). Condición: {estado1}\n"
            f"2. {c2_tag} se sitúa en ${p2:,.4f} ({ch2:+.2f}%). Condición: {estado2}\n\n"
            f"Las manos institucionales se mueven con cautela. ¿Cuál es tu plan de acción?"
        ),
        (
            f"⚠️ Actualización de última hora:\n"
            f"• {c1_tag} -> ${p1:,.4f} | Cambio: {ch1:+.2f}%\n"
            f"• {c2_tag} -> ${p2:,.4f} | Cambio: {ch2:+.2f}%\n\n"
            f"La presión compradora y vendedora está disputándose este nivel clave. ¿Hacia dónde romperá?"
        )
    ]

    cierres = [
        "Déjame tu lectura del mercado en los comentarios y sígueme para más análisis diarios 🚀",
        "La gestión de riesgo es la clave del éxito. ¿Estás dentro o fuera de esta jugada? 🧠",
        "Comparte tu estrategia y recuerda asegurar beneficios en cada operación 💰",
        "¿Ves un rebote inminente o una corrección mayor? Te leo abajo 👇"
    ]

    mensaje = (
        f"{random.choice(titulares)}\n\n"
        f"{random.choice(cuerpos)}\n\n"
        f"{random.choice(cierres)}\n\n"
        f"#Crypto #BinanceSquare {c1_tag} {c2_tag} #Trading #Analisis"
    )

except Exception as e:
    # Bloque de respaldo alternativo totalmente randomizado para evitar repetición idéntica
    alt_lista = [
        ("SOLUSDT", "Solana", "$SOL"), 
        ("ADAUSDT", "Cardano", "$ADA"), 
        ("XRPUSDT", "XRP", "$XRP"), 
        ("DOGEUSDT", "Dogecoin", "$DOGE")
    ]
    m_bk = random.choice(alt_lista)
    
    mensaje = (
        f"⚡️ [MONITOREO DE ACTIVOS]\n\n"
        f"El token {m_bk[2]} ({m_bk[1]}) registra movimientos interesantes en temporalidades de corto plazo. Los traders atentos están vigilando los puntos de entrada.\n\n"
        f"¿Qué opinas de la dirección actual del precio? Comenta abajo 👇\n\n"
        f"#Crypto #BinanceSquare {m_bk[2]} #Trading"
    )

# 3. Enviar a la API de Binance Square
url = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
api_key = os.environ.get("BINANCE_KEY")

headers = {
    "X-Square-OpenAPI-Key": api_key,
    "Content-Type": "application/json",
    "clienttype": "binanceSkill"
}

payload = {
    "bodyTextOnly": mensaje
}

response = requests.post(url, headers=headers, json=payload)
print("Respuesta de Binance:", response.text)
