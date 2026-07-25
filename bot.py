import os
import requests
import random

# Lista grande de criptomonedas populares para alternar aleatoriamente en cada post
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
    # Seleccionamos al azar 2 criptomonedas diferentes de la lista en cada ejecución
    seleccionadas = random.sample(criptos_disponibles, 2)
    c1_symbol, c1_name, c1_tag = seleccionadas[0]
    c2_symbol, c2_name, c2_tag = seleccionadas[1]

    # Consultar datos en tiempo real para las dos criptomonedas elegidas
    res1 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={c1_symbol}", timeout=10).json()
    res2 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={c2_symbol}", timeout=10).json()
    
    p1 = float(res1['lastPrice'])
    ch1 = float(res1['priceChangePercent'])
    
    p2 = float(res2['lastPrice'])
    ch2 = float(res2['priceChangePercent'])
    
    tend1 = "🚀 FUERTE AL ALZA 📈" if ch1 > 1 else ("🟢 LIGERO ASCENSO" if ch1 >= 0 else "📉 EN DESCENSO / SOPORTE")
    tend2 = "🚀 FUERTE AL ALZA 📈" if ch2 > 1 else ("🟢 LIGERO ASCENSO" if ch2 >= 0 else "📉 EN DESCENSO / SOPORTE")

    # Bancos masivos de textos completamente variados para asegurar 0 repetición
    titulares = [
        f"🔥 ¡ANÁLISIS DE ÚLTIMA HORA! El mercado se mueve rápido y estas dos joyas están dando señales críticas:",
        f"⚡️ ¡ATENCIÓN INVERSIONISTAS! Radiografía del movimiento actual en los principales activos:",
        f"🎯 ¡RADAR DE TRADING ACTIVADO! Analicemos la volatilidad que están registrando estos tokens:",
        f"📊 ¡INFORME DE TENDENCIAS! Las posiciones se reconfiguran y esto es lo que hacen los precios ahora mismo:",
        f"💡 ¡VISTA RÁPIDA AL TABLERO! No te pierdas cómo están reaccionando estos mercados:"
    ]

    cuerpos = [
        f"• {c1_tag} ({c1_name}): ${p1:,.4f} USD ({ch1:+.2f}%) -> {tend1}\n• {c2_tag} ({c2_name}): ${p2:,.4f} USD ({ch2:+.2f}%) -> {tend2}",
        f"📉 Datos en directo:\n- {c1_tag}: ${p1:,.4f} ({ch1:+.2f}%)\n- {c2_tag}: ${p2:,.4f} ({ch2:+.2f}%)\n¡Vigila de cerca el volumen de negociación!",
        f"📈 Seguimiento técnico express:\n1️⃣ {c1_tag} cotiza en ${p1:,.4f} con un cambio de {ch1:+.2f}%.\n2️⃣ {c2_tag} marca ${p2:,.4f} variando un {ch2:+.2f}%."
    ]

    cierres = [
        "¿Hacemos entradas en LONG o esperamos corrección? Deja tu opinión abajo 👇",
        "El riesgo se gestiona con cabeza fría. ¿Cuál de las dos tienes en tu radar hoy? 🧠",
        "Las oportunidades aparecen cuando hay volatilidad. ¿Estás operando este movimiento? 🚀",
        "Coméntame si ves ruptura inminente o consolidación en estos niveles 📊"
    ]

    mensaje = (
        f"{random.choice(titulares)}\n\n"
        f"{random.choice(cuerpos)}\n\n"
        f"{random.choice(cierres)}\n\n"
        f"#Crypto #BinanceSquare {c1_tag} {c2_tag} #Trading #Altcoins"
    )

except Exception as e:
    # Plan B totalmente dinámico por si falla la red, usando otras monedas al azar
    alt_coins = [("$BTC", "Bitcoin"), ("$ETH", "Ethereum"), ("$SOL", "Solana"), ("$XRP", "XRP"), ("$DOGE", "Dogecoin")]
    m1, m2 = random.sample(alt_coins, 2)
    
    mensaje = (
        f"🚨 ¡ACTUALIZACIÓN FLASH DEL MERCADO!\n\n"
        f"La acción de precio en {m1[0]} ({m1[1]}) y {m2[0]} ({m2[1]}) muestra un escenario interesante para los traders con paciencia.\n\n"
        f"Mantén tu estrategia clara y protege tu capital. ¿Hacia dónde irá la tendencia principal hoy? 🤔👇\n\n"
        f"#Crypto #BinanceSquare {m1[0]} {m2[0]} #Trading"
    )

# 3. Publicar en Binance Square mediante la API
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


