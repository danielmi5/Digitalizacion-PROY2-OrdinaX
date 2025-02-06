# Sistema de Organización Automática de Archivos - OrdinaX

## Descripción General  
El proyecto consiste en un **sistema de organización automática de archivos**, diseñado para facilitar la gestión y clasificación de documentos dentro de un sistema de directorios.  

El objetivo principal es **automatizar** la tarea de organizar archivos de manera eficiente, permitiendo que estos se **clasifiquen y se muevan** sin intervención manual. Este sistema es ideal para usuarios que manejan grandes volúmenes de archivos y necesitan mantener un orden coherente sin invertir tiempo en tareas repetitivas.  

## Objetivos  
- **Reducir el tiempo y esfuerzo** dedicado a la organización manual de archivos.  
- **Asegurar un almacenamiento estructurado y accesible** para distintos tipos de documentos.  
- **Evitar la pérdida de información** mediante registros de actividad detallados.  
- **Optimizar la productividad**, permitiendo que el usuario se enfoque en tareas más importantes.  

## Características  

### 📂 Clasificación Automática  
El sistema organizará los archivos en base a diferentes criterios, tales como:  
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

### 🖥 Interfaz Gráfica (GUI)  
El sistema contará con una interfaz gráfica sencilla e intuitiva, diseñada con **Tkinter**, que permitirá:  
- Seleccionar carpetas de origen y destino.  
- Configurar las reglas de clasificación.  
- Visualizar el estado del proceso en tiempo real.  

## Tecnologías Utilizadas  

**Lenguaje:**  
- Python  

**IDE:**  
- PyCharm  

**Bibliotecas:**  
- `os` → Manejo del sistema de archivos.  
- `shutil` → Movimientos y copias de archivos.  
- `Tkinter` → Interfaz gráfica.  
- `logging` → Registro de eventos y errores.  
- `watchdog` → Detección de cambios en archivos en tiempo real.  

## Posibles Mejoras Futuras  
- **Soporte para almacenamiento en la nube**.
- **Integración con bases de datos** para un historial más robusto.  
- **Compatibilidad con más formatos y sistemas operativos**.

---
