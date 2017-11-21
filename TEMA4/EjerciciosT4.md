**Alumno: Carlos Toledano Delgado**
### EJERCICIOS TEMA 4

**EJERCICIO 1: Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo, disponible tanto en GitHub como en el sitio web está bastante más avanzada; para evitar problemas sobre todo con las herramientas que vamos a ver más adelante, conviene que te instales la última versión y si es posible una igual o mayor a la 1.0.**
Lo he instalado con el siguiente comando:
```
sudo apt install lxc1
```
Y nos queda lo siguiente:

![1](1)
![2](2)

**EJERCICIO 2: Crear y ejecutar un contenedor basado en tu distribución y otro basado en otra distribución, tal como Fedora. Nota En general, crear un contenedor basado en tu distribución y otro basado en otra que no sea la tuya.**

**Mi distribución**
Para crear un contenedor basado en Debian usamos la siguiente orden:

```
sudo lxc-create -t debian -n una-caja-debian
```

Ejecutamos el contenedor con:

```
sudo lxc-start -n una-caja-debian```
```

**Otra distribución: CentOS**
Voy a crear un contenedor CentOS. Para ello, necesito instalar el gestor de paquetes yum:

```
sudo apt-get install yum
```

Una vez hecho esto, creamos el contenedor con la orden:

```
lxc-create -t centos -n centos
```
Tenemos que establecer la contraseña con la siguiente orden:

```
sudo chroot /var/lib/lxc/centos/rootfs passwd
```

Una vez hecho esto, ya podremos iniciar el contenedor:

```
 sudo lxc-start -n centos
```

**EJERCICIO 3: Instalar docker.**

Simplemente tenemos que ejecutar lo siguiente:

```
sudo apt-get installdocker.io
```

Instalamos transport-https con el siguiente comando:
```
 apt-get install apt-transport-https
```
Tenemos que añadir la clave del repositorio Docker:
```
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys CLAVE(sustituir)

```
Faltaría añadir el repositorio a nuestra lista apt y actualizar los repositorios:
```
sh -c "echo deb https://get.docker.com/ubuntu docker main\/etc/apt/sources.list.d/docker.list"
```
Vemos que se ha instalado correctamente:
![3](docker)

**EJERCICIO 4:
1.Instalar a partir de docker una imagen alternativa de Ubuntu y alguna adicional, por ejemplo de CentOS.**
Para instalar una imagen de Ubuntu usamos:
```
sudo docker pull ubuntu
```
![3](dockerubu)

Comprobamos que se ha instalado correctamente con la orden:

```
sudo docker run ubuntu ls
```

![3](dockerinstacorre)

Para instalar CentOs es exactamente igual que lo que acabo de explicar, pero cambiando ubuntu por centos. Sería de la siguiente manera:
```
sudo docker pull centos
```

Comprobamos también que se ha instalado correctamente con la orden:
```
sudo docker run centos ls
```

**2.Buscar e instalar una imagen que incluya MongoDB.**

Similar al apartado anterior. Ejecutamos:
```
sudo docker pull mongo
```
y para ver que se ha instalado correctamente volvemos a hacer:
```
sudo docker run mongo ls
```

Vemos ahora las imágenes que tenemos instaladas y que está todo correcto:

![3](imagesdoc)

**EJERCICIO 5: Crear un usuario propio e instalar alguna aplicación tal como nginx en el contenedor creado de esta forma, usando las órdenes propias del sistema operativo con el que se haya inicializado el contenedor.**

Lanzaremos el contenedor con la orden
```
sudo docker run -i -t ubuntu /bin/bash
```

Ahora debemos crear el usuario y darle permisos de superusuario con las ordenes:

```
useradd -d /home/carlillostole -m carlillostole
passwd carlillostole
adduser carlillostole sudo
```

Una vez hecho esto, haremos login con nuestro usuario y la contraseña que hayamos especificado.

Para instalar nginx simplemente hacemos
```
sudo apt-get install nginx
```
y vemos que funciona con la orden
```
service nginx status
```

**EJERCICIO 6: Crear a partir del contenedor anterior una imagen persistente con commit.**

Primero debemos localizar el id del contenedor. Para ello podemos usar la orden
```
sudo docker ps -a
```
![3](dockerps)

Una vez que ya sabemos el id, podremos realizar el commit con la orden:
```
sudo docker commit cff54f041483 docker-commit
```
![3](commit)

Ahora comprobamos que se ha creado la imagen correctamente:

![3](commitsize)

**EJERCICIO 7: Crear un Dockerfile para el servicio web que se ha venido desarrollando en el proyecto de la asignatura.**

El contenido de mi fichero es el siguiente:
```
# Version sistema operativo
FROM ubuntu:17.10

# Autor
MAINTAINER Carlos Toledano Delgado <carliyostole@gmail.com>

#Actualizar Repositorio
RUN apt-get -y update

#Instalamos python y pip por medio de nuestro Makefile
RUN apt-get install -y python-dev
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

#Instalamos git y descargamos el repositorio
RUN apt-get install -y git
RUN git clone https://github.com/carlillostole/proyectoIV17-18

# Instalacion de las dependencias del proyecto
RUN cd proyectoIV17-18/ && make install

EXPOSE 8000
WORKDIR proyectoIV17-18/
CMD gunicorn app:app --log-file=- --bind 0.0.0.0:8000
```

**EJERCICIO 8:Desplegar un contenedor en alguno de estos servicios, de prueba gratuita o gratuitos.**
Desplegado en DockerHub:
[Contenedor DockerHub](https://hub.docker.com/r/carlillostole/proyectoiv17-18/)
Desplegado en Azure:
[Contenedor Azure](http://proyectoiv1718.azurewebsites.net/)
