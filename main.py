"""
Main Pipeline - Stock Sentiment Analysis
Pipeline completo: ETL + EDA
"""

import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from etl import StockSentimentETL
from eda import StockSentimentEDA


def main():
    """
    Ejecuta el pipeline completo de análisis
    """
    print("\n" + "=" * 100)
    print(" " * 30 + "🎯 STOCK SENTIMENT ANALYSIS PIPELINE")
    print(" " * 25 + "Análisis de Sentimiento del Dow Jones")
    print("=" * 100)
    
    # ========== FASE 1: ETL ==========
    print("\n" + "🔄 " * 40)
    print("FASE 1: EXTRACCIÓN, TRANSFORMACIÓN Y CARGA (ETL)")
    print("🔄 " * 40 + "\n")
    
    try:
        # Inicializar ETL
        etl = StockSentimentETL('stock_senti_analysis.csv')
        
        # Ejecutar pipeline ETL
        etl.extract()
        etl.transform()
        etl.load_csv()
        etl.load_parquet()
        etl.load_sqlite()
        
        # Mostrar resumen
        summary = etl.get_data_summary()
        print("\n📊 Resumen ETL:")
        print(f"  ✓ Registros procesados: {summary['total_rows']}")
        print(f"  ✓ Rango de fechas: {summary['date_range']['start']} a {summary['date_range']['end']}")
        print(f"  ✓ Formatos generados: CSV, Parquet, SQLite")
        
    except Exception as e:
        print(f"\n❌ Error en fase ETL: {str(e)}")
        return
    
    # ========== FASE 2: EDA ==========
    print("\n" + "📊 " * 40)
    print("FASE 2: ANÁLISIS EXPLORATORIO DE DATOS (EDA)")
    print("📊 " * 40 + "\n")
    
    try:
        # Inicializar EDA
        eda = StockSentimentEDA()
        
        # Cargar datos limpios
        eda.load_data()
        
        # Generar todas las visualizaciones
        eda.generate_all_plots()
        
        # Generar reporte
        eda.generate_summary_report()
        
    except Exception as e:
        print(f"\n❌ Error en fase EDA: {str(e)}")
        return
    
    # ========== FINALIZACIÓN ==========
    print("\n" + "=" * 100)
    print(" " * 40 + "✅ PIPELINE COMPLETADO")
    print("=" * 100)
    print("\n📁 Archivos generados:")
    print("  📊 Datos limpios:")
    print("     • data/stock_sentiment_clean.csv")
    print("     • data/stock_sentiment_clean.parquet")
    print("     • data/stock_sentiment.db")
    print("\n  📈 Visualizaciones:")
    print("     • visualizations/01_sentiment_distribution.png")
    print("     • visualizations/02_temporal_trend.png")
    print("     • visualizations/03_yearly_sentiment.png")
    print("     • visualizations/04_weekday_pattern.png")
    print("     • visualizations/05_news_count_distribution.png")
    print("     • visualizations/06_quarterly_heatmap.png")
    print("\n" + "=" * 100)
    print("🎉 ¡Análisis completado exitosamente!")
    print("=" * 100 + "\n")


if __name__ == "__main__":
    main()
