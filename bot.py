import os
import requests
import random

# Lista masiva de pares de criptomonedas
criptos_pool = [
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

# Banco gigante de noticias y ganchos de mercado aleatorios e independientes
banco_noticias = [
    lambda c1, c2, p1, ch1, p2, ch2: (
        f"🚨 ¡IMPACTO EN EL ORDER BOOK! Se detectan liquidaciones masivas en los principales exchanges.\n\n"
        f"• {c1[2]} ({c1[1]}): ${p1:,.2f} ({ch1:+.2f}%)\n"
        f"• {c2[2]} ({c2[1]}): ${p2:,.2f} ({ch2:+.2f}%)\n\n"
        f"¿Las ballenas están manipulando el precio o es una sana corrección? Coméntame tu lectura abajo 👇\n\n"
        f"#Crypto #BinanceSquare {c1[2]} {c2[2]} #BreakingNews #Trading"
    ),
    lambda c1, c2, p1, ch1, p2, ch2: (
        f"⚡️ ¡NOTICIA DE ÚLTIMA HORA! El volumen institucional se dispara repentinamente en el gráfico de 1H.\n\n"
        f"📊 Niveles actuales:\n"
        f"- {c1[2]}: ${p1:,.2f} | Variación: {ch1:+.2f}%\n"
        f"- {c2[2]}: ${p2:,.2f} | Variación: {ch2:+.2f}%\n\n"
        f"La volatilidad está al límite. ¿Estás operando en LONG o prefieres esperar en CASH? 🧠💰\n\n"
        f"#Crypto #BinanceSquare {c1[2]} {c2[2]} #Altcoins"
    ),
    lambda c1, c2, p1, ch1, p2, ch2: (
        f"🔥 ¡RUMBO CRÍTICO! Analistas reportan acumulación inusual en el ecosistema cripto hoy.\n\n"
        f"🔍 Comportamiento en vivo:\n"
        f"1️⃣ {c1[2]} ({c1[1]}): ${p1:,.2f} -> {ch1:+.2f}%\n"
        f"2️⃣ {c2[2]} ({c2[1]}): ${p2:,.2f} -> {ch2:+.2f}%\n\n"
        f"¿Crees que rompemos resistencia o nos vamos directo al soporte inferior? ¡Te leo! 📉📈\n\n"
        f"#Crypto #BinanceSquare {c1[2]} {c2[2]} #Analisis"
    ),
    lambda c1, c2, p1, ch1, p2, ch2: (
        f"🎯 ¡RADAR DE MERCADO ACTIVO! El sentimiento de los inversores cambia drásticamente en este bloque horario.\n\n"
        f"• Estado de {c1[2]}: ${p1:,.2f} ({ch1:+.2f}%)\n"
        f"• Estado de {c2[2]}: ${p2:,.2f} ({ch2:+.2f}%)\n\n"
        f"La paciencia paga más que operar por impulso. ¿Cómo va tu cartera hoy? 🚀\n\n"
        f"#Crypto #BinanceSquare {c1[2]} {c2[2]} #Trading"
    )
]

try:
    # Seleccionar 2 criptomonedas distintas al azar
    c1, c2 = random.sample(criptos_pool, 2)

    # Consultar precios reales con un tiempo de espera amplio para evitar fallos
    r1 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={c1[0]}", timeout=15).json()
    r2 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={c2[0]}", timeout=15).json()
    
    p1 = float(r1['lastPrice'])
    ch1 = float(r1['priceChangePercent'])
    
    p2 = float(r2['lastPrice'])
    ch2 = float(r2['priceChangePercent'])

    # Elegir una noticia/estructura completamente aleatoria del banco de noticias
    plantilla_noticia = random.choice(banco_noticias)
    mensaje = plantilla_noticia(c1, c2, p1, ch1, p2, ch2)

except Exception as e:
    # Respaldo dinámico alternativo por si ocurre un fallo de red puntual
    x1, x2 = random.sample(criptos_pool, 2)
    mensaje = (
        f"📊 ¡BOLETÍN FLASH DE MERCADO!\n\n"
        f"Nuevos movimientos detectados en {x1[2]} y {x2[2]}. El mapa de calor de Binance muestra cambios interesantes en la fuerza compradora.\n\n"
        f"Mantén tu estrategia clara y protege tus posiciones. ¿Hacia dónde ves el mercado? 👇\n\n"
        f"#Crypto #BinanceSquare {x1[2]} {x2[2]} #Trading"
    )

# 3. Publicar automáticamente en Binance Square
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
