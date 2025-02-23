import os, shutil, datetime

# Diccionario con las categorías de carpetas y las extensiones asociadas
tipos_de_archivos = {
    "python": [".py", ".pyc", ".pyo"],  # Archivos Python
    "kotlin": ["kt"],  # Archivos Kotlin
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

    # Recorre todos los archivos en la carpeta de origen
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):  # Verifica si es un archivo

            print(f"Archivo: {archivo}")

            # Obtiene la extensión del archivo
            extension = os.path.splitext(archivo)[-1].lower()

            # Recorre las carpetas de tipo de archivo
            for carpeta in tipos_de_archivos.keys():

                if extension in tipos_de_archivos[carpeta]:
                    destino = os.path.join(origen, carpeta)

                    # Si la carpeta no existe, la crea.
                    if not os.path.exists(destino):
                        os.makedirs(destino)
                        print(f"Carpeta creada: {destino}")

                    # Mover el archivo
                    try:
                        shutil.move(ruta_completa, os.path.join(destino, archivo))
                        print(f"Archivo {archivo} movido a: {destino}")
                    except Exception as e:
                        print(f"Error al mover el archivo {archivo}: {e}")


def clasificador_por_fecha(origen, recorre_carpetas = False):
    if not recorre_carpetas:
        # Recorre todos los archivos en la carpeta de origen
        for archivo in os.listdir(origen):
            ruta_completa = os.path.join(origen, archivo)
            tiempo = os.path.getmtime(ruta_completa)
            anio_archivo = datetime.datetime.fromtimestamp(tiempo).year
            destino = os.path.join(origen, str(anio_archivo))
            if os.path.isfile(ruta_completa):  # Verifica si es un archivo

                print(f"Archivo: {archivo}")

                # Si la carpeta no existe, la crea.
                if not os.path.exists(destino):
                    os.makedirs(destino)
                    print(f"Carpeta creada: {destino}")

                # Mover el archivo
                try:
                    shutil.move(ruta_completa, os.path.join(destino, archivo))
                    print(f"Archivo {archivo} movido a: {destino}")
                except Exception as e:
                    print(f"Error al mover el archivo {archivo}: {e}")
            else: print("ARCHIVO MALO")



def main():
    origen = "C:\\Users\danie\Documents\zDAWGIT\\xgit\Digitalizacion-PROY2-OrdinaX\prueba"

    # Verificar si la ruta de origen existe
    if not os.path.exists(origen):
        print("La ruta especificada no existe.")
    else:
        clasificador_por_tipo(origen)
        clasificador_por_fecha(os.path.join(origen, "python"))



if __name__ == "__main__":
    main()

