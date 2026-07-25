import os
import requests
import random

# Lista completa de criptomonedas con sus nombres y etiquetas
pool_criptos = [
    ("BTCUSDT", "Bitcoin", "$BTC"),
    ("ETHUSDT", "Ethereum", "$ETH"),
    ("SOLUSDT", "Solana", "$SOL"),
    ("BNBUSDT", "Binance Coin", "$BNB"),
    ("XRPUSDT", "XRP", "$XRP"),
    ("ADAUSDT", "Cardano", "$ADA"),
    ("DOGEUSDT", "Dogecoin", "$DOGE"),
    ("AVAXUSDT", "Avalanche", "$AVAX"),
    ("DOTUSDT", "Polkadot", "$DOT"),
    ("LINKUSDT", "Chainlink", "$LINK"),
    ("NEARUSDT", "NEAR Protocol", "$NEAR"),
    ("MATICUSDT", "Polygon", "$MATIC")
]

try:
    # Seleccionamos 2 criptomonedas al azar
    c1, c2 = random.sample(pool_criptos, 2)

    # Obtenemos datos reales de la API de Binance
    r1 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={c1[0]}", timeout=15).json()
    r2 = requests.get(f"https://api.binance.com/api/v3/ticker/24hr?symbol={c2[0]}", timeout=15).json()
    
    precio1 = float(r1['lastPrice'])
    cambio1 = float(r1['priceChangePercent'])
    
    precio2 = float(r2['lastPrice'])
    cambio2 = float(r2['priceChangePercent'])

    # Bancos totalmente independientes para mezclar y que NUNCA salga el mismo formato
    saludos = [
        "Atención comunidad, la sesión de hoy viene cargada de movimientos fuertes.",
        "Revisando los gráficos en temporalidad baja nos encontramos con sorpresas interesantes.",
        "El mapa de calor de los exchanges principales acaba de dar un giro inesperado.",
        "Analizando el flujo de capitales en este preciso instante para adelantarnos al movimiento.",
        "Las posiciones abiertas en futuros muestran un comportamiento inusual hoy."
    ]

    analisis_textos = [
        f"Por un lado, {c1[2]} ({c1[1]}) se cotiza sobre los ${precio1:,.4f} USD, registrando un movimiento de {cambio1:+.2f}%. Esto demuestra una presión compradora que intenta sostener el nivel clave. En paralelo, {c2[2]} ({c2[1]}) marca los ${precio2:,.4f} USD con una variación del {cambio2:+.2f}%, reflejando la indecisión de las manos fuertes en esta zona.",
        f"Profundizando en el rendimiento actual, tenemos a {c1[2]} marcando ${precio1:,.4f} (${cambio1:+.2f}%), un escenario que mantiene en alerta a los traders de scalping. Por otro lado, {c2[2]} se mueve hacia los ${precio2:,.4f} con un {cambio2:+.2f}%, sugiriendo un posible retesteo de soportes antes de la siguiente vela de una hora.",
        f"Echando un vistazo técnico, {c1[2]} opera en ${precio1:,.4f} con un balance diario de {cambio1:+.2f}%, mientras que {c2[2]} experimenta una fluctuación de {cambio2:+.2f}% situándose en ${precio2:,.4f}. La volatilidad está sirviendo para limpiar apalancamientos excesivos."
    ]

    consejos = [
        "Consejo de gestión: No persigas el precio de última hora. Espera siempre la confirmación del volumen antes de abrir operaciones en long o short.",
        "La paciencia es la herramienta más poderosa de un trader rentable. Protege tu capital y opera con la cabeza fría.",
        "Recuerda ajustar tus stops loss adecuadamente. En mercados tan volátiles, la disciplina vale más que la suerte.",
        "¿Estás acumulando activos para el largo plazo o prefieres tradear el impulso diario? Analiza bien tu estrategia."
    ]

    preguntas_finales = [
        "¿Hacia qué dirección crees que romperá el precio en las próximas horas? Déjame tu perspectiva en los comentarios 👇",
        "¿Abres posición a favor de la tendencia o esperas una corrección mayor? Te leo abajo 🧠",
        "¿Qué nivel de precio estás vigilando de cerca para estos tokens hoy? Compártelo 📊",
        "¿Ves una oportunidad clara de compra o prefieres mantener liquidez en cash? 🚀"
    ]

    # Armamos un mensaje 100% único combinando elementos al azar
    mensaje = (
        f"📊 {random.choice(saludos)}\n\n"
        f"{random.choice(analisis_textos)}\n\n"
        f"💡 {random.choice(consejos)}\n\n"
        f"{random.choice(preguntas_finales)}\n\n"
        f"#Crypto #BinanceSquare {c1[2]} {c2[2]} #Trading #AnalisisTecnico"
    )

except Exception as e:
    # Respaldo de emergencia aleatorio
    fallback_c = random.choice(pool_criptos)
    mensaje = (
        f"⚡️ Monitoreo express de mercado detecta actividad inusual en el token {fallback_c[2]} ({fallback_c[1]}). "
        f"Los volúmenes de negociación exigen máxima atención de parte de los traders de corto plazo. "
        f"¿Cómo visualizas el cierre de esta jornada? Coméntalo abajo 👇\n\n"
        f"#Crypto #BinanceSquare {fallback_c[2]} #Trading"
    )

# 3. Publicación en Binance Square
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
    
