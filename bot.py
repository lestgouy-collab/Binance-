import os
import requests

url = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
api_key = os.environ.get("BINANCE_KEY")

headers = {
    "X-Square-OpenAPI-Key": api_key,
    "Content-Type": "application/json",
    "clienttype": "binanceSkill"
}

payload = {
    "bodyTextOnly": "Análisis rápido de criptomonedas: $BTC y $ETH con tendencia alcista para hoy en el mercado. Mantén la cautela."
}

response = requests.post(url, headers=headers, json=payload)
print("Respuesta de Binance:", response.text)
