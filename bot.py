import os
import requests
import random

# 1. Obtener precios reales de Binance
try:
    res_btc = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").json()
    res_eth = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT").json()
    
    btc_price = float(res_btc['lastPrice'])
    btc_change = float(res_btc['priceChangePercent'])
    
    eth_price = float(res_eth['lastPrice'])
    eth_change = float(res_eth['priceChangePercent'])
    
    btc_trend = "🚀 FUERTE AL ALZA" if btc_change > 1 else ("📈 LIGERAMENTE AL ALZA" if btc_change >= 0 else "📉 A LA BAJA")
    eth_trend = "🚀 FUERTE AL ALZA" if eth_change > 1 else ("📈 LIGERAMENTE AL ALZA" if eth_change >= 0 else "📉 A LA BAJA")

    # Listas de frases creativas y aleatorias para que cada post sea único
    introducciones = [
        "🔥 ¡Atención traders! Así se mueve el tablero en este preciso instante:",
        "📊 Monitoreo rápido de las principales criptomonedas del mercado:",
        "⚡️ Actualización express de precios y tendencias clave:",
        "🎯 Nuevos movimientos detectados en el mercado cripto hoy:",
        "💡 Analizando el pulso actual de Bitcoin y Ethereum:"
    ]
    
    preguntas = [
        "¿Hará nuevo máximo o veremos un retesteo? 👇",
        "¿Cuál es tu estrategia para las próximas horas? Dejamela en los comentarios 💭",
        "¿Estás acumulando o prefieres esperar una corrección? 📉📈",
        "El mercado no descansa. ¿Qué opinas de este movimiento? 🧠",
        "Gestión de riesgo siempre por delante. ¿Cómo ves el panorama? 🎯"
    ]

    intro_elegida = random.choice(introductions if 'introductions' in locals() else introducciones)
    pregunta_elegida = random.choice(preguntas)

    mensaje = (
        f"{intro_elegida}\n\n"
        f"• $BTC (Bitcoin): ${btc_price:,.2f} USD | Cambio 24h: {btc_change:+.2f}% -> {btc_trend}\n"
        f"• $ETH (Ethereum): ${eth_price:,.2f} USD | Cambio 24h: {eth_change:+.2f}% -> {eth_trend}\n\n"
        f"{pregunta_elegida}\n\n"
        f"#Crypto #BinanceSquare #BTC #ETH #Trading"
    )

except Exception as e:
    mensaje = (
        f"⚡️ Monitoreo activo de activos digitales en tiempo real.\n\n"
        f"Mantén tu enfoque analizando de cerca a $BTC y $ETH. ¡El mercado cambia en segundos! 📊📈\n\n"
        f"#Crypto #BinanceSquare #BTC #ETH"
    )

# 2. Publicar automáticamente en Binance Square
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
