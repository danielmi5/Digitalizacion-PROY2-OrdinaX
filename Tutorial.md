# Tutorial: Ejecutar el Script

Este tutorial te guiará paso a paso para configurar el clasificador de archivos para poder ejecutarlo.

## Requisitos

*   Tener Python instalado.
*   Tener los archivos `config.py` y `main.py` en una carpeta de tu elección.
*   Configura el archivo `config.py` antes de ejecutar el script.

## Guía para ejecutarlo manualmente

En una terminal ejecutar 
```python main.py```

## Pasos para que el script sea automático mediante el programador de tareas (Windows)

1.  **Abrir el Programador de Tareas:**
    *   Busca "Programador de tareas" en el menú de inicio.
    *   Ábrelo. En el panel derecho, haz clic en "Crear tarea básica...".
    *   Dale un nombre a la tarea (por ejemplo, "Clasificador automático").
    *   Haz clic en "Siguiente".
    *   Selecciona el desencadenador que prefieras. Configura la frecuencia y la hora de inicio según tu elección.
    *   Haz clic en "Siguiente". Selecciona "Iniciar un programa".
    *   En "Programa/script", escribe `python`. Y en "Agregar argumentos", escribe la ruta completa al archivo `main.py`.
    *   En "Programa/script", escribe `python`.
    *   En "Agregar argumentos", escribe la ruta completa al archivo `main.py`. Y En "Iniciar en", escribe la ruta completa al directorio donde está `main.py`. Esto ayuda a asegurar que el script pueda encontrar el archivo de configuración y otros recursos.
    *   Revisa la configuración de la tarea. Asegúrate de que todo sea correcto y haz clic en "Finalizar".

## Consideraciones Adicionales

*   **Permisos:** Asegúrate de que la cuenta de usuario bajo la cual se ejecuta la tarea tenga los permisos necesarios para leer y escribir en el directorio que se está clasificando.
*   **Depuración:** Si la tarea no se ejecuta correctamente, revisa el historial de la tarea en el Programador de Tareas para ver si hay errores.  También puedes revisar el archivo de registro especificado en `config.py` para obtener más detalles.
*   **Archivo `config.py`:** Verifica que el archivo `config.py` esté configurado correctamente antes de ejecutar el script.
*   **Deshabilitar `CLASIFICAR_AUTOMATICO`:** Asegúrate de que la variable `CLASIFICAR_AUTOMATICO` en el archivo `config.py` esté establecida en `False`.  De lo contrario, el script intentará ejecutarse automáticamente *además* de la tarea programada, lo que puede causar problemas.
