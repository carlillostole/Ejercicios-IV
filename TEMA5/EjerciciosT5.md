**Alumno: Carlos Toledano Delgado**
### EJERCICIOS TEMA 5:  Virtualización completa: uso de máquinas virtuales

**EJERCICIO 1: Instalar los paquetes necesarios para usar KVM. Se pueden seguir estas instrucciones. Ya lo hicimos en el primer tema, pero volver a comprobar si nuestro sistema está preparado para ejecutarlo o hay que conformarse con la paravirtualización.**

Primero tenemos que instalar los paquetes con las órdenes siguientes:

```
sudo apt-get install qemu-kvm libvirt-bin
```

Una vez hecho esto, ejecutamos la orden: sudo kvm-ok y nos devuelve el siguiente mensaje:

```
INFO: Your CPU does not support KVM extensions
KVM acceleration can NOT be used
```
Como lo veíamos en la primera práctica, el resultado es el mismo, por lo que mi sistema no soporta virtualización de KVM.

**EJERCICIO 2: Crear varias máquinas virtuales con algún sistema operativo libre tal como Linux o BSD. Si se quieren distribuciones que ocupen poco espacio con el objetivo principalmente de hacer pruebas se puede usar CoreOS (que sirve como soporte para Docker) GALPon Minino, hecha en Galicia para el mundo, Damn Small Linux, SliTaz (que cabe en 35 megas) y ttylinux (basado en línea de órdenes solo).**

La primera máquina virtual que he creado ha sido con la distribución SliTaz. Para ello, primero nos creamos un disco duro virtual en formato qcow2 con la siguiente orden:

```
qemu-img create -f qcow2 SliTaz.qcow2 200M
```
![1](https://github.com/carlillostole/Ejercicios-IV/blob/master/TEMA5/capturas/1.png?raw=true)

Una vez hecho esto, instalamos el sistema con el fichero de almacenamiento virtual creado y la ISO que nos descargamos de la web de SliTaz.

A continuación, lanzamos el proceso de instalación con la siguiente orden:

```
sudo qemu-system-x86_64 -hda SliTaz.qcow2 -cdrom slitaz-4.0.iso &
```

**EJERCICIO 4: Crear una máquina virtual Linux con 512 megas de RAM y entorno gráfico LXDE a la que se pueda acceder mediante VNC y ssh.**

He elegido Lubuntu ya que viene con LXDE instalado.

Para ello, realizamos los mismo pasos que hicimos en ejercicios anteriores. Primero creamos la partición virtual con el comando:

```
qemu-img create -f qcow2 lubuntu.qcow2 2G
```

Nos descargamos la ISO y la lanzamos con el comando:

```
qemu-system-x86_64 -hda lubuntu.qcow2 -cdrom lubuntu-16.10-desktop-amd64.iso -m 512M
```
Aquí ya le estamos indicando que queremos que use 512M de RAM, con la opción -m.

**EJERCICIO 5: Crear una máquina virtual ubuntu e instalar en ella alguno de los servicios que estamos usando en el proyecto de la asignatura.**

Para el despliegue final del proyecto lo he realizado en Azure utilizando una máquina virtual Ubuntu que contendrá mi aplicación.


**EJERCICIO 5: Instalar una máquina virtual con Linux Mint para el hipervisor que tengas instalado.**

Nos descargamos la ISO de Linux Mint. El hipervisor que voy a utilizar será VirtualBox ya que es el que tengo instalado. Vamos a crear la máquina virtual:

![2](https://github.com/carlillostole/Ejercicios-IV/blob/master/TEMA5/capturas/2.png?raw=true)

Una vez seleccionado, ya podemos ver que se inicia sin ningún problema:

![3](https://github.com/carlillostole/Ejercicios-IV/blob/master/TEMA5/capturas/3.png?raw=true)
