**Alumno: Carlos Toledano Delgado**
### EJERCICIOS TEMA 2

**EJERCICIO 1: Descargar y ejecutar las pruebas de alguno de los proyectos anteriores, y si sale todo bien, hacer un pull request a este proyecto con tests adicionales, si es que faltan (en el momento que se lea este tema).**

Primero realizamos un fork del repositorio para compartirlo y segundo, realizamos un clonado del repositorio.

He añadido el siguiente test:

![1](https://github.com/carlillostole/Ejercicios-IV/blob/master/TEMA2/capturas/test1.png?raw=true)


**EJERCICIO 2: Para la aplicación que se está haciendo, escribir una serie de aserciones y probar que efectivamente no fallan. Añadir tests para una nueva funcionalidad, probar que falla y escribir el código para que no lo haga (vamos, lo que viene siendo TDD).**

Este ejercicio ya está realizado en mi proyecto como parte de los test que hay que hacer.

**EJERCICIO 3: Convertir los tests unitarios anteriores con assert a programas de test y ejecutarlos desde mocha, usando descripciones del test y del grupo de test de forma correcta. Si hasta ahora no has subido el código que has venido realizando a GitHub, es el momento de hacerlo, porque lo vas a necesitar un poco más adelante.**

Para poder convertir los test unitarios con assert y poder ejercutarlos desde Mocha he instalado la versión Pocha mediante pip.

__$ pip install pocha__

![2](https://github.com/carlillostole/Ejercicios-IV/blob/master/TEMA2/capturas/testej4.png?raw=true)

**EJERCICIO 4: Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).**

Como mi proyecto lo estoy realizando en Python he optado por el entorno virtual virtualenv.

La instalación se lleva a cabo con la siguiente orden:

__$ sudo apt-get install python-virtualenv__

Una vez instalado creamos el directorio en el cual queremos ejecutar el entorno virtual:

__$ virtualenv EntornoVirtualIV__

Ya está creado el entorno virtual, nos vamos a él e introducimos lo siguiente por terminal para iniciarlo:

__$ source bin/activate__

Por último, si queremos detenerlo:

__$ desactivate__

**EJERCICIO 5: Como ejercicio, algo ligeramente diferente: una web para calificar las empresas en las que hacen prácticas los alumnos. Las acciones serían: Crear empresa, Listar calificaciones para cada empresa, crear calificación y añadirla (comprobando que la persona no la haya añadido ya), borrar calificación (si se arrepiente o te denuncia la empresa o algo), Hacer un ránking de empresas por calificación, por ejemplo, Crear un repositorio en GitHub para la librería y crear un pequeño programa que use algunas de sus funcionalidades. Si se quiere hacer con cualquier otra aplicación, también es válido. Se trata de hacer una aplicación simple que se pueda hacer rápidamente con un generador de aplicaciones como los que incluyen diferentes marcos MVC. Si cuesta mucho trabajo, simplemente prepara una aplicación que puedas usar más adelante en el resto de los ejercicios.**

Para la aplicación he usado Django.
La aplicación se encuentra en este [repositorio](https://github.com/carlillostole/Ejercicio_EmpresaIV1718)


**EJERCICIO 6: Ejecutar el programa en diferentes versiones del lenguaje. ¿Funciona en todas ellas?**

Lo he probado tanto en python versión 2.7 como en la versión python 3, y funciona sin problemas en ambas.

**EJERCICIO 7: Crear una descripción del módulo usando package.json. En caso de que se trate de otro lenguaje, usar el método correspondiente.**

Como he usado python para la aplicación necesito tener el setup.py, que es el equivalente. Uso pip freeze para obtener las dependencias y nos queda:

![3](https://github.com/carlillostole/Ejercicios-IV/blob/master/TEMA2/capturas/setup.png?raw=true)

**EJERCICIO 8: Automatizar con grunt, gulp u otra herramienta de gestión de tareas en Node la generación de documentación de la librería que se cree usando docco u otro sistema similar de generación de documentación. Previamente, por supuesto, habrá que documentar tal librería.**

Para generar la documentación en python podemos usar epydoc. Bastaría con hacer $ epydoc nombre_paquete. Se nos creará un directorio html, en el que se encuentra la documentación generada automáticamente

**EJERCICIO 8: Haced los dos primeros pasos antes de pasar al tercero.**

Defino un fichero .travis.yml. El contenido es el siguiente:

![4](https://github.com/carlillostole/Ejercicios-IV/blob/master/TEMA2/capturas/travis.png?raw=true)

Travis sincroniza automáticamente cada cambio realizado en el repositorio y comprueba que sea correcto.
