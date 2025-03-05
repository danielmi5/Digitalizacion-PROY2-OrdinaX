# Ruta del directorio que quieres clasificar
RUTA_ORIGEN = "C:\\Users\\danie\\Documents\\zDAWGIT\\xgit\\Digitalizacion-PROY2-OrdinaX\\prueba"  # Cambiar según sea necesario

CLASIFICAR_AUTOMATICO = False
TIEMPO_ENTRE_CADA_CLASIFICACION = 86400  #SOLO EN CASO DE QUE SEA AUTO Y EN SEGUNDOS

# Patrón para clasificar archivos en subcarpetas
PATRONES = {
    "msi": "msi",
    "python": "py",
}

# Diccionario con las categorías de archivos y sus extensiones
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

# Ruta para el archivo de registro
ARCHIVO_LOG = "src/registro_actividad.txt"