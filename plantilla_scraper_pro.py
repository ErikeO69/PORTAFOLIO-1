import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def ejecutar_scraper(url_objetivo, archivo_salida="resultados.xlsx"):
    print(f"🚀 Iniciando extracción desde: {url_objetivo}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        respuesta = requests.get(url_objetivo, headers=headers)
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            
            # --- CONFIGURACIÓN DE BÚSQUEDA (El cliente edita aquí las etiquetas) ---
            # Ejemplo para extrae títulos/enlaces de listados generales
            elementos = soup.find_all(['h2', 'h3', 'a'], class_=True) 
            
            datos = []
            for i, elem in enumerate(elementos[:30], 1):
                texto = elem.text.strip()
                enlace = elem.get('href', 'N/A')
                if texto:
                    datos.append({"ID": i, "Texto/Título": texto, "Enlace": enlace})
            
            # Guardar en Excel
            df = pd.DataFrame(datos)
            df.to_excel(archivo_salida, index=False)
            print(f"✅ ¡Éxito! Se extrajeron {len(datos)} registros y se guardaron en '{archivo_salida}'.")
        else:
            print(f"❌ Error al conectar con la web. Código: {respuesta.status_code}")
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

if __name__ == "__main__":
    print("--- PLANTILLA AUTOMATIZADA DE EXTRACCIÓN DE DATOS ---")
    url = input("Ingresa la URL objetivo a extraer: ")
    ejecutar_scraper(url)