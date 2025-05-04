"""
Organizador de Archivos Automatizado
-------------------------------------
Este script clasifica y organiza archivos desde una carpeta origen usando criterios configurables como:
- Tipo de archivo (por extensión)
- Fecha de modificación
- Patrón en el nombre del archivo

La configuración general se toma desde un archivo `config.py`, el cual debe definir rutas, patrones, y opciones de ejecución.

Requiere: Python 3.x, módulos estándar (os, shutil, datetime, logging, re), y un archivo de configuración `config.py`.
"""

import os
import shutil
import datetime
import time
import re
import logging
from src import config

# Configuración del sistema de logs
logging.basicConfig(filename=config.ARCHIVO_LOG, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def registros_salto():
    """Agrega una línea vacía al archivo de log (salto visual)."""
    logging.info("\n")

def registrar_evento(msj, nivel=logging.INFO):
    """
    Registra un evento en el archivo de log con el nivel especificado.
    
    Parámetros:
    - msj (str): Mensaje a registrar.
    - nivel (int): Nivel de logging (INFO, WARNING, ERROR, etc.).
    """
    logging.log(nivel, msj)

def registrar_titulo(msj):
    """
    Escribe un título destacado en el archivo de log con la fecha y hora actual.

    Parámetro:
    - msj (str): Título del bloque de operaciones.
    """
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(config.ARCHIVO_LOG, "a", encoding="utf-8") as log:
        log.write(f"\n================= {fecha_hora} - {msj} =================\n")

def clasificador_por_tipo(origen):
    """
    Clasifica archivos en carpetas según su tipo/extensión.

    Parámetro:
    - origen (str): Ruta donde se encuentran los archivos a organizar.
    """
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            extension = os.path.splitext(archivo)[-1].lower()
            for carpeta, extensiones in config.TIPOS_DE_ARCHIVOS.items():
                if extension in extensiones:
                    mover_archivo(ruta_completa, os.path.join(origen, carpeta))
                    break

def clasificador_por_fecha(origen):
    """
    Clasifica archivos en carpetas por año de última modificación.

    Parámetro:
    - origen (str): Ruta de los archivos.
    """
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            anio_archivo = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_completa)).year
            mover_archivo(ruta_completa, os.path.join(origen, str(anio_archivo)))

def clasificador_por_patron(origen, nombre_carpeta, patron):
    """
    Clasifica archivos que coincidan con un patrón de nombre.

    Parámetros:
    - origen (str): Ruta origen de archivos.
    - nombre_carpeta (str): Nombre de la carpeta destino.
    - patron (str): Expresión regular para coincidencias.
    """
    regex = re.compile(patron)
    for archivo in os.listdir(origen):
        ruta_completa = os.path.join(origen, archivo)
        if os.path.isfile(ruta_completa):
            if regex.match(os.path.splitext(archivo)[0]):
                mover_archivo(ruta_completa, os.path.join(origen, nombre_carpeta))

def clasificador_por_patron2(origen, dict_patrones):
    """
    Clasifica archivos en múltiples carpetas según un diccionario de patrones.

    Parámetros:
    - origen (str): Ruta de origen.
    - dict_patrones (dict): Diccionario con nombre_carpeta: patron.
    """
    for nombre_carpeta, patron in dict_patrones.items():
        clasificador_por_patron(origen, nombre_carpeta, patron)

def mover_archivo(archivo, destino):
    """
    Mueve un archivo al destino indicado, creando la carpeta si no existe.

    Parámetros:
    - archivo (str): Ruta del archivo a mover.
    - destino (str): Ruta del destino.
    """
    try:
        if not os.path.exists(destino):
            os.makedirs(destino)
            registrar_evento(f"Carpeta creada: {destino}")
        
        destino_completo = os.path.join(destino, os.path.basename(archivo))
        if not os.path.exists(destino_completo):
            shutil.move(archivo, destino_completo)
            registrar_evento(f"Archivo {os.path.basename(archivo)} movido a: {destino}")
        else:
            registrar_evento(f"Archivo {os.path.basename(archivo)} ya existe en: {destino}", logging.WARNING)

    except Exception as e:
        registrar_evento(f"Error al mover {os.path.basename(archivo)}: {e}", logging.ERROR)

def mostrar_log():
    """Muestra el contenido actual del archivo de log por consola."""
    if os.path.exists(config.ARCHIVO_LOG):
        with open(config.ARCHIVO_LOG, "r", encoding="utf-8") as log:
            print("=== REGISTRO DE ACTIVIDAD ===")
            print(log.read())
    else:
        print("No hay registros disponibles.")

def clasificar_recursivamente(origen, orden_clasificacion):
    """
    Clasifica archivos de forma recursiva aplicando los criterios en orden.

    Parámetros:
    - origen (str): Ruta de archivos.
    - orden_clasificacion (list): Lista de criterios en orden: "tipo", "fecha", "patron".
    """
    if not orden_clasificacion:
        return

    criterio = orden_clasificacion[0]
    resto_criterios = orden_clasificacion[1:]

    if criterio == "tipo":
        clasificador_por_tipo(origen)
        for carpeta_tipo in config.TIPOS_DE_ARCHIVOS.keys():
            ruta_carpeta_tipo = os.path.join(origen, carpeta_tipo)
            if os.path.exists(ruta_carpeta_tipo):
                clasificar_recursivamente(ruta_carpeta_tipo, resto_criterios)
    elif criterio == "fecha":
        clasificador_por_fecha(origen)
        for anio in [d for d in os.listdir(origen) if os.path.isdir(os.path.join(origen, d)) and d.isdigit()]:
            ruta_carpeta_anio = os.path.join(origen, anio)
            clasificar_recursivamente(ruta_carpeta_anio, resto_criterios)
    elif criterio == "patron":
        clasificador_por_patron2(origen, config.PATRONES)
    else:
        registrar_evento(f"Criterio de clasificación desconocido: {criterio}", logging.WARNING)

def ejecutar_clasificacion():
    """Ejecuta la clasificación de archivos una vez."""
    origen = config.RUTA_ORIGEN
    if not os.path.exists(origen):
        print("La ruta especificada no existe.")
        return

    registrar_titulo(f"Iniciando clasificación en: {origen}")
    clasificar_recursivamente(origen, config.ORDEN_CLASIFICACION)

def ejecutar_automaticamente():
    """
    Ejecuta la clasificación continuamente cada cierto tiempo
    definido en config.TIEMPO_ENTRE_CADA_CLASIFICACION.
    """
    while True:
        ejecutar_clasificacion()
        time.sleep(config.TIEMPO_ENTRE_CADA_CLASIFICACION)

def main():
    """
    Función principal que inicia el programa.
    Decide si se ejecuta automáticamente o solo una vez.
    """
    auto_ejecutar = config.CLASIFICAR_AUTOMATICO
    if auto_ejecutar:
        ejecutar_automaticamente()
    else:
        ejecutar_clasificacion()

if __name__ == "__main__":
    main()

