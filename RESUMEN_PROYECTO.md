# 📋 RESUMEN DEL PROYECTO
## Análisis de Sentimiento para las Acciones del Dow Jones

### 🎯 Información General
- **Autor**: Sean Osorio
- **Repositorio**: https://github.com/SeanOsorio/An-lisis-de-Sentimiento-para-las-Acciones-del-Dow-Jones
- **Fecha de creación**: Octubre 2025
- **Versión**: 1.0.0

---

## ✅ OBJETIVOS CUMPLIDOS

### 1. ✅ Extracción de Datos (Extract)
- **Archivo de entrada**: `stock_senti_analysis.csv`
- **Registros totales**: 4,101 filas
- **Columnas**: 27 columnas (Date, Label, Top1-Top25)
- **Período**: Enero 2000 - Julio 2016 (16.5 años)
- **Codificación**: Soporte múltiple (UTF-8, Latin-1, ISO-8859-1, CP1252)

### 2. ✅ Transformación y Limpieza (Transform)
**Procesos realizados:**
- ✅ **Conversión de fechas**: Formato datetime estándar
- ✅ **Eliminación de duplicados**: 0 duplicados encontrados
- ✅ **Manejo de valores nulos**: 
  - 7 valores nulos detectados
  - Todos los nulos procesados correctamente
  - Fechas nulas eliminadas
  - Columnas Top* rellenadas con string vacío
- ✅ **Ajuste de tipos de datos**:
  - Date: datetime64
  - Label: int64
  - Top1-Top25: string
- ✅ **Normalizaciones básicas**:
  - Ordenamiento por fecha
  - Creación de características temporales: Year, Month, DayOfWeek, Quarter
  - Conteo de noticias por día (News_Count)

### 3. ✅ Carga de Datos (Load)
**Formatos generados:**

#### 📄 CSV
- **Archivo**: `data/stock_sentiment_clean.csv`
- **Tamaño**: ~6,086 líneas
- **Uso**: Análisis en herramientas de hoja de cálculo

#### 📦 Parquet
- **Archivo**: `data/stock_sentiment_clean.parquet`
- **Tamaño**: ~5.6 MB (comprimido)
- **Uso**: Análisis de Big Data, Spark, pandas

#### 🗄️ SQLite
- **Archivo**: `data/stock_sentiment.db`
- **Tabla**: `stock_sentiment`
- **Registros**: 4,101
- **Tamaño**: ~10 MB
- **Uso**: Consultas SQL, aplicaciones

### 4. ✅ Análisis Exploratorio de Datos (EDA)
**6 Visualizaciones generadas:**

#### 📊 Gráfica 1: Distribución de Sentimientos
- **Archivo**: `01_sentiment_distribution.png`
- **Tipo**: Barras + Pastel
- **Insights**:
  - 52.82% Sentimiento Positivo (2,166 días)
  - 47.18% Sentimiento Negativo (1,935 días)
  - Balance casi equitativo entre sentimientos

#### 📈 Gráfica 2: Tendencia Temporal
- **Archivo**: `02_temporal_trend.png`
- **Tipo**: Línea temporal mensual
- **Insights**:
  - Variación mensual de sentimientos
  - Períodos de alta volatilidad visible
  - Tendencias a largo plazo identificadas

#### 📊 Gráfica 3: Sentimientos por Año
- **Archivo**: `03_yearly_sentiment.png`
- **Tipo**: Barras agrupadas
- **Insights**:
  - Distribución anual de 2000 a 2016
  - Años con mayor positividad/negatividad
  - Promedio: ~247 días por año

#### 🗓️ Gráfica 4: Patrón Semanal
- **Archivo**: `04_weekday_pattern.png`
- **Tipo**: Barras apiladas + Proporción
- **Insights**:
  - Distribución por día de semana (solo días hábiles)
  - Miércoles con mayor número de registros (843 días)
  - Sin datos de fines de semana (mercado cerrado)

#### 📰 Gráfica 5: Distribución de Noticias
- **Archivo**: `05_news_count_distribution.png`
- **Tipo**: Histograma + Boxplot + Tendencia + Estadísticas
- **Insights**:
  - Promedio: 25 noticias por día
  - Mediana: 25 noticias
  - Desviación estándar: 0.06 (muy consistente)
  - Rango: 22-25 noticias

#### 🔥 Gráfica 6: Mapa de Calor Trimestral (BONUS)
- **Archivo**: `06_quarterly_heatmap.png`
- **Tipo**: Heatmap
- **Insights**:
  - Sentimiento promedio por trimestre y año
  - Identificación de períodos críticos
  - Patrones estacionales visibles

---

## 🏗️ Arquitectura del Proyecto

### Módulos Principales

#### 1. `src/etl.py` - Módulo ETL
**Clase**: `StockSentimentETL`
- `extract()`: Extracción con múltiples codificaciones
- `transform()`: Limpieza y transformación completa
- `load_csv()`: Exportación a CSV
- `load_parquet()`: Exportación a Parquet
- `load_sqlite()`: Exportación a SQLite
- `get_data_summary()`: Resumen estadístico

#### 2. `src/eda.py` - Módulo EDA
**Clase**: `StockSentimentEDA`
- `load_data()`: Carga de datos limpios
- `plot_sentiment_distribution()`: Gráfica 1
- `plot_temporal_trend()`: Gráfica 2
- `plot_yearly_sentiment()`: Gráfica 3
- `plot_weekday_pattern()`: Gráfica 4
- `plot_news_count_distribution()`: Gráfica 5
- `plot_quarterly_heatmap()`: Gráfica 6
- `generate_all_plots()`: Generación completa
- `generate_summary_report()`: Reporte resumen

#### 3. `main.py` - Pipeline Principal
Ejecuta el flujo completo ETL → EDA

---

## 📊 Estadísticas del Dataset

### Distribución Temporal
```
Total de días: 4,101
Período: 2000-01-03 a 2016-07-01
Duración: 6,024 días (~16.5 años)

Por año:
  2000: 247 días    2009: 252 días
  2001: 246 días    2010: 252 días
  2002: 222 días    2011: 252 días
  2003: 248 días    2012: 250 días
  2004: 252 días    2013: 252 días
  2005: 252 días    2014: 252 días
  2006: 242 días    2015: 252 días
  2007: 251 días    2016: 126 días
  2008: 253 días
```

### Distribución de Sentimientos
```
Positivo (1): 2,166 días (52.82%)
Negativo (0): 1,935 días (47.18%)

Balance: Casi equitativo con ligera tendencia positiva
```

### Patrón Semanal
```
Lunes:      773 días (18.85%)
Martes:     841 días (20.51%)
Miércoles:  843 días (20.56%)
Jueves:     824 días (20.09%)
Viernes:    820 días (19.99%)

Total días hábiles: 4,101 (solo lunes-viernes)
```

---

## 🔄 Flujo de Trabajo Git

### Ramas del Proyecto
```
master (main)           ← Producción
  └── development       ← Desarrollo
        └── feature/etl-eda  ← Feature completada
```

### Commits Realizados
1. **Initial commit**: Configuración inicial del proyecto
2. **feat: Implementar pipeline completo de ETL y EDA**: Feature completa
3. **Merge feature/etl-eda into development**: Integración

### Estado Actual
- ✅ `master`: Commit inicial
- ✅ `development`: Con feature ETL+EDA integrada
- ✅ `feature/etl-eda`: Feature completada y mergeada
- ✅ Todas las ramas sincronizadas con GitHub

---

## 🛠️ Tecnologías Utilizadas

### Lenguaje
- Python 3.11.9

### Librerías Principales
| Librería | Versión | Propósito |
|----------|---------|-----------|
| pandas | 2.1.4 | Manipulación de datos |
| numpy | 1.26.2 | Operaciones numéricas |
| matplotlib | 3.8.2 | Visualizaciones base |
| seaborn | 0.13.0 | Visualizaciones estadísticas |
| pyarrow | 14.0.1 | Formato Parquet |
| wordcloud | 1.9.3 | Nubes de palabras |

### Herramientas
- Git / GitHub (Control de versiones)
- VS Code (Editor)
- SQLite (Base de datos)

---

## 📁 Estructura de Archivos Generados

```
├── data/
│   ├── stock_sentiment_clean.csv         (6,086 líneas)
│   ├── stock_sentiment_clean.parquet     (5.6 MB)
│   └── stock_sentiment.db                (10 MB)
│
└── visualizations/
    ├── 01_sentiment_distribution.png     (181 KB)
    ├── 02_temporal_trend.png             (636 KB)
    ├── 03_yearly_sentiment.png           (149 KB)
    ├── 04_weekday_pattern.png            (259 KB)
    ├── 05_news_count_distribution.png    (371 KB)
    └── 06_quarterly_heatmap.png          (362 KB)
```

**Total de archivos generados**: 9 archivos
**Peso total aproximado**: ~17 MB

---

## 🚀 Cómo Ejecutar

### Instalación
```bash
git clone https://github.com/SeanOsorio/An-lisis-de-Sentimiento-para-las-Acciones-del-Dow-Jones.git
cd An-lisis-de-Sentimiento-para-las-Acciones-del-Dow-Jones
pip install -r requirements.txt
```

### Ejecución Completa
```bash
python main.py
```

### Ejecución por Módulos
```bash
# Solo ETL
python src/etl.py

# Solo EDA
python src/eda.py
```

---

## 🎯 Cumplimiento de Requisitos

| Requisito | Estado | Detalle |
|-----------|--------|---------|
| ✅ Extraer archivos CSV | ✅ Completado | `stock_senti_analysis.csv` |
| ✅ Transformar/Limpiar datos | ✅ Completado | Fechas, duplicados, nulos, tipos |
| ✅ Cargar dataset limpio | ✅ Completado | CSV, Parquet, SQLite |
| ✅ Generar 5+ gráficas EDA | ✅ Completado | 6 gráficas generadas |
| ✅ Usar Git Flow | ✅ Completado | master, development, feature |
| ✅ Subir a GitHub | ✅ Completado | Todas las ramas sincronizadas |

---

## 📈 Conclusiones

### Hallazgos Principales
1. **Balance de Sentimientos**: El mercado mostró un balance casi equitativo entre días positivos (52.82%) y negativos (47.18%)
2. **Consistencia de Datos**: Muy baja variación en el número de noticias por día (desv. est: 0.06)
3. **Cobertura Temporal**: 16.5 años de datos proporcionan una vista histórica robusta
4. **Patrones Semanales**: Distribución uniforme entre días hábiles, sin sesgo por día de semana

### Calidad del Proyecto
- ✅ Código modular y reutilizable
- ✅ Documentación completa
- ✅ Manejo robusto de errores
- ✅ Múltiples formatos de salida
- ✅ Visualizaciones profesionales
- ✅ Git Flow implementado correctamente

---

## 🔮 Próximos Pasos Sugeridos
1. Crear rama `release/v1.0.0` para preparar release
2. Mergear a `master` cuando esté listo para producción
3. Crear tag `v1.0.0`
4. Implementar análisis de texto sobre las columnas Top1-Top25
5. Agregar modelos de Machine Learning para predicción
6. Crear dashboard interactivo con Plotly/Dash

---

**Proyecto completado exitosamente el 14 de octubre de 2025** 🎉
