import os, shutil

# Diccionario con las categorías de carpetas y las extensiones asociadas
tipos_de_archivos = {
    "python": [".py", ".pyc", ".pyo"], # Archivos Python
    "kotlin": ["kt"], # Archivos Kotlin
    "documentos": [".docx", ".doc", ".pdf", ".txt", ".odt"],  # Archivos de texto y documentos
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],  # Archivos de imagen
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],  # Archivos de video
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],  # Archivos de audio
    "presentaciones": [".pptx", ".ppt", ".odp"],  # Archivos de presentaciones
    "hojas_de_calculo": [".xlsx", ".xls", ".ods", ".csv"],  # Archivos de hojas de cálculo
    "archivos_comprimidos": [".zip", ".rar", ".tar", ".gz", ".7z"],  # Archivos comprimidos
    "codigo_fuente": [".cpp", ".h", ".java", ".js", ".html", ".css"],  # Archivos de código fuente
    "web": [".html", ".css", ".js"],  # Archivos web
    "otros": [".md", ".json", ".xml", ".yml", ".ini", ".log"],  # Otros tipos de archivo comunes
}

def clasificador_por_tipo(origen):
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            #Obtengo la extensión del archivo
            extension = os.path.splitext(archivo)
            print(extension)
            break

            
def main():
    clasificador_por_tipo("")
