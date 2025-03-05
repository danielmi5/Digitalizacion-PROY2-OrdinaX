import os, shutil
import datetime, time
import re
import config  # Importa la configuración

def registros_salto():
     with open(config.ARCHIVO_LOG, "a", encoding="utf-8") as log:
        log.write("\n")

# Función para registrar eventos en el archivo de log
def registrar_evento(msj):
    """ Registra eventos en un archivo de texto. """
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(config.ARCHIVO_LOG, "a", encoding="utf-8") as log:
        log.write(f"{fecha_hora} - {msj}\n")

# Función para clasificar por tipo de archivo
def clasificador_por_tipo(origen):
    """ Mueve archivos a carpetas según su extensión. """
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            extension = os.path.splitext(archivo)[-1].lower()
            for carpeta, extensiones in config.TIPOS_DE_ARCHIVOS.items():
                if extension in extensiones:
                    mover_archivo(ruta_completa, os.path.join(origen, carpeta))

# Función para clasificar por fecha
def clasificador_por_fecha(origen):
    """ Mueve archivos a carpetas según su año de modificación. """
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            anio_archivo = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_completa)).year
            mover_archivo(ruta_completa, os.path.join(origen, str(anio_archivo)))

# Función para clasificar por patrón de nombre
def clasificador_por_patron(origen, nombre_carpeta, patron):
    """ Mueve archivos que coincidan con un patrón de nombre. """
    regex = re.compile(patron)
    for archivo in os.listdir(origen):
        if regex.match(os.path.splitext(archivo)[0]):
            mover_archivo(os.path.join(origen, archivo), os.path.join(origen, nombre_carpeta))

# Función para clasificar según varios patrones de nombres
def clasificador_por_patron2(origen, dict_patrones):
    """ Clasifica archivos en varias carpetas según patrones de nombres. """
    for nombre_carpeta, patron in dict_patrones.items():
        clasificador_por_patron(origen, nombre_carpeta, patron)

# Función para mover archivos a la carpeta destino
def mover_archivo(archivo, destino):
    """ Mueve un archivo a la carpeta destino, creándola si es necesario. """
    try:
        if not os.path.exists(destino):
            os.makedirs(destino)
            registrar_evento(f"Carpeta creada: {destino}")

        shutil.move(archivo, os.path.join(destino, os.path.basename(archivo)))
        registrar_evento(f"Archivo {os.path.basename(archivo)} movido a: {destino}")
    except Exception as e:
        registrar_evento(f"Error al mover {os.path.basename(archivo)}: {e}")

# Función para mostrar el log de actividades
def mostrar_log():
    """ Muestra el contenido del archivo de registro en la consola. """
    if os.path.exists(config.ARCHIVO_LOG):
        with open(config.ARCHIVO_LOG, "r", encoding="utf-8") as log:
            print("=== REGISTRO DE ACTIVIDAD ===")
            print(log.read())
    else:
        print("No hay registros disponibles.")

# Función principal que ejecuta la clasificación
def ejecutar_clasificacion():
    origen = config.RUTA_ORIGEN  # Utiliza la ruta definida en config.py

    if not os.path.exists(origen):
        print("La ruta especificada no existe.")
        return

    registrar_evento(f"Iniciando clasificación en: {origen}")
    
    # Clasificación por tipo de archivo
    clasificador_por_tipo(origen)
    
    # Clasificación por fecha
    clasificador_por_fecha(origen)
    
    # Clasificación por patrón (por ejemplo, para imágenes)
    clasificador_por_patron2(os.path.join(origen, "python"), config.PATRONES)

    registros_salto()


# Función para ejecutar automáticamente cada tiempo (valor en config.py)
def ejecutar_automáticamente():
    while True:
        # Ejecuta la clasificación automáticamente
        ejecutar_clasificacion()
        registros_salto()
        # Espera 24 horas (86400 segundos) antes de ejecutar nuevamente
        time.sleep(config.TIEMPO_ENTRE_CADA_CLASIFICACION)
        


def main():
    auto_ejecutar = config.CLASIFICAR_AUTOMATICO

    if auto_ejecutar == True:
        ejecutar_automáticamente()  # Ejecuta automáticamente cada 24 horas
    else:
        ejecutar_clasificacion()  # Ejecuta solo una vez
    

# Ejecutar el programa
if __name__ == "__main__":
    main()
