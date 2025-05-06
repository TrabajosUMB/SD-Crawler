import pandas as pd
import numpy as np  # useful for many scientific computing in Python
from PIL import Image # converting images into arrays
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

def save_to_txt(filename,umb_posts):
    with open(filename, "w", encoding="utf-8") as archivo:
        for post in umb_posts:
            titulo = post.find("h2").text.strip()
            archivo.write(titulo + "\n")

# Leer el contenido del archivo TXT y extraer solo títulos y párrafos
texto_completo = []
with open('noticias_umb.txt', 'r', encoding='utf-8') as f:
    lineas = f.readlines()
    for linea in lineas:
        linea = linea.strip()
        # Capturar títulos
        if linea.startswith("TÍTULO:"):
            titulo = linea.split(":", 1)[1].strip()
            texto_completo.append(titulo)
        # Capturar párrafos
        elif linea.startswith("Párrafo"):
            contenido = linea.split(":", 1)[1].strip()
            texto_completo.append(contenido)

# Unir todo el texto
texto = " ".join(texto_completo)

# Configurar stopwords
stopwords = set(STOPWORDS)
stopwords.update([
    # Artículos
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'lo',
    # Preposiciones
    'a', 'ante', 'bajo', 'con', 'contra', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta',
    'para', 'por', 'según', 'sin', 'sobre', 'tras', 'durante', 'mediante',
    # Conjunciones
    'y', 'e', 'ni', 'o', 'u', 'pero', 'sino', 'porque', 'pues', 'que',
    # Pronombres
    'yo', 'tú', 'él', 'ella', 'nosotros', 'vosotros', 'ellos', 'ellas', 'este', 'esta',
    'ese', 'esa', 'aquel', 'aquella', 'le', 'les', 'me', 'te', 'se',
    # Verbos comunes
    'es', 'son', 'fue', 'ser', 'estar', 'era', 'ha', 'han', 'hemos', 'tiene', 'tienen',
    # Adverbios comunes
    'más', 'menos', 'muy', 'mucho', 'poco', 'casi', 'ahora', 'antes', 'después', 'como',
    # Palabras del formato
    'NOTICIA', 'TÍTULO', 'IMAGEN', 'LINK', 'CONTENIDO', 'Párrafo',
    # Otras palabras comunes
    'si', 'no', 'al', 'del', 'donde', 'cuando', 'quien', 'cuyo', 'cuya', 'sus', 'este',
    'año', 'años', 'día', 'días', 'vez', 'veces'
])

# Crear y configurar el WordCloud
txt_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords,
    width=3200,  # Duplicamos el ancho
    height=1600,  # Duplicamos el alto
    min_font_size=8,  # Tamaño mínimo de fuente
    max_font_size=150,  # Tamaño máximo de fuente
    random_state=42,  # Para consistencia en la disposición
    prefer_horizontal=0.7,  # 70% de palabras horizontales
    font_path='C:\\Windows\\Fonts\\Arial.ttf'  # Usar una fuente clara
)

# Generar la nube de palabras
txt_wc.generate(texto)

# Mostrar y guardar la imagen
plt.figure(figsize=(32,16), dpi=300)  # Aumentamos el tamaño y DPI de la figura
plt.imshow(txt_wc, interpolation='lanczos')  # Mejor interpolación
plt.axis('off')  # Ocultar ejes
plt.title('Nube de Palabras - Noticias UMB', fontsize=40, pad=20)
plt.savefig('nube_palabras_umb.png', 
            bbox_inches='tight',
            dpi=300)  # Alta resolución
plt.close()

print("Se ha generado la nube de palabras en 'nube_palabras_umb.png'")