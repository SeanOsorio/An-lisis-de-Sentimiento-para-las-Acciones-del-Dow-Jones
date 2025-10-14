"""
EDA Module for Stock Sentiment Analysis
Análisis Exploratorio de Datos con visualizaciones
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os
from datetime import datetime


class StockSentimentEDA:
    """
    Clase para realizar análisis exploratorio de datos
    """
    
    def __init__(self, data_path='data/stock_sentiment_clean.csv'):
        """
        Inicializa el EDA con los datos limpios
        
        Args:
            data_path (str): Ruta del archivo de datos limpios
        """
        self.data_path = data_path
        self.df = None
        self.output_dir = 'visualizations'
        
        # Configurar estilo de visualizaciones
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        
    def load_data(self):
        """
        Carga los datos limpios
        """
        print(f"📥 Cargando datos desde: {self.data_path}")
        self.df = pd.read_csv(self.data_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        print(f"✅ Datos cargados: {self.df.shape[0]} filas, {self.df.shape[1]} columnas")
        
        # Crear directorio de salida
        os.makedirs(self.output_dir, exist_ok=True)
        
        return self.df
    
    def plot_sentiment_distribution(self):
        """
        Gráfica 1: Distribución de sentimientos (Label)
        """
        print("\n📊 Generando gráfica 1: Distribución de sentimientos...")
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Gráfica de barras
        sentiment_counts = self.df['Label'].value_counts().sort_index()
        axes[0].bar(sentiment_counts.index, sentiment_counts.values, 
                    color=['#e74c3c', '#3498db'], alpha=0.7, edgecolor='black')
        axes[0].set_xlabel('Sentimiento (Label)', fontsize=12, fontweight='bold')
        axes[0].set_ylabel('Frecuencia', fontsize=12, fontweight='bold')
        axes[0].set_title('Distribución de Sentimientos', fontsize=14, fontweight='bold')
        axes[0].set_xticks([0, 1])
        axes[0].set_xticklabels(['Negativo (0)', 'Positivo (1)'])
        axes[0].grid(axis='y', alpha=0.3)
        
        # Añadir valores en las barras
        for i, v in enumerate(sentiment_counts.values):
            axes[0].text(i, v + 50, str(v), ha='center', va='bottom', fontweight='bold')
        
        # Gráfica de pastel
        colors = ['#e74c3c', '#3498db']
        axes[1].pie(sentiment_counts.values, labels=['Negativo (0)', 'Positivo (1)'], 
                    autopct='%1.1f%%', colors=colors, startangle=90,
                    explode=(0.05, 0.05), shadow=True)
        axes[1].set_title('Proporción de Sentimientos', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        output_file = os.path.join(self.output_dir, '01_sentiment_distribution.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"  ✅ Guardada en: {output_file}")
        plt.close()
    
    def plot_temporal_trend(self):
        """
        Gráfica 2: Tendencia temporal de sentimientos
        """
        print("\n📊 Generando gráfica 2: Tendencia temporal...")
        
        # Agrupar por fecha y sentimiento
        temporal_data = self.df.groupby([pd.Grouper(key='Date', freq='M'), 'Label']).size().unstack(fill_value=0)
        
        fig, ax = plt.subplots(figsize=(16, 6))
        
        # Plotear líneas
        temporal_data[0].plot(ax=ax, label='Negativo', color='#e74c3c', linewidth=2, marker='o', markersize=4)
        temporal_data[1].plot(ax=ax, label='Positivo', color='#3498db', linewidth=2, marker='s', markersize=4)
        
        ax.set_xlabel('Fecha', fontsize=12, fontweight='bold')
        ax.set_ylabel('Número de Noticias', fontsize=12, fontweight='bold')
        ax.set_title('Tendencia Temporal de Sentimientos por Mes', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11, loc='upper left')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        output_file = os.path.join(self.output_dir, '02_temporal_trend.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"  ✅ Guardada en: {output_file}")
        plt.close()
    
    def plot_yearly_sentiment(self):
        """
        Gráfica 3: Sentimientos por año
        """
        print("\n📊 Generando gráfica 3: Sentimientos por año...")
        
        yearly_data = self.df.groupby(['Year', 'Label']).size().unstack(fill_value=0)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        x = np.arange(len(yearly_data.index))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, yearly_data[0], width, label='Negativo', 
                       color='#e74c3c', alpha=0.8, edgecolor='black')
        bars2 = ax.bar(x + width/2, yearly_data[1], width, label='Positivo', 
                       color='#3498db', alpha=0.8, edgecolor='black')
        
        ax.set_xlabel('Año', fontsize=12, fontweight='bold')
        ax.set_ylabel('Número de Noticias', fontsize=12, fontweight='bold')
        ax.set_title('Distribución de Sentimientos por Año', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(yearly_data.index)
        ax.legend(fontsize=11)
        ax.grid(axis='y', alpha=0.3)
        
        # Añadir valores en las barras
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                if height > 0:
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}',
                           ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        output_file = os.path.join(self.output_dir, '03_yearly_sentiment.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"  ✅ Guardada en: {output_file}")
        plt.close()
    
    def plot_weekday_pattern(self):
        """
        Gráfica 4: Patrón de sentimientos por día de la semana
        """
        print("\n📊 Generando gráfica 4: Patrón por día de semana...")
        
        weekday_data = self.df.groupby(['DayOfWeek', 'Label']).size().unstack(fill_value=0)
        weekday_names = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))
        
        # Gráfica de barras apiladas
        weekday_data.plot(kind='bar', stacked=True, ax=axes[0], 
                         color=['#e74c3c', '#3498db'], alpha=0.8, edgecolor='black')
        axes[0].set_xlabel('Día de la Semana', fontsize=12, fontweight='bold')
        axes[0].set_ylabel('Número de Noticias', fontsize=12, fontweight='bold')
        axes[0].set_title('Distribución de Sentimientos por Día de la Semana (Apilado)', 
                         fontsize=14, fontweight='bold')
        axes[0].set_xticklabels(weekday_names[:len(weekday_data)], rotation=45)
        axes[0].legend(['Negativo', 'Positivo'], fontsize=11)
        axes[0].grid(axis='y', alpha=0.3)
        
        # Gráfica de proporción
        weekday_prop = weekday_data.div(weekday_data.sum(axis=1), axis=0) * 100
        weekday_prop.plot(kind='bar', ax=axes[1], color=['#e74c3c', '#3498db'], 
                         alpha=0.8, edgecolor='black')
        axes[1].set_xlabel('Día de la Semana', fontsize=12, fontweight='bold')
        axes[1].set_ylabel('Proporción (%)', fontsize=12, fontweight='bold')
        axes[1].set_title('Proporción de Sentimientos por Día de la Semana', 
                         fontsize=14, fontweight='bold')
        axes[1].set_xticklabels(weekday_names[:len(weekday_data)], rotation=45)
        axes[1].legend(['Negativo', 'Positivo'], fontsize=11)
        axes[1].grid(axis='y', alpha=0.3)
        axes[1].set_ylim([0, 100])
        
        plt.tight_layout()
        output_file = os.path.join(self.output_dir, '04_weekday_pattern.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"  ✅ Guardada en: {output_file}")
        plt.close()
    
    def plot_news_count_distribution(self):
        """
        Gráfica 5: Distribución del número de noticias por día
        """
        print("\n📊 Generando gráfica 5: Distribución de noticias por día...")
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Histograma general
        axes[0, 0].hist(self.df['News_Count'], bins=25, color='#9b59b6', 
                       alpha=0.7, edgecolor='black')
        axes[0, 0].set_xlabel('Número de Noticias por Día', fontsize=11, fontweight='bold')
        axes[0, 0].set_ylabel('Frecuencia', fontsize=11, fontweight='bold')
        axes[0, 0].set_title('Distribución del Número de Noticias', fontsize=12, fontweight='bold')
        axes[0, 0].grid(axis='y', alpha=0.3)
        axes[0, 0].axvline(self.df['News_Count'].mean(), color='red', 
                          linestyle='--', linewidth=2, label=f'Media: {self.df["News_Count"].mean():.1f}')
        axes[0, 0].legend()
        
        # Boxplot por sentimiento
        self.df.boxplot(column='News_Count', by='Label', ax=axes[0, 1], 
                       patch_artist=True, grid=False)
        axes[0, 1].set_xlabel('Sentimiento', fontsize=11, fontweight='bold')
        axes[0, 1].set_ylabel('Número de Noticias', fontsize=11, fontweight='bold')
        axes[0, 1].set_title('Número de Noticias por Sentimiento', fontsize=12, fontweight='bold')
        axes[0, 1].set_xticklabels(['Negativo (0)', 'Positivo (1)'])
        plt.sca(axes[0, 1])
        plt.xticks(rotation=0)
        
        # Tendencia temporal de noticias
        news_by_month = self.df.groupby(pd.Grouper(key='Date', freq='M'))['News_Count'].mean()
        axes[1, 0].plot(news_by_month.index, news_by_month.values, 
                       color='#27ae60', linewidth=2, marker='o', markersize=4)
        axes[1, 0].set_xlabel('Fecha', fontsize=11, fontweight='bold')
        axes[1, 0].set_ylabel('Promedio de Noticias', fontsize=11, fontweight='bold')
        axes[1, 0].set_title('Promedio Mensual de Noticias por Día', fontsize=12, fontweight='bold')
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Estadísticas descriptivas
        stats_text = f"""
        Estadísticas de Noticias por Día:
        
        Media:     {self.df['News_Count'].mean():.2f}
        Mediana:   {self.df['News_Count'].median():.2f}
        Moda:      {self.df['News_Count'].mode()[0] if len(self.df['News_Count'].mode()) > 0 else 'N/A'}
        Desv. Est: {self.df['News_Count'].std():.2f}
        Mínimo:    {self.df['News_Count'].min()}
        Máximo:    {self.df['News_Count'].max()}
        Q1:        {self.df['News_Count'].quantile(0.25):.2f}
        Q3:        {self.df['News_Count'].quantile(0.75):.2f}
        """
        
        axes[1, 1].text(0.1, 0.5, stats_text, fontsize=11, 
                       verticalalignment='center', family='monospace',
                       bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        axes[1, 1].axis('off')
        
        plt.tight_layout()
        output_file = os.path.join(self.output_dir, '05_news_count_distribution.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"  ✅ Guardada en: {output_file}")
        plt.close()
    
    def plot_quarterly_heatmap(self):
        """
        Gráfica 6 (BONUS): Mapa de calor de sentimientos por trimestre
        """
        print("\n📊 Generando gráfica BONUS: Mapa de calor trimestral...")
        
        # Crear pivot table
        quarterly_data = self.df.pivot_table(
            values='Label', 
            index='Year', 
            columns='Quarter', 
            aggfunc='mean'
        )
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        sns.heatmap(quarterly_data, annot=True, fmt='.3f', cmap='RdYlGn', 
                   center=0.5, cbar_kws={'label': 'Sentimiento Promedio'},
                   linewidths=0.5, ax=ax)
        
        ax.set_xlabel('Trimestre', fontsize=12, fontweight='bold')
        ax.set_ylabel('Año', fontsize=12, fontweight='bold')
        ax.set_title('Mapa de Calor: Sentimiento Promedio por Trimestre', 
                    fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        output_file = os.path.join(self.output_dir, '06_quarterly_heatmap.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"  ✅ Guardada en: {output_file}")
        plt.close()
    
    def generate_all_plots(self):
        """
        Genera todas las visualizaciones
        """
        print("\n" + "=" * 80)
        print("🎨 GENERANDO VISUALIZACIONES DE ANÁLISIS EXPLORATORIO")
        print("=" * 80)
        
        self.plot_sentiment_distribution()
        self.plot_temporal_trend()
        self.plot_yearly_sentiment()
        self.plot_weekday_pattern()
        self.plot_news_count_distribution()
        self.plot_quarterly_heatmap()
        
        print("\n" + "=" * 80)
        print("✅ TODAS LAS VISUALIZACIONES GENERADAS EXITOSAMENTE")
        print(f"📁 Ubicación: {os.path.abspath(self.output_dir)}")
        print("=" * 80)
    
    def generate_summary_report(self):
        """
        Genera un reporte resumen del análisis exploratorio
        """
        print("\n" + "=" * 80)
        print("📄 REPORTE RESUMEN - ANÁLISIS EXPLORATORIO DE DATOS")
        print("=" * 80)
        
        print(f"\n📊 INFORMACIÓN GENERAL:")
        print(f"  • Total de registros: {len(self.df)}")
        print(f"  • Rango de fechas: {self.df['Date'].min().strftime('%Y-%m-%d')} a {self.df['Date'].max().strftime('%Y-%m-%d')}")
        print(f"  • Días totales: {(self.df['Date'].max() - self.df['Date'].min()).days}")
        
        print(f"\n💭 DISTRIBUCIÓN DE SENTIMIENTOS:")
        sentiment_counts = self.df['Label'].value_counts()
        for label, count in sentiment_counts.items():
            label_name = 'Negativo' if label == 0 else 'Positivo'
            percentage = (count / len(self.df)) * 100
            print(f"  • {label_name} ({label}): {count} ({percentage:.2f}%)")
        
        print(f"\n📰 ESTADÍSTICAS DE NOTICIAS:")
        print(f"  • Promedio de noticias por día: {self.df['News_Count'].mean():.2f}")
        print(f"  • Mediana: {self.df['News_Count'].median():.2f}")
        print(f"  • Desviación estándar: {self.df['News_Count'].std():.2f}")
        print(f"  • Rango: {self.df['News_Count'].min()} - {self.df['News_Count'].max()}")
        
        print(f"\n📅 DISTRIBUCIÓN TEMPORAL:")
        years = self.df['Year'].value_counts().sort_index()
        for year, count in years.items():
            print(f"  • Año {year}: {count} días")
        
        print(f"\n🗓️ PATRÓN SEMANAL:")
        weekday_names = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        weekday_counts = self.df['DayOfWeek'].value_counts().sort_index()
        for day, count in weekday_counts.items():
            if day < len(weekday_names):
                print(f"  • {weekday_names[day]}: {count} días")
        
        print("\n" + "=" * 80)


def main():
    """
    Función principal para ejecutar el EDA
    """
    print("=" * 80)
    print("🔍 STOCK SENTIMENT ANALYSIS - EXPLORATORY DATA ANALYSIS")
    print("=" * 80)
    
    # Inicializar EDA
    eda = StockSentimentEDA()
    
    # Cargar datos
    eda.load_data()
    
    # Generar todas las visualizaciones
    eda.generate_all_plots()
    
    # Generar reporte resumen
    eda.generate_summary_report()


if __name__ == "__main__":
    main()
