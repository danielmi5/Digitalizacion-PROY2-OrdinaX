import os
import shutil
import datetime
import time
import re
import logging
import config

# Configuración del logging
logging.basicConfig(filename=config.ARCHIVO_LOG, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def registros_salto():
    logging.info("\n")

# Función para registrar eventos en el archivo de log
def registrar_evento(msj, nivel=logging.INFO):
    """Registra eventos usando la biblioteca logging con diferentes niveles."""
    logging.log(nivel, msj)  # Utiliza logging.log para especificar el nivel

# Función para registrar eventos en el archivo de log
def registrar_titulo(msj):
    """Registra títulos en un archivo de texto."""
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(config.ARCHIVO_LOG, "a", encoding="utf-8") as log:
        log.write(f"\n================= {fecha_hora} - {msj} =================\n")

# Funciones de clasificación individuales
def clasificador_por_tipo(origen):
    """Mueve archivos a carpetas según su extensión."""
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            extension = os.path.splitext(archivo)[-1].lower()
            for carpeta, extensiones in config.TIPOS_DE_ARCHIVOS.items():
                if extension in extensiones:
                    mover_archivo(ruta_completa, os.path.join(origen, carpeta))
                    break  # Importante: Sale del bucle después de encontrar el tipo

def clasificador_por_fecha(origen):
    """Mueve archivos a carpetas según su año de modificación."""
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            anio_archivo = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_completa)).year
            mover_archivo(ruta_completa, os.path.join(origen, str(anio_archivo)))

def clasificador_por_patron(origen, nombre_carpeta, patron):
    """Mueve archivos que coincidan con un patrón de nombre."""
    regex = re.compile(patron)
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):  # Verifica que sea un archivo
            if regex.match(os.path.splitext(archivo)[0]):
                mover_archivo(ruta_completa, os.path.join(origen, nombre_carpeta))

# Función para clasificar según varios patrones de nombres
def clasificador_por_patron2(origen, dict_patrones):
    """Clasifica archivos en varias carpetas según patrones de nombres."""
    for nombre_carpeta, patron in dict_patrones.items():
        clasificador_por_patron(origen, nombre_carpeta, patron)

# Función para mover archivos a la carpeta destino
def mover_archivo(archivo, destino):
    """Mueve un archivo a la carpeta destino, creándola si es necesario."""
    try:
        if not os.path.exists(destino):
            os.makedirs(destino)
            registrar_evento(f"Carpeta creada: {destino}")
        
        # Mover el archivo solo si no existe ya en el destino
        destino_completo = os.path.join(destino, os.path.basename(archivo))
        if not os.path.exists(destino_completo):
            shutil.move(archivo, destino_completo)
            registrar_evento(f"Archivo {os.path.basename(archivo)} movido a: {destino}")
        else:
            registrar_evento(f"Archivo {os.path.basename(archivo)} ya existe en: {destino}", logging.WARNING)

    except Exception as e:
        registrar_evento(f"Error al mover {os.path.basename(archivo)}: {e}", logging.ERROR)  # Registra el error con nivel ERROR

# Función para mostrar el log de actividades
def mostrar_log():
    """Muestra el contenido del archivo de registro en la consola."""
    if os.path.exists(config.ARCHIVO_LOG):
        with open(config.ARCHIVO_LOG, "r", encoding="utf-8") as log:
            print("=== REGISTRO DE ACTIVIDAD ===")
            print(log.read())
    else:
        print("No hay registros disponibles.")

# Nueva función recursiva para clasificar según el orden configurado
def clasificar_recursivamente(origen, orden_clasificacion):
    """Clasifica archivos recursivamente según el orden definido en la configuración."""
    if not orden_clasificacion:
        return  # Caso base: no hay más criterios de clasificación

    criterio = orden_clasificacion[0]
    resto_criterios = orden_clasificacion[1:]

    if criterio == "tipo":
        clasificador_por_tipo(origen)
        # Aplica la clasificación recursiva a las subcarpetas de tipo
        for carpeta_tipo in config.TIPOS_DE_ARCHIVOS.keys():
            ruta_carpeta_tipo = os.path.join(origen, carpeta_tipo)
            if os.path.exists(ruta_carpeta_tipo):  # Verifica si la carpeta existe
                clasificar_recursivamente(ruta_carpeta_tipo, resto_criterios)
    elif criterio == "fecha":
        clasificador_por_fecha(origen)
        # Aplica la clasificación recursiva a las subcarpetas de fecha (año)
        for anio in [d for d in os.listdir(origen) if os.path.isdir(os.path.join(origen, d)) and d.isdigit()]:
            ruta_carpeta_anio = os.path.join(origen, anio)
            clasificar_recursivamente(ruta_carpeta_anio, resto_criterios)
    elif criterio == "patron":
        clasificador_por_patron2(origen, config.PATRONES)
    else:
        registrar_evento(f"Criterio de clasificación desconocido: {criterio}", logging.WARNING)

# Función principal que ejecuta la clasificación
def ejecutar_clasificacion():
    origen = config.RUTA_ORIGEN  # Utiliza la ruta definida en config.py
    if not os.path.exists(origen):
        print("La ruta especificada no existe.")
        return

    registrar_titulo(f"Iniciando clasificación en: {origen}")
    clasificar_recursivamente(origen, config.ORDEN_CLASIFICACION)

# Función para ejecutar automáticamente cada tiempo (valor en config.py)
def ejecutar_automaticamente():
    while True:
        # Ejecuta la clasificación automáticamente
        ejecutar_clasificacion()
        # Espera el tiempo configurado antes de ejecutar nuevamente
        time.sleep(config.TIEMPO_ENTRE_CADA_CLASIFICACION)

def main():
    auto_ejecutar = config.CLASIFICAR_AUTOMATICO
    if auto_ejecutar:
        ejecutar_automaticamente()  # Ejecuta automáticamente
    else:
        ejecutar_clasificacion()  # Ejecuta solo una vez

# Ejecutar el programa
if __name__ == "__main__":
    main()

