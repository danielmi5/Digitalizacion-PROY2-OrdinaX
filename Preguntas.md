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

Optimizaría la gestión de documentos en entornos industriales y empresariales, reduciendo el tiempo dedicado a la organización manual y minimizando errores. Aspectos que mejoraría:

  + Optimización del flujo de trabajo: Organiza automáticamente documentos administrativos, contratos, facturas y reportes, evitando la pérdida de archivos importantes.

  + Automatización de procesos administrativos: Clasificación automática de archivos contables, registros de clientes y reportes de ventas.

  + Organización automática de archivos generados por sensores IoT y sistemas de monitoreo.

  + Historial de mantenimiento y auditoría: Clasifica reportes por fecha, permitiendo un acceso rápido y ordenado a documentos de mantenimiento.



- ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?

Automátizaría la gestión de los archivos que se generan y reduciría los errores. Además, mejoraría en auditorías, ya que permite clasificar archivos por fechas, lo que ayuda a encontrar registros e información más rapido. Con menos tiempo en tener que organizar los datos, mñas tiempo se tiene a realizar otras tareas.



- Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?

El software se podría modificar y optimizar para otros entornos, según los datos que se manejan. Por ejemplo, mediante el archivo de configuración se podrían modificar los tipos de archivos, para especificarlos al sentido de ese sector. O modificar las funcionalidades para que clasifique de otra manera según el negocio o lo que se pida.



### Mejoras en IT y OT (2f):

- ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

Puede actuar como un puente entre IT y OT al facilitar la gestión y organización de datos generados en ambos entornos. Algunas maneras en que puede mejorar esta integración incluyen:

    + Automatización del manejo de archivos en sistemas mixtos: En entornos industriales, los dispositivos OT generan archivos de registro, reportes de mantenimiento y datos operativos. Al clasificar estos archivos de manera automática, facilita a los sistemas IT el análisis y monitoreo de estos datos.

    + Mejora de la trazabilidad y auditoría de datos: El software ya incluye un archivo de log, lo que permite rastrear qué archivos fueron organizados, cuándo y dónde, facilitando la auditoría de procesos.



- ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?

La principal de la que se encarga, que es la gestión de archivos en servidores IT. También en el momitoreo y almacenamiento de datos de sensores OT. Por último, ayuda a automatizar los archivos en equipos compartidos: en entornos con múltiples usuarios (como en una oficina), los equipos se llenan de archivos y generalmente desordenados. Reduciría el tiempo en el que estos usuarios estarían buscando archivos concretos.



- Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

Podría incluir:

  + Integración con bases de datos: Puede ser modificado para enviar archivos organizados a una base de datos.

  + Integración en la nube: Además de con una base de datos, podrían almacenarse en plataformas en la nube como Google Drive o OneDrive.

### Tecnologías Habilitadoras Digitales (2g):

- ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto? ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software? Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?



Actualmente, el software usa tecnologías básicas como:

  + Automatización de procesos: Mediante Python, se logra la clasificación automática de archivos.

  + Gestión de archivos y registros: Se utilizan módulos como os, shutil, re y datetime para organizar, mover y registrar archivos de manera eficiente.



Sin embargo, se pueden integrar más tecnologías para mejorar su alcance, como:

  + Inteligencia Artificial: Se podría usar IA para analizar patrones en los archivos y mejorar la clasificación automática, esto permitiría mayor automatización y precisión.

  + Machine Learning: Modelos de ML podrían identificar archivos duplicados o predecir la categoría de documentos no reconocidos.

  + Computación en la nube: Integrar almancenamiento en la nube para poder acceder desde cualquier lugar y permitiría colaboración en la nube.

  + Integrar ciberseguridad mediante control de accesos: Agregar autenticación y permisos para que solo usuarios autorizados puedan mover ciertos archivos. Ayudaría a prevenir cambios no autorizados.
