# 📊 Análisis de Sentimiento para las Acciones del Dow Jones

## 📖 Descripción
Proyecto de análisis de sentimiento aplicado a noticias relacionadas con acciones del Dow Jones. El proyecto implementa un pipeline completo de ETL (Extracción, Transformación y Carga) y EDA (Análisis Exploratorio de Datos) para procesar y analizar datos de sentimiento del mercado de valores.

## 🎯 Objetivos
- ✅ Extraer datos de archivos CSV con noticias y sentimientos
- ✅ Limpiar y transformar datos (fechas, duplicados, nulos, tipos de datos)
- ✅ Cargar datos limpios en múltiples formatos (CSV, Parquet, SQLite)
- ✅ Generar visualizaciones de análisis exploratorio (mínimo 5 gráficas)
- ✅ Identificar patrones temporales y distribuciones de sentimiento

## 📁 Estructura del Proyecto
```
Parcial2BigData/
├── data/                           # Datos del proyecto
│   ├── stock_sentiment_clean.csv   # Datos limpios en CSV
│   ├── stock_sentiment_clean.parquet # Datos limpios en Parquet
│   └── stock_sentiment.db          # Base de datos SQLite
├── notebooks/                      # Jupyter notebooks para análisis
├── src/                           # Código fuente
│   ├── __init__.py               # Inicialización del paquete
│   ├── etl.py                    # Módulo de ETL
│   └── eda.py                    # Módulo de EDA
├── visualizations/                # Gráficas generadas
│   ├── 01_sentiment_distribution.png
│   ├── 02_temporal_trend.png
│   ├── 03_yearly_sentiment.png
│   ├── 04_weekday_pattern.png
│   ├── 05_news_count_distribution.png
│   └── 06_quarterly_heatmap.png
├── main.py                        # Script principal del pipeline
├── stock_senti_analysis.csv      # Datos originales
├── requirements.txt              # Dependencias del proyecto
├── .gitignore                    # Archivos ignorados por Git
└── README.md                     # Este archivo
```

## 🚀 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación
```bash
# 1. Clonar el repositorio
git clone https://github.com/SeanOsorio/An-lisis-de-Sentimiento-para-las-Acciones-del-Dow-Jones.git
cd An-lisis-de-Sentimiento-para-las-Acciones-del-Dow-Jones

# 2. Crear entorno virtual (recomendado)
python -m venv venv
.\venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt
```

## 💻 Uso

### Ejecutar el Pipeline Completo
Para ejecutar todo el proceso de ETL y EDA de una sola vez:
```bash
python main.py
```

### Ejecutar Módulos Individuales

**Solo ETL:**
```bash
python src/etl.py
```

**Solo EDA:**
```bash
python src/eda.py
```

### Uso Programático
```python
from src.etl import StockSentimentETL
from src.eda import StockSentimentEDA

# ETL
etl = StockSentimentETL('stock_senti_analysis.csv')
etl.extract()
etl.transform()
etl.load_csv()
etl.load_parquet()
etl.load_sqlite()

# EDA
eda = StockSentimentEDA()
eda.load_data()
eda.generate_all_plots()
eda.generate_summary_report()
```

## 📊 Análisis Realizados

### Proceso ETL
1. **Extracción**: Lectura de datos desde CSV
2. **Transformación**:
   - Conversión de fechas a formato datetime
   - Eliminación de duplicados
   - Manejo de valores nulos
   - Normalización de tipos de datos
   - Creación de características adicionales (año, mes, día de semana, trimestre)
3. **Carga**: Exportación a CSV, Parquet y SQLite

### Visualizaciones EDA
1. **Distribución de Sentimientos**: Gráfica de barras y pastel mostrando la proporción de sentimientos positivos y negativos
2. **Tendencia Temporal**: Evolución mensual de sentimientos a lo largo del tiempo
3. **Sentimientos por Año**: Comparación de sentimientos entre diferentes años
4. **Patrón Semanal**: Análisis de sentimientos por día de la semana
5. **Distribución de Noticias**: Análisis estadístico del número de noticias por día
6. **Mapa de Calor Trimestral**: Visualización de sentimientos promedio por trimestre (BONUS)

## 📦 Dependencias Principales
- **pandas**: Manipulación y análisis de datos
- **numpy**: Computación numérica
- **matplotlib**: Visualizaciones básicas
- **seaborn**: Visualizaciones estadísticas avanzadas
- **pyarrow**: Soporte para formato Parquet
- **wordcloud**: Generación de nubes de palabras (opcional)

## 📈 Resultados
Los resultados del análisis incluyen:
- Dataset limpio con más de 6,000 registros procesados
- 6 visualizaciones de alta calidad guardadas en formato PNG
- Base de datos SQLite para consultas SQL
- Archivos optimizados en formato Parquet
- Reporte estadístico completo

## Flujo de Trabajo Git
Este proyecto sigue Git Flow:
- `main`: Rama de producción
- `development`: Rama de desarrollo
- `feature/*`: Ramas de características
- `release/*`: Ramas de release
- `hotfix/*`: Ramas de correcciones urgentes

## Contribuciones
Por favor, crea una rama feature antes de hacer cambios.

## Licencia
Pendiente...
