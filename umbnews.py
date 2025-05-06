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
parrafos = []  # Lista para almacenar los párrafos de cada noticia

# Buscar todas las noticias
for noticia in soup.find_all("article", class_="fusion-post-grid"):
    # Obtener título
    titulo_elem = noticia.find("h2", class_="blog-shortcode-post-title")
    if titulo_elem and titulo_elem.find("a"):
        titulo = titulo_elem.find("a").text.strip()
        link = titulo_elem.find("a")['href']  # Obtener el enlace directamente del título
    else:
        titulo = "Sin título"
        link = "Sin link"

    # Obtener imagen
    img_container = noticia.find("div", class_="fusion-flexslider")
    if img_container:
        img_elem = img_container.find("img")
        if img_elem:
            # Intentar diferentes atributos para la URL de la imagen
            imagen = (
                img_elem.get("data-lazy-src") or
                img_elem.get("data-src") or
                img_elem.get("data-orig-src") or
                img_elem.get("src", "Sin imagen")
            )
        else:
            imagen = "Sin imagen"
    else:
        imagen = "Sin imagen"

    # Obtener el contenido completo de la noticia
    contenido_parrafos = []
    if link != "Sin link":
        try:
            # Visitar la página individual de la noticia
            response_noticia = requests.get(link, headers=headers)
            soup_noticia = BeautifulSoup(response_noticia.content, 'html.parser')
            
            # Buscar el contenido principal de la noticia
            contenido_elem = soup_noticia.find("div", class_="post-content")
            if contenido_elem:
                # Obtener todos los párrafos del contenido
                for p in contenido_elem.find_all("p"):
                    texto = p.text.strip()
                    # Excluir metadatos y párrafos vacíos
                    if texto and not any(texto.startswith(x) for x in ["Web Master", "By", "|"]):
                        contenido_parrafos.append(texto)
        except Exception as e:
            print(f"Error al obtener contenido de {link}: {str(e)}")
            contenido_parrafos = ["Error al obtener contenido"]
    
    # Agregar datos a las listas
    titulos.append(titulo)
    imagenes.append(imagen)
    links.append(link)
    parrafos.append(contenido_parrafos)

    # Imprimir la información encontrada
    print("\nNoticia encontrada:")
    print("Título:", titulo)
    print("Imagen URL:", imagen)
    print("URL de la noticia:", link)
    print("Contenido:")
    for i, parrafo in enumerate(contenido_parrafos, 1):
        print(f"  Párrafo {i}: {parrafo}")
    print("---")

# Crear DataFrame con los datos
df = pd.DataFrame({
    'Título': titulos,
    'Imagen': imagenes,
    'Link': links,
    'Párrafos': parrafos
})

# Guardar en Excel
df.to_excel('noticias_umb.xlsx', index=False)
print(f"\nSe han guardado {len(df)} noticias en el archivo 'noticias_umb.xlsx'")

# Guardar en archivo de texto
with open('noticias_umb.txt', 'w', encoding='utf-8') as f:
    for i, (titulo, imagen, link, contenido) in enumerate(zip(titulos, imagenes, links, parrafos), 1):
        f.write(f"NOTICIA {i}\n")
        f.write("="*50 + "\n")
        f.write(f"TÍTULO: {titulo}\n")
        f.write(f"IMAGEN: {imagen}\n")
        f.write(f"LINK: {link}\n")
        f.write("\nCONTENIDO:\n")
        for j, parrafo in enumerate(contenido, 1):
            f.write(f"Párrafo {j}: {parrafo}\n")
        f.write("\n" + "="*50 + "\n\n")

print(f"Se ha guardado el contenido en 'noticias_umb.txt'")

# Mostrar las primeras 3 noticias
print("\nPrimeras 3 noticias:")
print(df.head(3))
