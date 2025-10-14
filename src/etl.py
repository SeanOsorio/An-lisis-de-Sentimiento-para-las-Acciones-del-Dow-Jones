"""
ETL Module for Stock Sentiment Analysis
Extrae, Transforma y Carga datos del análisis de sentimiento de acciones del Dow Jones
"""

import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime
import os


class StockSentimentETL:
    """
    Clase para realizar el proceso ETL sobre los datos de sentimiento de acciones
    """
    
    def __init__(self, input_file):
        """
        Inicializa el ETL con el archivo de entrada
        
        Args:
            input_file (str): Ruta del archivo CSV de entrada
        """
        self.input_file = input_file
        self.df = None
        self.df_clean = None
        
    def extract(self):
        """
        Extrae los datos del archivo CSV
        
        Returns:
            pd.DataFrame: DataFrame con los datos extraídos
        """
        print(f"📥 Extrayendo datos de: {self.input_file}")
        try:
            # Intentar con diferentes codificaciones
            encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
            for encoding in encodings:
                try:
                    self.df = pd.read_csv(self.input_file, encoding=encoding)
                    print(f"✅ Datos extraídos exitosamente con codificación '{encoding}'")
                    print(f"   {self.df.shape[0]} filas, {self.df.shape[1]} columnas")
                    return self.df
                except UnicodeDecodeError:
                    continue
            
            # Si ninguna codificación funciona, usar errors='ignore'
            self.df = pd.read_csv(self.input_file, encoding='latin-1', errors='ignore')
            print(f"✅ Datos extraídos con codificación alternativa")
            print(f"   {self.df.shape[0]} filas, {self.df.shape[1]} columnas")
            return self.df
        except Exception as e:
            print(f"❌ Error al extraer datos: {str(e)}")
            raise
    
    def transform(self):
        """
        Transforma y limpia los datos
        
        Returns:
            pd.DataFrame: DataFrame limpio y transformado
        """
        print("\n🔄 Iniciando transformación de datos...")
        
        if self.df is None:
            raise ValueError("Primero debe ejecutar extract()")
        
        # Crear copia para transformación
        self.df_clean = self.df.copy()
        
        # 1. Convertir fechas
        print("  📅 Convirtiendo fechas...")
        self.df_clean['Date'] = pd.to_datetime(self.df_clean['Date'], errors='coerce')
        
        # 2. Eliminar duplicados
        print("  🔍 Eliminando duplicados...")
        duplicados_antes = self.df_clean.shape[0]
        self.df_clean = self.df_clean.drop_duplicates()
        duplicados_eliminados = duplicados_antes - self.df_clean.shape[0]
        print(f"    - Duplicados eliminados: {duplicados_eliminados}")
        
        # 3. Manejo de valores nulos
        print("  🧹 Manejando valores nulos...")
        nulos_antes = self.df_clean.isnull().sum().sum()
        
        # Eliminar filas donde la fecha es nula
        self.df_clean = self.df_clean.dropna(subset=['Date'])
        
        # Para las columnas Top1-Top25, rellenar con string vacío
        top_cols = [f'Top{i}' for i in range(1, 26)]
        for col in top_cols:
            if col in self.df_clean.columns:
                self.df_clean[col] = self.df_clean[col].fillna('')
        
        nulos_despues = self.df_clean.isnull().sum().sum()
        print(f"    - Valores nulos antes: {nulos_antes}")
        print(f"    - Valores nulos después: {nulos_despues}")
        
        # 4. Verificar y ajustar tipos de datos
        print("  🔧 Ajustando tipos de datos...")
        self.df_clean['Label'] = self.df_clean['Label'].astype(int)
        
        # 5. Normalizaciones básicas
        print("  ✨ Aplicando normalizaciones...")
        # Ordenar por fecha
        self.df_clean = self.df_clean.sort_values('Date').reset_index(drop=True)
        
        # Crear características adicionales
        self.df_clean['Year'] = self.df_clean['Date'].dt.year
        self.df_clean['Month'] = self.df_clean['Date'].dt.month
        self.df_clean['DayOfWeek'] = self.df_clean['Date'].dt.dayofweek
        self.df_clean['Quarter'] = self.df_clean['Date'].dt.quarter
        
        # Contar noticias por día
        self.df_clean['News_Count'] = self.df_clean[top_cols].apply(
            lambda row: sum(1 for val in row if val != ''), axis=1
        )
        
        print(f"\n✅ Transformación completada: {self.df_clean.shape[0]} filas limpias")
        print(f"\n📊 Resumen de datos limpios:")
        print(f"  - Rango de fechas: {self.df_clean['Date'].min()} a {self.df_clean['Date'].max()}")
        print(f"  - Etiquetas únicas: {self.df_clean['Label'].unique()}")
        print(f"  - Distribución de etiquetas:")
        print(f"    {self.df_clean['Label'].value_counts().to_dict()}")
        
        return self.df_clean
    
    def load_csv(self, output_path='data/stock_sentiment_clean.csv'):
        """
        Carga el dataset limpio en formato CSV
        
        Args:
            output_path (str): Ruta del archivo de salida
        """
        if self.df_clean is None:
            raise ValueError("Primero debe ejecutar transform()")
        
        print(f"\n💾 Guardando datos limpios en CSV: {output_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df_clean.to_csv(output_path, index=False)
        print(f"✅ Archivo CSV guardado exitosamente")
    
    def load_parquet(self, output_path='data/stock_sentiment_clean.parquet'):
        """
        Carga el dataset limpio en formato Parquet
        
        Args:
            output_path (str): Ruta del archivo de salida
        """
        if self.df_clean is None:
            raise ValueError("Primero debe ejecutar transform()")
        
        print(f"\n💾 Guardando datos limpios en Parquet: {output_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df_clean.to_parquet(output_path, index=False, engine='pyarrow')
        print(f"✅ Archivo Parquet guardado exitosamente")
    
    def load_sqlite(self, db_path='data/stock_sentiment.db', table_name='stock_sentiment'):
        """
        Carga el dataset limpio en una tabla SQLite
        
        Args:
            db_path (str): Ruta de la base de datos SQLite
            table_name (str): Nombre de la tabla
        """
        if self.df_clean is None:
            raise ValueError("Primero debe ejecutar transform()")
        
        print(f"\n💾 Guardando datos limpios en SQLite: {db_path}")
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Conectar a la base de datos
        conn = sqlite3.connect(db_path)
        
        # Guardar el DataFrame en la tabla
        self.df_clean.to_sql(table_name, conn, if_exists='replace', index=False)
        
        # Verificar
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        
        print(f"✅ Datos guardados en SQLite: {count} registros en tabla '{table_name}'")
        
        conn.close()
    
    def get_data_summary(self):
        """
        Obtiene un resumen estadístico de los datos limpios
        
        Returns:
            dict: Diccionario con estadísticas
        """
        if self.df_clean is None:
            raise ValueError("Primero debe ejecutar transform()")
        
        summary = {
            'total_rows': len(self.df_clean),
            'total_columns': len(self.df_clean.columns),
            'date_range': {
                'start': str(self.df_clean['Date'].min()),
                'end': str(self.df_clean['Date'].max()),
                'days': (self.df_clean['Date'].max() - self.df_clean['Date'].min()).days
            },
            'label_distribution': self.df_clean['Label'].value_counts().to_dict(),
            'missing_values': self.df_clean.isnull().sum().to_dict(),
            'data_types': self.df_clean.dtypes.astype(str).to_dict()
        }
        
        return summary


def main():
    """
    Función principal para ejecutar el ETL
    """
    print("=" * 80)
    print("🚀 STOCK SENTIMENT ANALYSIS - ETL PIPELINE")
    print("=" * 80)
    
    # Inicializar ETL
    etl = StockSentimentETL('stock_senti_analysis.csv')
    
    # Ejecutar pipeline
    etl.extract()
    etl.transform()
    
    # Cargar en múltiples formatos
    etl.load_csv()
    etl.load_parquet()
    etl.load_sqlite()
    
    # Mostrar resumen
    print("\n" + "=" * 80)
    print("📊 RESUMEN FINAL DEL ETL")
    print("=" * 80)
    summary = etl.get_data_summary()
    print(f"\nTotal de registros: {summary['total_rows']}")
    print(f"Total de columnas: {summary['total_columns']}")
    print(f"\nRango de fechas:")
    print(f"  - Inicio: {summary['date_range']['start']}")
    print(f"  - Fin: {summary['date_range']['end']}")
    print(f"  - Días totales: {summary['date_range']['days']}")
    print(f"\nDistribución de etiquetas:")
    for label, count in summary['label_distribution'].items():
        print(f"  - Label {label}: {count} ({count/summary['total_rows']*100:.2f}%)")
    
    print("\n" + "=" * 80)
    print("✅ ETL COMPLETADO EXITOSAMENTE")
    print("=" * 80)


if __name__ == "__main__":
    main()
