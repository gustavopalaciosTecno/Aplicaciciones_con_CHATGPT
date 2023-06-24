import csv
import pandas as pd


correos = []

with open('C:/Curso/app-chatgpt/csv/datos.csv', 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Omitir la primera fila de encabezados
    for fila in lector_csv:
        if len(fila) > 3:  # Verificar que la fila tenga al menos 4 elementos
            correo = fila[3]  # Obtener el correo electrónico (índice 3)
            correos.append(correo)

# Crear un DataFrame de pandas con los correos electrónicos
df = pd.DataFrame(correos, columns=['Correo Electrónico'])

# Guardar el DataFrame en un archivo Excel
df.to_excel('correos.xlsx', index=False)





# import csv

# correos = []

# with open('C:/Curso/app-chatgpt/csv/datos.csv', 'r', encoding='utf-8') as archivo_csv:
#     lector_csv = csv.reader(archivo_csv)
#     next(lector_csv)  # Omitir la primera fila de encabezados
#     for fila in lector_csv:
#         if len(fila) > 3:  # Verificar que la fila tenga al menos 4 elementos
#             correo = fila[3]  # Obtener el correo electrónico (índice 3)
#             correos.append(correo)

# # Imprimir los correos electrónicos obtenidos
# for correo in correos:
#     print(correo)

# # Contar la cantidad de correos electrónicos
# cantidad_correos = len(correos)
# print("Cantidad de correos electrónicos:", cantidad_correos)
