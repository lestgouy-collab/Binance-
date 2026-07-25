import os
import requests

try:
    res_btc = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").json()
    res_eth = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT").json()
    
    btc_price = float(res_btc['lastPrice'])
    btc_change = float(res_btc['priceChangePercent'])
    
    eth_price = float(res_eth['lastPrice'])
    eth_change = float(res_eth['priceChangePercent'])
    
    btc_trend = "AL ALZA 📈" if btc_change >= 0 else "A LA BAJA 📉"
    eth_trend = "AL ALZA 📈" if eth_change >= 0 else "A LA BAJA 📉"
    
    mensaje = (
        f"📊 Análisis de Mercado en Tiempo Real:\n\n"
        f"• $BTC (Bitcoin): ${btc_price:,.2f} USD ({btc_change:+.2f}%) -> {btc_trend}\n"
        f"• $ETH (Ethereum): ${eth_price:,.2f} USD ({eth_change:+.2f}%) -> {eth_trend}\n\n"
        f"Monitoreando las tendencias del mercado cripto. ¿Cuál es tu proyección para hoy? 👇\n\n"
        f"#Crypto #BinanceSquare #BTC #ETH"
    )
except Exception as e:
    mensaje = (
        f"📊 Actualización del mercado cripto:\n\n"
        f"Mantén tu estrategia clara analizando $BTC y $ETH en todo momento.\n\n"
        f"#Crypto #BinanceSquare #BTC #ETH"
    )

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

