import os
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Establecer la ubicación de la carpeta "static"
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app.config['STATIC_FOLDER'] = static_folder

@app.route('/')
def index():
    # Cargar los datos del archivo CSV
    data = pd.read_csv('inflacion.csv')

    # Obtener los últimos 10 años
    last_10_years = data.tail(10)

    # Obtener los valores de año e inflación media
    years = last_10_years['Año']
    inflation = last_10_years['Inflación Media']

    # Generar el gráfico
    plt.plot(years, inflation, 'b-o')
    plt.xlabel('Año')
    plt.ylabel('Inflación Media')
    plt.title('Inflación Media en Argentina (Últimos 10 años)')
    plt.grid(True)

    # Guardar el gráfico en un archivo
    graph_path = os.path.join(app.config['STATIC_FOLDER'], 'grafico.png')
    plt.savefig(graph_path)

    # Renderizar la plantilla HTML
    return render_template('index.html', graph_path=graph_path)

if __name__ == '__main__':
    app.run()
