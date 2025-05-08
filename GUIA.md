# Guía para ejecutar el script automáticamente

Este tutorial te guiará paso a paso para configurar el clasificador de archivos para poder ejecutarlo.

## Pasos para que el script sea automático mediante el programador de tareas (Windows)

* **Abrir el Programador de Tareas:**
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
  
## Pasos para que el script sea automático mediante el programador de tareas `cron` (Linux/macOS)

Estos pasos indican cómo automatizar la ejecución de un script de Python en sistemas Linux o macOS usando el programador de tareas `cron`.

1. Abre una terminal y ejecuta este comando `crontab -e`. Esto abrirá el archivo de tareas programadas

2. Añade la siguiente línea al final del archivo: `0 9 * * * /usr/bin/python3 /ruta/completa/al/main.py`. Puedes configurar cuando se realiza la ejecución cambiando los primeros valores.
	* Descripción del comando:
		* `0 9 * * *`: Ejecuta todos los días a las 9 de la mañana, todos los días del mes (\*), todos los meses(\*) y todos los días de la semana (*). Cambialo a caundo quieras que se ejecute.
		* `/usr/bin/python3`: Ruta completa al intérprete de Python.
		* `/ruta/completa/al/main.py`: Ruta completa al `main.py` que deseas ejecutar.
	* Explicación de `0 9 * * *`:
```
         ┌───────────── minuto (0 - 59)
         │  ┌───────────── hora (0 - 23)
         │  │  ┌───────────── día del mes (1 - 31)
         │  │  │  ┌───────────── mes (1 - 12)
         │  │  │  │  ┌───────────── día de la semana (0 - 7) (domingo es 0 o 7, 1 lunes...)
         │  │  │  │  │
         │  │  │  │  │
         0  9  *  *  * 
```
4. Guarda y cierra el archivo
5. Por si acaso, puedes verificar que la tarea fue añadida correctamente con: `crontab -l`

Con esto ya tendrías todo configurado para que se ejecute el script automáticamente.

## Consideraciones Adicionales

*   **Permisos:** Asegúrate de que tengas los permisos necesarios para leer y escribir en el directorio que se está clasificando.
*   **Depuración:** Si la tarea no se ejecuta correctamente, revisa el historial de la tarea en el Programador de Tareas para ver si hay errores.  También puedes revisar el archivo de registro especificado en `config.py` para obtener más detalles.
*   **Archivo `config.py`:** Verifica que el archivo `config.py` esté configurado correctamente antes de ejecutar el script.
*   **Deshabilitar `CLASIFICAR_AUTOMATICO`:** Asegúrate de que la variable `CLASIFICAR_AUTOMATICO` en el archivo `config.py` esté establecida en `False`.  De lo contrario, el script intentará ejecutarse automáticamente *además* de la tarea programada, lo que puede causar problemas.
