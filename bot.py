import os
import requests
import random
import time
import xml.etree.ElementTree as ET

BINANCE_API_KEY = os.environ.get("BINANCE_KEY")

# ---------------- SOLO FUTUROS PERPETUOS ----------------
def obtener_mercado():
    try:
        res = requests.get("https://fapi.binance.com/fapi/v1/ticker/24hr", timeout=5).json()
        pares = [p for p in res if p["symbol"].endswith("USDT") and "_" not in p["symbol"]]
        seleccion = random.sample(pares, 2)
        datos = []
        for p in seleccion:
            moneda = p["symbol"].replace("USDT","")
            precio = float(p["lastPrice"])
            cambio = float(p["priceChangePercent"])
            tendencia = "📈 **SE ESPERA SUBIDA**" if cambio > 0 else "📉 **SE ESPERA BAJADA**"
            datos.append( (moneda, precio, cambio, tendencia) )
        return datos
    except:
        return [
            ("BTC", 78500, 2.8, "📈 **SE ESPERA SUBIDA**"),
            ("ETH", 2380, -1.5, "📉 **SE ESPERA BAJADA**")
        ]

# ---------------- NOTICIAS REALES ----------------
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
        "La volatilidad define el rumbo de los futuros hoy.",
        "Datos macroeconómicos mueven los contratos perpetuos.",
        "Liquidaciones masivas marcan la tendencia del mercado."
    ]

# ---------------- PUBLICAR UNA SOLA VEZ ----------------
def publicar(texto):
    url = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
    resp = requests.post(url, headers={
        "X-Square-OpenAPI-Key": BINANCE_API_KEY,
        "Content-Type": "application/json"
    }, json={"bodyTextOnly": texto}, timeout=10)
    print(f"📤 Respuesta: {resp.status_code}")
    print(f"📋 Detalle: {resp.text[:200]}")
    return resp.json().get("code") == "000000"

# ---------------- EJECUCIÓN ÚNICA ----------------
if __name__ == "__main__":
    print("✅ PREPARANDO PUBLICACIÓN ÚNICA...")
    titular = random.choice(obtener_noticias())
    m1, p1, c1, t1 = obtener_mercado()[0]
    m2, p2, c2, t2 = obtener_mercado()[1]

    mensaje = (
        f"🔥 **ALERTA FUTUROS | {time.strftime('%d/%m · %H:%M')}**\n\n"
        f"📰 NOTICIA CLAVE:\n{titular}\n\n"
        f"⚡ PREDICCIÓN Y DATOS:\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🔸 ${m1}: ${p1:,.4f} ({c1:+.2f}%)\n{t1}\n"
        f"🔸 ${m2}: ${p2:,.4f} ({c2:+.2f}%)\n{t2}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"¿Coincidís con la tendencia? ¿Vas largo o corto? 👇\n\n"
        f"#FuturosPerpetuos #Binance #Trading #{m1} #{m2}"
    )

    ok = publicar(mensaje)
    if ok:
        print("✅ ✅ PUBLICADO EXITOSAMENTE EN TU PERFIL")
    else:
        print("❌ No se pudo publicar, revisá la clave API o permisos")
        
