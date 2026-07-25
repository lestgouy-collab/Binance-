import os
import requests
import random

# Fuente estable de CoinGecko para los datos
url_mercado = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=15&page=1&sparkline=false"

try:
    response = requests.get(url_mercado, timeout=10)
    data = response.json()
    m1, m2 = random.sample(data, 2)
    
    nombre1, simbolo1, precio1, cambio1 = m1['name'], m1['symbol'].upper(), m1['current_price'], m1['price_change_percentage_24h']
    nombre2, simbolo2, precio2, cambio2 = m2['name'], m2['symbol'].upper(), m2['current_price'], m2['price_change_percentage_24h']
except Exception as e:
    nombre1, simbolo1, precio1, cambio1 = "Bitcoin", "BTC", 65000.0, 1.5
    nombre2, simbolo2, precio2, cambio2 = "Ethereum", "ETH", 3500.0, -0.5

# Banco de textos analíticos
textos_analisis = [
    (
        f"📊 [ANÁLISIS DE FLUJO INSTITUCIONAL]\n\n"
        f"El comportamiento del mercado muestra señales clave:\n"
        f"• ${simbolo1} ({nombre1}): ${precio1:,.2f} USD ({cambio1:+.2f}%)\n"
        f"• ${simbolo2} ({nombre2}): ${precio2:,.2f} USD ({cambio2:+.2f}%)\n\n"
        f"¿Estás acumulando en esta zona o prefieres esperar una corrección mayor? 🧠👇\n\n"
        f"#Crypto #BinanceSquare ${simbolo1} ${simbolo2} #Trading"
    ),
    (
        f"⚡️ [INFORME TÉCNICO DE ACTIVIDAD]\n\n"
        f"Monitoreando los cambios en la capitalización y fuerza de los activos:\n"
        f"1️⃣ {nombre1} (${simbolo1}) cotiza en ${precio1:,.2f} con un movimiento de {cambio1:+.2f}%\n"
        f"2️⃣ {nombre2} (${simbolo2}) cotiza en ${precio2:,.2f} con un movimiento de {cambio2:+.2f}%\n\n"
        f"La disciplina marca la diferencia. ¿Cómo va tu plan hoy? 📈\n\n"
        f"#Crypto #BinanceSquare ${simbolo1} ${simbolo2} #Altcoins"
    )
]

mensaje_final = random.choice(textos_analisis)

# Lista de imágenes atractivas relacionadas con criptomonedas (puedes cambiarlas o usar tus propias URLs públicas)
imagenes_pool = [
    "https://images.unsplash.com/photo-1621416894569-0f39ed31d247?q=80&w=1000&auto=format&fit=crop", # Gráficos trading
    "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?q=80&w=1000&auto=format&fit=crop", # Cripto abstracto
    "https://images.unsplash.com/photo-1642543492481-44e81e3914a7?q=80&w=1000&auto=format&fit=crop"  # Bitcoin / Monedas
]

imagen_seleccionada = random.choice(imagenes_pool)

# Envío a la API de Binance Square con soporte de imagen y texto
url_binance = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
api_key = os.environ.get("BINANCE_KEY")

headers = {
    "X-Square-OpenAPI-Key": api_key,
    "Content-Type": "application/json",
    "clienttype": "binanceSkill"
}

# Payload estructurado para enviar texto y la imagen adjunta
payload = {
    "bodyTextOnly": mensaje_final,
    "imgs": [imagen_seleccionada]
}

res_pub = requests.post(url_binance, headers=headers, json=payload)
print("Respuesta de Binance:", res_pub.text)
