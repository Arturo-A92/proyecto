<h1> Proyecto final </h1>

<h2>realizado por: Arturo Alfonzo</h2>

Este proyecto tiene como objetivo crear un blog como proyecto final de curso.
Cosas que puedes hacer:

- Crear, leer, actualizar, Buscar y eliminar blogs.
- sistema de loggin y creacion de usuarios.

# Instalar

Para instalar este software necesitas hacer:

## Comprobar la versión de Python
Este proyecto se escribió con python 3.9.12, por lo que le sugiero que pruebe con esta versión o superior para no tener problemas de compatibilidad.

Cómo verifico mi versión de python,

en sistemas *nix:

```bash
> python --versión
> Python 3.8.0
```

en ventanas:

```bash
c:\> py --versión
c:\> Python 3.8.0
```

## Instalar dependencias

Para instalar dependencias necesitas ejecutar `pip install`, asegúrate de estar en la carpeta del proyecto y puedes ver cuando haces `ls` o `dir`:

```bash
> pip install django
```
Este último devolverá un montón de cosas en la terminal.

`Algunos sistemas operativos requerirán que uses pip3 en lugar de pip`

para este trabajo se utilizo la version (4, 0, 6) de Django 

## Configuración de la aplicación Django

Una vez que termine la instalación de las dependencias, debe ejecutar algunos comandos Django.

### Migraciones

Inicializar la base de datos
*nada:
```bash
> python manage.py migrate
```
ventanas:
```bash
c:\> py administrar.py migrate
```

### Ejecutar el servidor de prueba

```bash
> python mananage.py runserver
```
ventanas:
```bash
c:\> py manage.py runserver
```
Ir a localhost:8000/

para tener acceso a la aplicación.

Si todo va bien, debería poder abrir el navegador y ver cómo se ejecuta la aplicación.