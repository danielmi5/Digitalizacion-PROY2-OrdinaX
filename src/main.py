import os, shutil, datetime, re

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

hist = dict()


# Ruta del archivo de registro
LOG_FILE = "src\\registro_actividad.txt"

def registrar_evento(msj):
    """
    Registra eventos en un archivo de texto.
    """
    evento = LOG_FILE
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(evento, "a") as log:
        log.write(f"{fecha_hora} - {msj}\n")
        
def empezar_evento(evento):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(evento, "a") as log:
        log.write(f"{fecha}\n")

def clasificador_por_tipo(origen, tipos_de_archivos = tipos_de_archivos):
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            extension = os.path.splitext(archivo)[-1].lower()
            for carpeta, extensiones in tipos_de_archivos.items():
                if extension in extensiones:
                    destino = os.path.join(origen, carpeta)
                    if not os.path.exists(destino):
                        os.makedirs(destino)
                        registrar_evento(f"Carpeta creada: {destino}")
                    try:
                        shutil.move(ruta_completa, os.path.join(destino, archivo))
                        registrar_evento(f"Archivo {archivo} movido a: {destino}")
                    except Exception as e:
                        registrar_evento(f"Error al mover el archivo {archivo}: {e}")

def clasificador_por_fecha(origen):
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            tiempo = os.path.getmtime(ruta_completa)
            anio_archivo = datetime.datetime.fromtimestamp(tiempo).year
            destino = os.path.join(origen, str(anio_archivo))
            if not os.path.exists(destino):
                os.makedirs(destino)
                registrar_evento(f"Carpeta creada: {destino}")
            try:
                shutil.move(ruta_completa, os.path.join(destino, archivo))
                registrar_evento(f"Archivo {archivo} movido a: {destino}")
            except Exception as e:
                registrar_evento(f"Error al mover el archivo {archivo}: {e}")

def clasificador_por_patron(origen, nombreCarpeta, patron):
    regex = re.compile(patron)
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        nombre_sin_extension = os.path.splitext(archivo)[0]
        if regex.match(nombre_sin_extension):
            destino = os.path.join(origen, nombreCarpeta)
            if not os.path.exists(destino):
                os.makedirs(destino)
                registrar_evento(f"Carpeta creada: {destino}")
            try:
                shutil.move(ruta_completa, os.path.join(destino, archivo))
                registrar_evento(f"Archivo {archivo} movido a: {destino}")
            except Exception as e:
                registrar_evento(f"Error al mover el archivo {archivo}: {e}")

def clasificador_por_patron2(origen, dictPatrones):
    for nombreCarpeta, patron in dictPatrones.items():
        regex = re.compile(patron)
        for archivo in os.listdir(origen):
            ruta_completa = os.path.join(origen, archivo)
            nombre_sin_extension = os.path.splitext(archivo)[0]
            if regex.match(nombre_sin_extension):
                destino = os.path.join(origen, nombreCarpeta)
                if not os.path.exists(destino):
                    os.makedirs(destino)
                    registrar_evento(f"Carpeta creada: {destino}")
                try:
                    shutil.move(ruta_completa, os.path.join(destino, archivo))
                    registrar_evento(f"Archivo {archivo} movido a: {destino}")
                except Exception as e:
                    registrar_evento(f"Error al mover el archivo {archivo}: {e}")
        
def mostrar_log():
    """
    Muestra el contenido del archivo de registro en la consola.
    """
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as log:
            print("=== REGISTRO DE ACTIVIDAD ===")
            print(log.read())
    else:
        print("No hay registros disponibles.")

def main():
    origen = "C:\\Users\danie\Documents\zDAWGIT\\xgit\Digitalizacion-PROY2-OrdinaX\prueba"

    # Verificar si la ruta de origen existe
    if not os.path.exists(origen):
        print("La ruta especificada no existe.")
    else:
        empezar_evento(LOG_FILE)
        clasificador_por_tipo(origen)
        clasificador_por_fecha(origen)
        clasificador_por_patron2(origen+"\imagenes", {"msi" : "msi"})
    mostrar_log()



if __name__ == "__main__":
    main()

