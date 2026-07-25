import os
import requests
import random

# 1. Obtener datos reales de Binance para BTC y ETH
try:
    res_btc = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT", timeout=10).json()
    res_eth = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT", timeout=10).json()
    
    btc_price = float(res_btc['lastPrice'])
    btc_change = float(res_btc['priceChangePercent'])
    
    eth_price = float(res_eth['lastPrice'])
    eth_change = float(res_eth['priceChangePercent'])
    
    # Análisis detallado de tendencias
    btc_estado = "🚨 ¡ATENCIÓN TRADERS! Movimiento bajista peligroso detectado" if btc_change < 0 else "🚀 ¡OJO AQUÍ! Presión alcista imparable"
    eth_estado = "🚨 ¡Se desploma o busca soporte crítico!" if eth_change < 0 else "🔥 ¡Fuerza compradora desatada en este nivel!"

    # 2. Banco de textos largos, llamativos y aleatorios estilo análisis profesional
    ganchos = [
        f"⚠️ ¡ESTA MONEDA ESTÁ DANDO DE QUÉ HABLAR! El mercado no perdonas los despistes y la volatilidad actual está liquidando posiciones apalancadas. Analicemos los datos en frío:",
        f"🔥 ¡ALERTA ROJA EN EL MERCADO CRIPTO! Las ballenas se están moviendo rápido y la acción de precio nos deja un escenario técnico sumamente delicado. Mira esto:",
        f"📉📈 ¡GIRO INESPERADO EN LAS TENDENCIAS! Si operas sin gestión de riesgo hoy, puedes quedar atrapado. Desglosamos el comportamiento de los activos principales:",
        f"⚡️ ¡INFORME DE ÚLTIMA HORA EN EL TABLERO! El volumen de transacciones se dispara y los indicadores apuntan a un movimiento decisivo en las próximas horas:"
    ]

    reflexiones = [
        "💡 Consejo de trader: Nunca operes por emociones. Espera la confirmación de volumen antes de entrar en long o en short. ¿Estás protegido?",
        "🧠 El sentimiento del mercado cambia en segundos. Las manos débiles venden en pánico mientras los institucionales acumulan. ¿De qué lado estás?",
        "📊 Recuerda revisar tus niveles de liquidación. Un mercado bajista o alcista extremo requiere paciencia quirúrgica.",
        "🎯 La paciencia paga más que operar por desesperación. Analiza el gráfico de 4 horas antes de tomar cualquier decisión precipitada."
    ]

    gancho_elegido = random.choice(ganchos)
    reflexion_elegida = random.choice(reflexiones)

    # Construcción del mensaje largo, completo y profesional
    mensaje = (
        f"{gancho_elegido}\n\n"
        f"• Activo 1: $BTC (Bitcoin)\n"
        f"  - Precio Actual: ${btc_price:,.2f} USD\n"
        f"  - Rendimiento 24h: {btc_change:+.2f}%\n"
        f"  - Diagnóstico: {btc_estado}\n\n"
        f"• Activo 2: $ETH (Ethereum)\n"
        f"  - Precio Actual: ${eth_price:,.2f} USD\n"
        f"  - Rendimiento 24h: {eth_change:+.2f}%\n"
        f"  - Diagnóstico: {eth_estado}\n\n"
        f"{reflexion_elegida}\n\n"
        f"👇 ¿Qué opinas de este movimiento? Déjame tu análisis en los comentarios y dime si abres posición a la baja o al alza.\n\n"
        f"#Crypto #BinanceSquare #BTC #ETH #Trading #AnalisisTecnico"
    )

except Exception as e:
    # Mensaje de respaldo robusto por si falla la red momentáneamente
    mensaje = (
        f"🚨 ¡ALERTA DE MERCADO EN TIEMPO REAL!\n\n"
        f"El comportamiento de $BTC y $ETH nos muestra una volatilidad extrema. Los traders experimentados saben que este es el momento de máxima cautela y oportunidad.\n\n"
        f"📊 Mantén el ojo en los soportes claves y no olvides gestionar tu riesgo adecuadamente. El mercado recompensa la disciplina.\n\n"
        f"¿Hacia dónde crees que romperá el precio hoy? Coméntalo abajo 👇\n\n"
        f"#Crypto #BinanceSquare #BTC #ETH #Trading"
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

