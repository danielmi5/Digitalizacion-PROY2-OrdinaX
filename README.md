# Sistema de Organización Automática de Archivos - OrdinaX

## Descripción General  
El proyecto consiste en un **sistema de organización automática de archivos**, diseñado para facilitar la gestión y clasificación de documentos dentro de un sistema de directorios.  

El objetivo principal es **automatizar** la tarea de organizar archivos de manera eficiente, permitiendo que estos se **clasifiquen y se muevan** sin intervención manual. Este sistema es ideal para usuarios que manejan grandes volúmenes de archivos y necesitan mantener un orden coherente sin invertir tiempo en tareas repetitivas.  

## Motivación

Elegí la organización de archivos porque constantemente me enfrento a carpetas desordenadas ya sean proyectos, descargas o documentos personales y sentí la necesidad de una solución automatizada que hiciera este trabajo por mí. He logrado integrar este organizador en mi flujo diario, y desde entonces, la limpieza de carpetas ha pasado de ser una tarea tediosa a una operación silenciosa y automática. Si te interesa cómo hacerlo funcionar en tu entorno, puedes seguir la guía de uso incluida más abajo.


## ¿Por qué?

OrdenaX busca ayudarte a clasificar y mover archivos en tu sistema de forma automática e inteligente. A veces, la simplicidad también comunica mejor.

Este proyecto quiere ser una herramienta útil, clara y extensible para estudiantes, profesionales o cualquier persona que quiera tener sus carpetas organizadas.

## Objetivos  
- **Reducir el tiempo y esfuerzo** dedicado a la organización manual de archivos.  
- **Asegurar un almacenamiento estructurado y accesible** para distintos tipos de documentos.  
- **Evitar la pérdida de información** mediante registros de actividad detallados.  
- **Optimizar la productividad**, permitiendo que el usuario se enfoque en tareas más importantes.  

## Cómo funciona

El Organizador de Archivos Automatizado sigue un flujo en varias etapas, inspirado en cómo lo haría una persona metódica:

1. **Análisis inicial**: Recorre la carpeta especificada y detecta todos los archivos disponibles. Extrae su tipo (extensión), nombre y fecha de modificación.

2. **Aplicación de reglas**: Evalúa el orden definido en `ORDEN_CLASIFICACION`, que puede incluir:
   - Tipo de archivo
   - Año de modificación
   - Patrones de nombre

3. **Clasificación**: Mueve los archivos a subcarpetas según las reglas aplicadas. Por ejemplo:
   - `documentos/2023/` para archivos `.pdf` modificados en 2023.
   - `imagenes/` para archivos `.png` o `.jpg`.
   - `otros/` para archivos sin coincidencias claras.

4. **Registro de actividad**: Todas las operaciones quedan registradas en `registro_actividad.txt`, lo que permite auditar cambios o diagnosticar errores.

5. **Ejecución automática (opcional)**: Si se activa, el script puede ejecutarse cada cierto tiempo de manera automática, por ejemplo, cada 24 horas.

Este enfoque modular permite modificar fácilmente cada etapa sin romper el funcionamiento general del sistema.

## Características  

### 📂 Clasificación Automática  
El sistema organizará los archivos en base a diferentes criterios:  
- **Por tipo de archivo:** Se almacenarán en carpetas según su extensión.  
  - Ejemplo: `Python -> .py`, `Word -> .docx`, `Imágenes -> .jpg, .png`.  
- **Por fecha:** Se clasificarán según la fecha de creación o modificación.  
  - Ejemplo: Carpetas organizadas por año `2022, 2023...`.   
- **Por nombre o patrón:** Permitirá filtrar y ordenar archivos siguiendo un esquema de nombres definido.  

### 🔄 Modo Automático y Manual  
- **Modo Automático:** El sistema monitorea la carpeta de origen y clasifica los archivos en tiempo real.  
- **Modo Manual:** El usuario podrá ejecutar la organización bajo demanda.  

### 📜 Registros y Seguridad  
- **Registro de actividad:** Se almacenará un historial detallado de archivos movidos, renombrados y errores detectados.  
- **Manejo de errores:** En caso de archivos corruptos o conflictos de nombres, se generarán alertas y soluciones alternativas.  
- **Recuperación de archivos:** Opción para revertir cambios en caso de errores accidentales.

## Ejemplos de uso

1. **Clasificación de archivos por extensión**

Este ejemplo muestra cómo usar el organizador para mover archivos según su tipo de extensión. Puedes modificar las reglas en el archivo `config.py` para ajustarlas a tus necesidades.
Imagina que tienes la carpeta `descargas` con archivos de diferentes tipos, y deseas mover diferentes tipos de archivos a distintas carpetas.

```python
# La ruta de la carpeta elegida (descargas)
RUTA = ~/Descargas

"""
Diccionario que define tipos de archivos según su extensión
Clave = nombre de la subcarpeta destino
Valor = lista de extensiones asociadas a ese tipo
"""
TIPOS_DE_ARCHIVOS = {
    "documentos": [".pdf", ".docx", ".txt"],
    "imagenes": [".jpg", ".jpeg", ".png"],
    "videos": [".mp4", ".mkv"]
}

# Ejecutar la clasificación por extensión en la carpeta "descargas"
clasificador_por_tipo(RUTA)
```
Este script moverá los archivos .pdf, .docx, .txt a una carpeta `documentos/`, las imágenes .jpg, .jpeg, .png a `imagenes/`, y los videos .mp4, .mkv a `videos/`.

2. **Clasificación de archivos por fecha**

Este ejemplo muestra mover archivos según su fecha de modificación.
Imagina que tienes la carpeta `descargas` con archivos de diferentes años, y deseas moverlos a distintas carpetas por año.

```python
# La ruta de la carpeta elegida (descargas)
RUTA = ~/Descargas
# Teniendo en la carpeta:
Foto2022.png
Documento2024.png
Video2021.mp4

# Ejecutar la clasificación por extensión en la carpeta "descargas"
clasificador_por_fecha(RUTA)
```
Este script moverá el archivo `Foto2022.png` a una carpeta `2022/`, el archivo `Documento2024.png` a una carpeta `2024/`, y `Video2021.mp4` a `2021/`.

3. **Clasificación por nombre**

Este ejemplo muestra cómo configurarlo para mover archivos según su nombre. Puedes modificar los patrones en el archivo `config.py` para ajustarlas a tus necesidades.
Imagina que tienes la carpeta `descargas` con archivos de diferentes nombres, y deseas mover diferentes tipos de archivos a distintas carpetas personalizadas.

```python
# La ruta de la carpeta elegida (descargas)
RUTA = ~/Descargas

#Archivos:
ejercicio01.sql
ejercicio02.py
examen-de-mates.pdf

"""
Diccionario de patrones (expresiones regulares simples) para clasificar por nombre
Clave = nombre de la subcarpeta destino
Valor = patrón que debe coincidir con el nombre del archivo (sin extensión)
"""
PATRONES = {
    "ejercicios": "ej",
    "examenes" : "examen"
}

# Ejecutar la clasificación por extensión en la carpeta "descargas"
clasificador_por_patron(RUTA)
```
Este script moverá los archivos que contengan "ej" a una carpeta `ejercicios/` y los archivos que contengan examen a una carpeta `examenes/`.

## Instrucciones

Estas instrucciones te guiarán paso a paso para configurar el clasificador de archivos para poder ejecutarlo correctamente.

Para ejecutarlo manualmente:

* En Windows: En una terminal ejecutar ```python main.py```
* En Linux/macOS: En una terminal ejecutar ```python3 main.py```

Para ejecutarlo automáticamente puedes seguir esta [GUIA](https://github.com/danielmi5/Digitalizacion-PROY2-OrdinaX/blob/main/GUIA), creada para mostrar los pasos para configurarlo en diferentes sistemas operativos.

## Tecnologías Utilizadas  

**Lenguaje:**  
- Python  

**IDE:**  
- PyCharm  

**Bibliotecas:**  
- `os` → Manejo del sistema de archivos.  
- `shutil` → Movimientos y copias de archivos.  
- `logging` → Registro de eventos y errores.  
- `datetime, time, re` → Manejo de fechas, hora y expresiones regulares. 
- `watchdog` → Detección de cambios en archivos en tiempo real.


## Contribuciones

¡Las contribuciones son muy bienvenidas! Ya sea para mejorar el código, proponer nuevas funciones o mejorar la documentación.

Consulta el archivo [CONTRIBUTING.md](https://github.com/danielmi5/Digitalizacion-PROY2-OrdinaX/blob/main/CONTRIBUTING) para conocer como puedes contribuir al proyecto.

## Posibles Mejoras Futuras  
- **Soporte para almacenamiento en la nube**.
- **Implementar una interfaz gráfica**.
- **Integración con bases de datos** para un historial más robusto.  
- **Compatibilidad con más formatos y sistemas operativos**.


## Licencia
Este proyecto se publica bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente, incluso para fines comerciales.
