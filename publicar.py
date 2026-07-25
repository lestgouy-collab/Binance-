import os
import requests
import random

# Usamos la API pública de CoinGecko, que es ultra estable para GitHub Actions
url_mercado = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=15&page=1&sparkline=false"

try:
    response = requests.get(url_mercado, timeout=10)
    data = response.json()
    
    # Seleccionamos dos monedas al azar de la lista real del mercado global
    m1, m2 = random.sample(data, 2)
    
    nombre1, simbolo1, precio1, cambio1 = m1['name'], m1['symbol'].upper(), m1['current_price'], m1['price_change_percentage_24h']
    nombre2, simbolo2, precio2, cambio2 = m2['name'], m2['symbol'].upper(), m2['current_price'], m2['price_change_percentage_24h']
    
except Exception as e:
    # Respaldo inteligente por si falla la red externa
    nombre1, simbolo1, precio1, cambio1 = "Bitcoin", "BTC", 65000.0, 1.5
    nombre2, simbolo2, precio2, cambio2 = "Ethereum", "ETH", 3500.0, -0.5

# Variaciones analíticas profesionales para maximizar engagement
textos_analisis = [
    (
        f"📊 [ANÁLISIS DE FLUJO INSTITUCIONAL]\n\n"
        f"El comportamiento del mercado en temporalidad diaria muestra señales clave:\n"
        f"• ${simbolo1} ({nombre1}): ${precio1:,.2f} USD ({cambio1:+.2f}%)\n"
        f"• ${simbolo2} ({nombre2}): ${precio2:,.2f} USD ({cambio2:+.2f}%)\n\n"
        f"¿Estás acumulando en esta zona o prefieres esperar una corrección mayor? Te leo en los comentarios 🧠👇\n\n"
        f"#Crypto #BinanceSquare ${simbolo1} ${simbolo2} #Trading"
    ),
    (
        f"⚡️ [INFORME TÉCNICO DE ACTIVIDAD]\n\n"
        f"Monitoreando los cambios en la capitalización y fuerza de los activos:\n"
        f"1️⃣ {nombre1} (${simbolo1}) cotiza en ${precio1:,.2f} con un movimiento de {cambio1:+.2f}%\n"
        f"2️⃣ {nombre2} (${simbolo2}) cotiza en ${precio2:,.2f} con un movimiento de {cambio2:+.2f}%\n\n"
        f"La disciplina marca la diferencia entre un trader rentable y uno emocional. ¿Cómo va tu plan hoy? 📈\n\n"
        f"#Crypto #BinanceSquare ${simbolo1} ${simbolo2} #Altcoins"
    ),
    (
        f"🔥 [RADAR DE TENDENCIA GLOBAL]\n\n"
        f"Las métricas actuales revelan un comportamiento interesante en el tablero:\n"
        f"- ${simbolo1} | Precio: ${precio1:,.2f} | Variación 24h: {cambio1:+.2f}%\n"
        f"- ${simbolo2} | Precio: ${precio2:,.2f} | Variación 24h: {cambio2:+.2f}%\n\n"
        f"¿Hacia dónde inclinas tu perspectiva para las siguientes horas? ¡Comenta abajo! 🚀\n\n"
        f"#Crypto #BinanceSquare ${simbolo1} ${simbolo2} #AnalisisTecnico"
    )
]

mensaje_final = random.choice(textos_analisis)

# Envío directo a la API de Binance Square
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

res_pub = requests.post(url_binance, headers=headers, json=payload)
print("Respuesta de Binance:", res_pub.text)
