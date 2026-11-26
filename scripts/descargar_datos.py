"""Descarga los 36 archivos del Drive compartido del equipo a data/raw/.

Uso:
    python scripts/descargar_datos.py          # descarga lo que falte
    python scripts/descargar_datos.py --forzar # vuelve a bajar todo

Los archivos deben estar compartidos como "Cualquier persona con el enlace".
Carpeta de Drive: https://drive.google.com/drive/folders/1ZT31mcZ_fW-3NNC3NHJ-OjU2EmOJ2CXT
"""
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = {"MC4": RAIZ / "data/raw/mc4", "SKP": RAIZ / "data/raw/skp"}

# Molino Caliente 4 (Pesquería): 24 archivos quincenales, 2025
ARCHIVOS_MC4 = {
    "MC4_PSQ Enero 1 a 15 2025.xlsx": "1ot8-f1ti0h5rbWlzL8sIO7pnAXbS97KE",
    "MC4_PSQ Enero 16 a 31 2025.xlsx": "1Vr-busbt-q1eWeBAvG_Gfl82Zk9zIzBN",
    "MC4_PSQ Febrero 1 a 15 2025.xlsx": "1MG8eXy2wKhYz-cvEFF5xOuzMzM5ZRUsI",
    "MC4_PSQ Febrero 16 a 28 2025.xlsx": "1KnhKDqb7mGhvAMWKfu-dNs7CswrAzuvS",
    "MC4_PSQ Marzo 1 a 15 2025.xlsx": "1mswAchvO5tJAwxpPG43etEpBnctLPb3b",
    "MC4_PSQ Marzo 16 a 31 2025.xlsx": "1JezpbzONdZvwtJesns7mSQzqRSKiLbhM",
    "MC4_PSQ Abril 1 a 15 2025.xlsx": "1xMVD5rfnVwbSP-QyOsJe9kWrFsiKtKPB",
    "MC4_PSQ Abril 16 a 30 2025.xlsx": "148bbJlRC1Uyu3VDrEiHN9l90NpEOJ2Ac",
    "MC4_PSQ Mayo 1 a 15 2025.xlsx": "1ezWcYljTTBVeCt1oV7qObAtCX_yQhw34",
    "MC4_PSQ Mayo 16 a 31 2025.xlsx": "1qVGGw3llo3_wbI7f8miJAxskgPGPtwzf",
    "MC4_PSQ Junio 1 a 15 2025.xlsx": "1cMbbrVYHEVo3do6zOpgjNH4GSYP9LTu8",
    "MC4_PSQ Junio 16 a 30 2025.xlsx": "1dK2KmOOFtsczlP8BeXwfAqyZrm606FxZ",
    "MC4_PSQ Julio 1 a 15 2025.xlsx": "1Iy1KmeZcS1ngZCx5IFm4qJcEhcm6NhML",
    "MC4_PSQ Julio 16 a 31 2025.xlsx": "1XnFt4cAxG7qq7yqaRj8inEqMmEwXAboX",
    "MC4_PSQ Agosto 1 a 15 2025.xlsx": "1_4fVKUHJBtZMtYW_jgJ_CyTC2ZqEwnCU",
    "MC4_PSQ Agosto 16 a 31 2025.xlsx": "10YHfG-UG1-XW34HbAuNOB-hOd0Zt2ICf",
    "MC4_PSQ Septiembre 1 a 15 2025.xlsx": "1IgVWSRKKUC7XQPVbN2u_beTJiLVlYDxI",
    "MC4_PSQ Septiembre 16 a 30 2025.xlsx": "1ZE4h760SDeNSK3UK6gREqWImWCWnzXwb",
    "MC4_PSQ Octubre 1 a 15 2025.xlsx": "1rnFKHgKGsWTwRDdWURXobGpxT1QELhfD",
    "MC4_PSQ Octubre 16 a 31 2025.xlsx": "1dV7t8JT0hjbqSIdiQZk7dgnHeSheePcq",
    "MC4_PSQ Noviembre 1 a 15 2025.xlsx": "1htmDtrDhfQW3Mo9a69fijmG9KwD87Hxq",
    "MC4_PSQ Noviembre 16 a 30 2025.xlsx": "1C233hNEA-Wb1MhcelI1KgCAf_o4lzYOL",
    "MC4_PSQ Diciembre 1 a 15 2025.xlsx": "14gaxV_PPXt9EDIsGJbMT-ylskA654EK7",
    "MC4_PSQ Diciembre 16 a 31 2025.xlsx": "1Mdjs04yilHoJGN3ZS72Xt2oU8z1P047d",
}

# Skinpass (Pesquería): 12 archivos mensuales, 2025
ARCHIVOS_SKP = {
    "SKP_PSQ Enero 2025.xlsx": "1LgWmmlaXU6bHxffk0GQFq5q0xvfquXHn",
    "SKP_PSQ Febrero 2025.xlsx": "1txO7e_C2XiRWAc_UuHL7SZdb9gMCrq0w",
    "SKP_PSQ Marzo 2025.xlsx": "16ewq8uf2FBErYErTsvFBPPM75xVv4Iy1",
    "SKP_PSQ Abril 2025.xlsx": "1gnXdlK-42Mc4-tjRyvvcTAQLSe-c8D3Z",
    "SKP_PSQ Mayo 2025.xlsx": "121pTamD_mz41oX-zuxIOj3ig-5JPzNsL",
    "SKP_PSQ Junio 2025.xlsx": "1Yywe1MJlNyn-2UurOx1dRLzh-o5rM4Lm",
    "SKP_PSQ Julio 2025.xlsx": "1ri6KPG7OVAAii-c3FauzihTEFUFsgO2q",
    "SKP_PSQ Agosto 2025.xlsx": "1VOFIPbrManrdAuGp_XxM6MyEni3xPi2S",
    "SKP_PSQ Septiembre 2025.xlsx": "1_ckeAGW94_TBWf5eh8RTO-CrRLesvFF7",
    "SKP_PSQ Octubre 2025.xlsx": "1pwvcWxDzvfHa0zHP7Gy0JFvHRpwYs03h",
    "SKP_PSQ Noviembre 2025.xlsx": "1OyyfC5aE0xcXcB4C3TPbnNIMhFWDplIK",
    "SKP_PSQ Diciembre 2025.xlsx": "18d8LYRtx5f1gTpnYpiDfU97j30gdkM4N",
}

URL = "https://drive.usercontent.google.com/download?id={id}&export=download&confirm=t"


def bajar(nombre, file_id, forzar=False):
    carpeta = DESTINO[nombre.split("_")[0]]
    carpeta.mkdir(parents=True, exist_ok=True)
    ruta = carpeta / nombre
    if ruta.exists() and ruta.stat().st_size > 100_000 and not forzar:
        return f"[ya existe] {nombre}"
    for intento in range(3):
        try:
            with urllib.request.urlopen(URL.format(id=file_id), timeout=120) as r:
                datos = r.read()
            if not datos.startswith(b"PK"):  # un .xlsx es un zip
                raise ValueError("Drive no devolvió un Excel (¿permisos o cuota?)")
            ruta.write_bytes(datos)
            return f"[ok] {nombre} ({len(datos)/1e6:.1f} MB)"
        except Exception as e:
            error = e
            time.sleep(2 * (intento + 1))
    return f"[FALLÓ] {nombre}: {error}"


def main():
    forzar = "--forzar" in sys.argv
    todos = {**ARCHIVOS_MC4, **ARCHIVOS_SKP}
    with ThreadPoolExecutor(max_workers=6) as ex:
        for linea in ex.map(lambda kv: bajar(*kv, forzar=forzar), todos.items()):
            print(linea)
    faltan = [n for n in todos if not (DESTINO[n.split("_")[0]] / n).exists()]
    print(f"\n{len(todos) - len(faltan)} de {len(todos)} archivos en data/raw/")
    if faltan:
        sys.exit(1)


if __name__ == "__main__":
    main()
