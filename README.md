# SD-Crawler

## Descripción
Este proyecto es un web crawler especializado para extraer y analizar noticias del portal de la Universidad Manuela Beltrán (UMB). El sistema está compuesto por dos componentes principales:

### 1. Crawler de Noticias (`umbnews.py`)
Este componente se encarga de:
- Extraer noticias del portal web de la UMB
- Procesar el contenido HTML
- Almacenar la información en formato estructurado
- Gestionar la paginación y navegación del sitio
- Manejar errores y excepciones durante el proceso de extracción

### 2. Analizador de Noticias (`umbnews_analysis.py`)
Este componente realiza:
- Procesamiento de lenguaje natural (NLP) de las noticias extraídas
- Análisis de sentimientos
- Extracción de palabras clave
- Identificación de temas principales
- Generación de insights sobre el contenido

## Requisitos
- Python 3.x
- Bibliotecas requeridas:
  - requests
  - beautifulsoup4
  - spacy (pendiente de instalación)
  - pandas

## Instalación
1. Clonar el repositorio
2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso
1. Para extraer noticias:
```bash
python umbnews.py
```

2. Para analizar las noticias:
```bash
python umbnews_analysis.py
```

## Estructura del Proyecto
```
SD-Crawler/
├── umbnews.py         # Crawler principal
├── umbnews_analysis.py # Análisis de noticias
├── README.md          # Documentación
└── requirements.txt   # Dependencias
```

## Detalles Técnicos

### Crawler (`umbnews.py`)
#### Funcionamiento
1. **Inicialización**
   - Configuración de headers HTTP para simular navegador
   - Gestión de sesiones para mantener cookies y estado

2. **Proceso de Extracción**
   - Método: Scraping HTML usando BeautifulSoup4
   - URLs objetivo: Portal de noticias UMB
   - Paginación: Manejo automático de navegación entre páginas
   - Rate limiting: Delays entre requests para evitar sobrecarga

3. **Procesamiento de Datos**
   - Extracción de elementos clave:
     * Título de la noticia
     * Fecha de publicación
     * Contenido principal
     * Imágenes asociadas
     * Categorías/tags
   - Limpieza de texto HTML
   - Normalización de fechas y contenido

4. **Manejo de Errores**
   - Retry automático en caso de fallos de conexión
   - Logging de errores y excepciones
   - Validación de datos extraídos

### Analizador (`umbnews_analysis.py`)
#### Componentes NLP
1. **Preprocesamiento**
   - Tokenización de texto
   - Eliminación de stopwords
   - Normalización de caracteres
   - Lematización

2. **Análisis de Sentimientos**
   - Uso de modelo spaCy para español
   - Clasificación de polaridad (positivo/negativo/neutral)
   - Detección de subjetividad

3. **Extracción de Información**
   - Reconocimiento de entidades nombradas (NER)
   - Identificación de temas principales
   - Análisis de frecuencia de términos
   - Extracción de palabras clave

4. **Generación de Insights**
   - Estadísticas de publicación
   - Tendencias temáticas
   - Análisis temporal de contenidos

### Almacenamiento de Datos
- Formato: JSON estructurado
- Estructura de archivos:
  ```
  /data/
  ├── raw/              # Datos crudos extraídos
  ├── processed/        # Datos procesados y limpios
  └── analysis/         # Resultados de análisis
  ```

### Optimizaciones
- Caché de requests para reducir llamadas repetidas
- Procesamiento asíncrono para mejora de rendimiento
- Compresión de datos para almacenamiento eficiente
- Índices para búsqueda rápida

## Contribución
Este proyecto es parte de un trabajo académico para la Universidad Manuela Beltrán.