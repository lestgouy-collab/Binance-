import os
import requests
import random
import time
import xml.etree.ElementTree as ET

BINANCE_API_KEY = os.environ.get("BINANCE_KEY")
INTERVALO_PUBLICACION = 25  # Más rápido, pero seguro

def obtener_noticias():
    titulares = []
    try:
        res = requests.get("https://es.cointelegraph.com/rss", timeout=5)
        if res.status_code == 200:
            raiz = ET.fromstring(res.content)
            for item in raiz.findall(".//item"):
                t = item.find("title")
                if t is not None and t.text:
                    titulares.append(t.text.strip())
    except:
        pass
    return titulares if titulares else [
        "Movimientos clave en futuros de Binance.",
        "Volatilidad marca la sesión de hoy.",
        "Niveles de soporte y resistencia a vigilar."
    ]

def obtener_mercado():
    try:
        res = requests.get("https://fapi.binance.com/fapi/v1/ticker/24hr", timeout=5).json()
        pares = [p for p in res if p["symbol"].endswith("USDT") and "_" not in p["symbol"]]
        s = random.sample(pares, 2)
        return (
            s[0]["symbol"].replace("USDT",""), float(s[0]["lastPrice"]), float(s[0]["priceChangePercent"]),
            s[1]["symbol"].replace("USDT",""), float(s[1]["lastPrice"]), float(s[1]["priceChangePercent"])
        )
    except:
        return "BTC", 78500, 3.2, "ETH", 2380, 2.8

def publicar(texto):
    url = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
    resp = requests.post(url, headers={
        "X-Square-OpenAPI-Key": BINANCE_API_KEY,
        "Content-Type": "application/json"
    }, json={"bodyTextOnly": texto}, timeout=10)
    print(f"📤 {resp.status_code} | {resp.text[:150]}")
    return resp.json().get("code") == "000000"

if __name__ == "__main__":
    print("✅ BOT OPTIMIZADO INICIADO")
    while True:
        titular = random.choice(obtener_noticias())
        t1,p1,porc1,t2,p2,porc2 = obtener_mercado()
        ok = publicar(
            f"📰 {time.strftime('%d/%m %H:%M')}\n{titular}\n\n📊 ${t1}: ${p1:,.4f} ({porc1:+.2f}%)\n${t2}: ${p2:,.4f} ({porc2:+.2f}%)\n¿Qué esperás? Comenta 👇\n#Futuros #${t1} #${t2}"
        )
        print(f"⏳ Siguiente en {INTERVALO_PUBLICACION}min...\n")
        time.sleep(INTERVALO_PUBLICACION * 60)
        
