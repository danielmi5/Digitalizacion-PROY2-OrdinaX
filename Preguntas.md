# PREGUNTAS PROYECTO

### Ciclo de vida del dato (5b):
- ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?

Los archivos se generan de forma externa, por los usuarios o aplicaciones, y son depositados en una carpeta de origen que se especifica en la configuración del proyecto (config.RUTA_ORIGEN). El ciclo comienza cuando estos archivos están disponibles en el sistema de archivos del sistema operativo.

Una vez que los archivos están disponibles, el programa toma estos archivos y los clasifica en diferentes carpetas según las reglas definidas en el archivo de configuración (config.TIPOS_DE_ARCHIVOS, config.PATRONES, etc.). Este proceso puede incluir la clasificación por tipo de archivo, por fecha de modificación, o por coincidencia de un patrón en el nombre del archivo.

Después de clasificar los archivos, el programa los mueve a carpetas organizadas en función de las reglas mencionadas. Esto implica la creación de nuevas carpetas, si es necesario, y el traslado de archivos a su respectiva ubicación. Y por último, en cuanto a la eliminación, el proyecto no implementa una funcionalidad para la eliminación de archivo actualmente.
- ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?

Cuando se mueve un archivo, el proceso está diseñado para controlar los posibles fallos. Por ejemplo, si se mueve un archivo de una carpeta a otra, se asegura de que la carpeta destino exista antes de realizar el movimiento. Esto se realiza con una verificación que crea la carpeta si no existe (os.makedirs(destino)), lo que reduce el riesgo de que el archivo se pierda por falta de destino.
Además, el programa mantiene un archivo de log (registro_actividad.txt) que registra todos los movimientos y eventos que se producen en el proceso. Esto ayuda a controlar y rastrear el ciclo de vida de cada archivo, asegurando que se pueda identificar cualquier problema o inconsistencia en el proceso de clasificación y movimiento de los archivos.
- Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?

Para un futuro, hacer un seguimiento más detallado de los archivos (como registrar más información sobre cada archivo, como quién lo creó, cuándo fue modificado por última vez, etc.), se podría usar una base de datos para almacenar estos metadatos. Además, se podría implementar la eliminación de archivos antiguos o archivarlos después de cierto período de tiempo para gestionar el almacenamiento de manera eficiente. 

### Almacenamiento en la nube (5f):
- Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?
- ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?
- Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?
### Seguridad y regulación (5i):
- ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?
- ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?
- Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?
### Implicación de las THD en negocio y planta (2e):
- ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?
- ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?
- Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?
### Mejoras en IT y OT (2f):
- ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?
- ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?
- Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?
### Tecnologías Habilitadoras Digitales (2g):
- ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?
- ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?
- Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?
