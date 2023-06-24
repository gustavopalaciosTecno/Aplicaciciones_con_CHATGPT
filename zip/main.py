import zipfile

# Nombre del archivo ZIP que vamos a crear
archivo_zip = "miarchivo.zip"

# Creamos un objeto ZipFile
mi_zip = zipfile.ZipFile(archivo_zip, mode='w')

# Agregamos archivos al ZIP
mi_zip.write("C:/Curso/app-chatgpt/zip/archivo1.txt")
mi_zip.write("C:/Curso/app-chatgpt/zip/archivo2.txt")
mi_zip.write("C:/Curso/app-chatgpt/zip/archivo3.txt")

# escribimos hola mundo en el archivo1.text
mi_zip.writestr("C:/Curso/app-chatgpt/zip/archivo1.txt", "Hola mundo desde ChatGPT")

# Cerramos el objeto ZipFile
mi_zip.close()