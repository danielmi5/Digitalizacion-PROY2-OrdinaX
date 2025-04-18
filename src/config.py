# --------------------------------------------
# Archivo de Configuración para el Organizador
# --------------------------------------------
# Aquí se definen rutas, parámetros de ejecución,
# criterios de clasificación y estructuras de carpetas.
# Este archivo es utilizado por el script principal.

# Ruta del directorio que se desea clasificar
RUTA_ORIGEN = "prueba"  # Cambiar esta ruta a la carpeta deseada

# Determina si la clasificación se ejecuta en modo automático
CLASIFICAR_AUTOMATICO = False  # True = ejecuta indefinidamente; False = solo una vez

# Tiempo de espera entre cada clasificación (en segundos) si está en automático
TIEMPO_ENTRE_CADA_CLASIFICACION = 86400  # Ejemplo: 86400 = 24 horas

# Orden de los criterios de clasificación a aplicar
# Opciones posibles: "tipo", "fecha", "patron"
ORDEN_CLASIFICACION = ["tipo", "fecha", "patron"]

# Diccionario de patrones (expresiones regulares simples) para clasificar por nombre
# Clave = nombre de la subcarpeta destino
# Valor = patrón que debe coincidir con el nombre del archivo (sin extensión)
PATRONES = {
    "msi": "msi",       # Archivos cuyo nombre contenga "msi"
    "python": "py",     # Archivos cuyo nombre contenga "py"
}

# Diccionario que define tipos de archivos según su extensión
# Clave = nombre de la subcarpeta destino
# Valor = lista de extensiones asociadas a ese tipo
TIPOS_DE_ARCHIVOS = {
    "python": [".py", ".pyc", ".pyo"],
    "kotlin": [".kt"],
    "documentos": [".docx", ".doc", ".pdf", ".txt", ".odt"],
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "presentaciones": [".pptx", ".ppt", ".odp"],
    "hojas_de_calculo": [".xlsx", ".xls", ".ods", ".csv"],
    "archivos_comprimidos": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "codigo_fuente": [".cpp", ".h", ".java", ".js", ".html", ".css"],
    "web": [".html", ".css", ".js"],
    "otros": [".md", ".json", ".xml", ".yml", ".ini", ".log"],
}

# Ruta del archivo donde se guardarán los logs del sistema
ARCHIVO_LOG = "src/registro_actividad.txt"
