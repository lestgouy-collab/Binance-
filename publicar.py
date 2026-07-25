import os
import requests
import random
import time
import xml.etree.ElementTree as ET

# ---------------- CONFIGURACIÓN ----------------
# Poné tu clave API acá o configurala como variable de entorno
BINANCE_API_KEY = os.environ.get("BINANCE_KEY", "PONÉ_TU_CLAVE_ACÁ_SI_NO_USAS_VARIABLES")
INTERVALO_PUBLICACION = 45  # Minutos entre cada publicación (no hagas menos de 30 para evitar bloqueos)

# ---------------- FUNCIÓN PARA OBTENER NOTICIAS NUEVAS EN CADA CICLO ----------------
def obtener_noticias():
    titulares = []
    try:
        res = requests.get("https://es.cointelegraph.com/rss", timeout=10)
        if res.status_code == 200:
            raiz = ET.fromstring(res.content)
            for item in raiz.findall(".//item"):
                titulo = item.find("title")
                if titulo is not None and titulo.text:
                    titulares.append(titulo.text.strip())
    except Exception as e:
        print(f"⚠️ Falló RSS: {e}")
    
    # Respaldo si falla la fuente
    if not titulares:
        return [
            "Volatilidad marcada en los principales activos de futuros.",
            "Movimientos de capital institucional mueven el mercado.",
            "Niveles clave de soporte y resistencia a seguir hoy.",
            "Liquidaciones acumuladas marcan la tendencia de la sesión."
        ]
    return titulares

# ---------------- FUNCIÓN PARA TRAER PRECIOS ACTUALIZADOS ----------------
def obtener_mercado():
    try:
        res = requests.get("https://fapi.binance.com/fapi/v1/ticker/24hr", timeout=10).json()
        pares = [p for p in res if p["symbol"].endswith("USDT") and "_" not in p["symbol"]]
        seleccion = random.sample(pares, 2)
        m1 = seleccion[0]
        m2 = seleccion[1]
        return (
            m1["symbol"].replace("USDT",""),
            float(m1["lastPrice"]),
            float(m1["priceChangePercent"]),
            m2["symbol"].replace("USDT",""),
            float(m2["lastPrice"]),
            float(m2["priceChangePercent"])
        )
    except Exception as e:
        print(f"⚠️ Falló mercado: {e}")
        return "BTC", 78500, 3.2, "ETH", 2380, 2.8

# ---------------- FUNCIÓN PARA PUBLICAR EN BINANCE ----------------
def publicar(contenido):
    url = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"
    cabeceras = {
        "X-Square-OpenAPI-Key": BINANCE_API_KEY,
        "Content-Type": "application/json"
    }
    datos = {"bodyTextOnly": contenido}
    try:
        resp = requests.post(url, headers=cabeceras, json=datos, timeout=20)
        print(f"📤 Respuesta: {resp.status_code} | {resp.text[:200]}")
        return resp.json().get("code") == "000000"
    except Exception as e:
        print(f"❌ Error publicación: {e}")
        return False

# ---------------- BUCLE PRINCIPAL: SE REPITE Y ACTUALIZA TODO ----------------
if __name__ == "__main__":
    print("✅ BOT INICIADO: Noticias y precios en tiempo real")
    while True:
        # 1. TRAE NOTICIAS NUEVAS EN CADA VUELTA
        noticias = obtener_noticias()
        titular = random.choice(noticias)
        
        # 2. TRAE PRECIOS ACTUALIZADOS
        t1, p1, porc1, t2, p2, porc2 = obtener_mercado()
        
        # 3. ARMA EL MENSAJE SIEMPRE DIFERENTE
        mensaje = (
            f"📰 ACTUALIZACIÓN MERCADO | {time.strftime('%d/%m %H:%M')}\n\n"
            f"📌 {titular}\n\n"
            f"📊 Datos futuros en vivo:\n"
            f"• ${t1}: ${p1:,.4f} ({porc1:+.2f}%)\n"
            f"• ${t2}: ${p2:,.4f} ({porc2:+.2f}%)\n\n"
            f"¿Cómo ves la tendencia? Comenta 👇\n"
            f"#BinanceSquare #Futuros #${t1} #${t2}"
        )
        
        # 4. PUBLICA Y ESPERA
        ok = publicar(mensaje)
        if ok: print("✅ PUBLICADO CORRECTAMENTE")
        print(f"⏳ Siguiente en {INTERVALO_PUBLICACION}min...\n")
        time.sleep(INTERVALO_PUBLICACION * 60)
        
