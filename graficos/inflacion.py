import pandas as pd
import random

# Generar años del 2013 al 2022
years = list(range(2013, 2023))

# Generar valores de inflación aleatorios entre 0 y 30%
inflation = [random.uniform(0, 30) for _ in range(10)]

# Crear DataFrame de pandas
df = pd.DataFrame({'Año': years, 'Inflación Media': inflation})

# Guardar DataFrame en archivo CSV
df.to_csv('inflacion.csv', index=False)
