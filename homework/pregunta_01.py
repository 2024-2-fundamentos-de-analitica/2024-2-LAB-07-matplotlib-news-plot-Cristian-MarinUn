"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    import os
    import pandas as pd
    import matplotlib.pyplot as plt


    """
    Carga los datos desde 'files/input/news.csv' y genera un gráfico de líneas,
    mostrando cómo la gente obtiene sus noticias a lo largo del tiempo.
    Guarda la imagen en 'files/plots/news.png'.
    """
    
    # Definir los colores, el orden en las capas y el grosor de línea por categoría
    estilo = {
        'Television': {'color': 'black', 'zorder': 1, 'linewidth': 2},
        'Newspaper': {'color': 'darkgray', 'zorder': 1, 'linewidth': 2},
        'Internet': {'color': 'blue', 'zorder': 2, 'linewidth': 3},
        'Radio': {'color': 'silver', 'zorder': 1, 'linewidth': 2},
    }
    
    # Cargar los datos
    ruta_datos = 'files/input/news.csv'
    df = pd.read_csv(ruta_datos, index_col=0)
    
    # Crear la figura
    plt.figure()
    
    for categoria, config in estilo.items():
        plt.plot(
            df[categoria],
            color=config['color'],
            label=categoria,
            zorder=config['zorder'],
            linewidth=config['linewidth']
        )
    
    # Configuración del gráfico
    plt.title('Evolución del Consumo de Noticias', fontsize=14)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    
    # Agregar etiquetas iniciales y finales
    for categoria, config in estilo.items():
        anio_inicio = df.index[0]
        anio_fin = df.index[-1]
        
        plt.scatter(anio_inicio, df[categoria][anio_inicio], color=config['color'], zorder=config['zorder'])
        plt.text(anio_inicio - 0.2, df[categoria][anio_inicio], f"{categoria} {df[categoria][anio_inicio]}%", ha='right', va='center', color=config['color'])
        
        plt.scatter(anio_fin, df[categoria][anio_fin], color=config['color'], zorder=config['zorder'])
        plt.text(anio_fin + 0.2, df[categoria][anio_fin], f"{categoria} {df[categoria][anio_fin]}%", ha='left', va='center', color=config['color'])
    
    # Crear carpeta de salida si no existe
    os.makedirs('files/plots', exist_ok=True)
    
    # Guardar la imagen
    plt.tight_layout()
    plt.savefig('files/plots/news.png')

pregunta_01()

