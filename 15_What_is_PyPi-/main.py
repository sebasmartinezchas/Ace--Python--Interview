"""
15 . What is Pypi

Python viene con muchos modulos nativos, pero cuando necesitamos un modulo externo, vamos a Pypi, que es Python Package Index.

Si no usas Pipy en tus proyectos probablemente estas haciendo algo mal o trabajando de mas.

Al momento de grabación de esta clase, año 2019, la cantidad de modulos superaba los 200.000.

Se hace pip install nombre_proyecto y ya lo tendré disponible para usar en mi entorno actual

¿ Como sabemos si un paquete es digno de confianza?

Vamos a ver su web en github, cantidad de instalaciones, quienes contribuyen, versiones, etc.

Siempre hay que tener un poco de cuidado porque existe la posibilidad de que alguién haya subido algún virus,
no es algo muy común si se tienen las precauciones antes descriptas pero cada tanto pasa.

Otro punto a considerar es el tipo de licencia, normalmente es MIT.

Lo que hace normalmente Lerner es ir a awesome-python.com un sitio muy conocido y debería ser un primer filtro-

El nombre. Se escribe PyPI (Python Package Index). En el texto aparece "Pypi" y también "Pipy".
"Lo tendré disponible en mi entorno actual". No necesariamente: pip install instala en el intérprete al que pertenece ese pip, que puede no ser el que usa tu proyecto. La documentación oficial recomienda python -m pip install ... para estar seguro de qué Python lo recibe, y trabajar dentro de un entorno virtual (Installing Python Modules, venv).
"No es algo muy común". Hoy esa afirmación se queda corta. Hay campañas repetidas de typosquatting: paquetes maliciosos con nombres casi iguales a los de librerías populares. En marzo de 2024 hubo una tan grande que PyPI suspendió brevemente el registro de usuarios nuevos tras una ola de proyectos maliciosos subidos como parte de una campaña de typosquatting, con más de 500 variantes de proyectos auténticos y el código malicioso dentro del setup.py. Y sigue pasando este año: en enero de 2026 se publicó sympy-dev, que acumuló más de 1.000 descargas en su primer día. Para tus apuntes, la precaución más concreta es revisar bien el nombre exacto antes del pip install. Mirar las estrellas de GitHub ayuda menos.
#1 Trusted Cybersecurity News Platform
 +2

"""
