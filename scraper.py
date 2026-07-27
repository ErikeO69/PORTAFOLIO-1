import requests
from bs4 import BeautifulSoup

# URL de prueba (noticias/artículos)
url = "https://news.ycombinator.com/"

print("🔍 Conectando con la página...")

# Hacemos la petición HTTP a la web
respuesta = requests.get(url)

if respuesta.status_code == 200:
    print("✅ ¡Conexión exitosa! Extrayendo datos...\n")
    
    # Parseamos el HTML con BeautifulSoup
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    
    # Buscamos los elementos con la clase de los títulos
    titulos = soup.find_all('span', class_='titleline')
    
    # Mostramos los primeros 10 resultados
    for i, elemento in enumerate(titulos[:10], 1):
        enlace = elemento.find('a')
        texto_titulo = enlace.text
        url_titulo = enlace['href']
        
        print(f"[{i}] {texto_titulo}")
        print(f"    🔗 {url_titulo}\n")
        
else:
    print(f"❌ Error al conectar. Código de estado: {respuesta.status_code}")