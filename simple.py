import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL Objetivo
url = "https://quotes.toscrape.com/" # Pagina de prueba para scraping

# Obtener contenido HTML
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Inicializar listas para almacenar los datos
quotes = []
authors = []

# Buscar todas las citas
for quote_block in soup.find_all("div", class_="quote"):
    text = quote_block.find("span", class_="text").text
    author = quote_block.find("small", class_="author").text
    quotes.append(text)
    authors.append(author)
    print("Frase:", text)
    print("Autor:", author)
    print("---")

# Crear un DataFrame
df = pd.DataFrame({
    "Frase": quotes,
    "Autor": authors
})

# Guardar el DataFrame en un archivo Excel
nombre_archivo = "citas.xlsx"
df.to_excel(nombre_archivo, index=False)

print(f"\nSe han guardado {len(quotes)} citas en el archivo '{nombre_archivo}'")
print("\nPrimeras 3 citas:")
print(df.head(3))
exit()