import os
import requests
import random

# Consultamos directamente el endpoint público de Futuros de Binance
url_futuros = "https://fapi.binance.com/fapi/v1/ticker/24hr"

try:
    response = requests.get(url_futuros, timeout=10)
    data = response.json()
    
    # Filtramos solo los pares que terminan en USDT (mercado de futuros USDT-M)
    pares_usdt = [item for item in data if item['symbol'].endswith('USDT')]
    
    # Seleccionamos 3 criptomonedas al azar del mercado de futuros
    seleccionadas = random.sample(pares_usdt, 3)
    
    # Extraemos los datos limpios
    c1, c2, c3 = seleccionadas[0], seleccionadas[1], seleccionadas[2]
    
    s1, p1, v1 = c1['symbol'].replace('USDT', ''), float(c1['lastPrice']), float(c1['priceChangePercent'])
    s2, p2, v2 = c2['symbol'].replace('USDT', ''), float(c2['lastPrice']), float(c2['priceChangePercent'])
    s3, p3, v3 = c3['symbol'].replace('USDT', ''), float(c3['lastPrice']), float(c3['priceChangePercent'])

except Exception as e:
    # Respaldo por seguridad en caso de fallo de red
    s1, p1, v1 = "BTC", 65000.0, 1.2
    s2, p2, v2 = "ETH", 3500.0, -0.5
    s3, p3, v3 = "SOL", 140.0, 3.4

# Diseños de mensajes enfocados 100% en el mercado de derivados / futuros
plantillas = [
    (
        f"⚡ [RADAR DE FUTUROS & APalancamiento]\n\n"
        f"Monitoreando la volatilidad en el mercado de derivados:\n"
        f"🔹 ${s1}: ${p1:,.4f} ({v1:+.2f}%)\n"
        f"🔹 ${s2}: ${p2:,.4f} ({v2:+.2f}%)\n\n"
        f"¿Ves oportunidad de entrada en long o prefieres buscar cortos en estas zonas? 📊👇\n\n"
        f"#BinanceSquare #CryptoFutures #${s1} #${s2} #Trading"
    ),
    (
        f"📈 [ANÁLISIS TÉCNICO DE DERIVADOS]\n\n"
        f"Revisando los movimientos clave de las últimas horas:\n"
        f"• ${s1} -> Precio: ${p1:,.4f} | Variación: {v1:+.2f}%\n"
        f"• ${s3} -> Precio: ${p3:,.4f} | Variación: {v3:+.2f}%\n\n"
        f"La gestión de riesgo y el apalancamiento controlado marcan la diferencia. ¿Cómo vas hoy? 🧠\n\n"
        f"#BinanceSquare #Futures #${s1} #${s3} #Crypto"
    ),
    (
        f"🔥 [FLUJO DE PRECIO EN FUTUROS]\n\n"
        f"Seguimiento de tendencia en tiempo real:\n"
        f"1. ${s2} cotiza en ${p2:,.4f} con un movimiento de {v2:+.2f}%\n"
        f"2. ${s3} cotiza en ${p3:,.4f} con un movimiento de {v3:+.2f}%\n\n"
        f"¿Hacia dónde crees que liquidarán el próximo movimiento? ¡Comenta abajo! 🚀\n\n"
        f"#BinanceSquare #Derivados #${s2} #${s3} #Trading"
    )
]

# Selección aleatoria para evitar repeticiones
mensaje_final = random.choice(plantillas)

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

res_pub = requests.post(url_binance, headers=headers, json=payload)
print("Respuesta de Binance:", res_pub.text)
