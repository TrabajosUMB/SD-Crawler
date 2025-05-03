import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL de las noticias de la UMB
url = "https://umb.edu.co/noticias/"

# Headers para simular un navegador web
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

# Obtener contenido HTML
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Inicializar listas para almacenar los datos
titulos = []
imagenes = []
links = []

# Buscar todas las noticias
for noticia in soup.find_all("article", class_="fusion-post-grid"):
    # Obtener título
    titulo_elem = noticia.find("h2", class_="blog-shortcode-post-title")
    if titulo_elem and titulo_elem.find("a"):
        titulo = titulo_elem.find("a").text.strip()
    else:
        titulo = "Sin título"
    
    """
    Proceso para obtener la URL de la imagen:
    1. Primero buscamos el contenedor de la imagen: div con clase 'fusion-flexslider'
    2. Dentro de ese contenedor, buscamos la etiqueta <img>
    3. La imagen puede estar en diferentes atributos debido al lazy loading:
       - data-lazy-src: URL usada por el lazy loading de WordPress
       - data-src: Alternativa común para lazy loading
       - data-orig-src: URL original de la imagen
       - srcset: Lista de URLs para diferentes tamaños (tomamos la primera)
       - src: URL directa de la imagen
    4. Probamos cada atributo en orden hasta encontrar uno que tenga la URL
    5. Si ningún atributo tiene la URL, devolvemos "Sin imagen"
    """
    img_container = noticia.find("div", class_="fusion-flexslider")
    if img_container:
        img_elem = img_container.find("img")
        if img_elem:
            # Intentar diferentes atributos para la URL de la imagen
            imagen = (
                img_elem.get("data-lazy-src") or
                img_elem.get("data-src") or
                img_elem.get("data-orig-src") or
                img_elem.get("srcset", "").split(" ")[0] or
                img_elem.get("src") or
                "Sin imagen"
            )
        else:
            imagen = "Sin imagen"
    else:
        imagen = "Sin imagen"
    
    # Obtener link de leer más
    link_elem = noticia.find("a", class_="fusion-read-more")
    if link_elem:
        link = link_elem.get("href")
    else:
        link = "Sin link"
    
    titulos.append(titulo)
    imagenes.append(imagen)
    links.append(link)
    
    print("\nNoticia encontrada:")
    print("Título:", titulo)
    print("Imagen URL:", imagen)
    print("Leer más URL:", link)
    print("---")

# Crear un DataFrame
df = pd.DataFrame({
    "Título": titulos,
    "Imagen": imagenes,
    "Leer más": links
})

# Guardar el DataFrame en un archivo Excel
try:
    nombre_archivo = "noticias_umb.xlsx"
    # Si el archivo existe, intentar eliminarlo primero
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
    df.to_excel(nombre_archivo, index=False)
    print(f"\nSe han guardado {len(titulos)} noticias en el archivo '{nombre_archivo}'")
    print("\nPrimeras 3 noticias:")
    print(df.head(3))
except PermissionError:
    print(f"\nError: No se pudo guardar el archivo '{nombre_archivo}'. Asegúrate de que no esté abierto en Excel.")
    print("\nMostrando los datos en consola:")
    print(df)
except Exception as e:
    print(f"\nError al guardar el archivo: {str(e)}")
    print("\nMostrando los datos en consola:")
    print(df)

exit()
