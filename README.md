# viajes-frontend

¡Bienvenido al sitio Volar por el mundo! Este proyecto te ofrece una experiencia interactiva relacionada con el fascinante mundo de los viajes. El proyecto es la primera entrega para el curso Full Stack Python organizado por Codo a codo 4.0.

## Elementos a entregar

[Link al Desploy en Github](https://agustinsalum.github.io/viajes.github.io/)

[Link al Repositorio de Github](https://github.com/agustinsalum/viajes.github.io)

## Cómo ejecutar la página

1. Clonamos el repositorio

```
git git@github.com:agustinsalum/viajes.github.io.git
```

2. Accedemos a la carpeta clonada:

```
cd viajes-frontend
```

3. Puedes ejecutar la página de dos maneras:

### Opción 1: Haciendo clic derecho en `index.html`
Simplemente haz clic derecho en el archivo `index.html` y selecciona "Abrir con tu navegador favorito". Esto abrirá la página en tu navegador predeterminado.

### Opción 2: Usando Live Server
Si prefieres una experiencia más dinámica durante el desarrollo, puedes instalar la extensión Live Server en tu editor de código favorito. Luego, simplemente haz clic en "Go Live" desde tu editor y se abrirá automáticamente la página en tu navegador.

¡Disfruta explorando el mundo de los viajes en nuestro sitio!

# viajes-backend

# Trabajo Integrador Final

## Objetivo

El objetivo de este trabajo práctico es desarrollar una aplicación web que utilice una API REST (ideal) o el modelo MVT en el backend y un frontend interactivo para realizar operaciones CRUD en una base de datos MySQL.

## Instrucciones

### Parte 1: Back-end, Construyendo una API RESTful con Python, Django y MySQL

1. Utilizando Python, Django y MySQL, deberás crear una API REST o utilizar el modelo MVT de Django que cumpla con los siguientes requisitos:
   - Implementar el protocolo HTTP y los métodos GET, POST, PUT y DELETE.
   - Utilizar formato JSON para enviar y recibir datos desde la base de datos.
   - La API deberá permitir la creación, lectura, actualización y eliminación de registros en la base de datos.

2. Sigue los pasos del tutorial para el Back que encontrarás en el siguiente enlace: [Repositorio de Backend](https://github.com/andru-oca/Django-Backend-Inicial).

3. Sube el backend a un hosting que permita correr Python y Django, por ejemplo, PythonAnyWhere. Encuentra instrucciones en el siguiente tutorial: [Despliegue del backend](https://github.com/andru-oca/Django-Backend-Inicial/tree/main/3_django-tercera-parte-deploy).

4. Documentación del repositorio del backend, junto con la información del frontend.

### Parte 2: Front-end, Creando un CRUD con HTML, CSS, Bootstrap, JavaScript y Vue

1. Deberás crear un CRUD (Create, Read, Update, Delete) que interactúe con la API REST que has desarrollado en el backend. Utiliza las siguientes tecnologías:
   - HTML, CSS y Bootstrap para la estructura y diseño de la interfaz.
   - JavaScript y Vue.js para la interacción con la API REST y la manipulación de los datos.
   - Thunder Client, POSTMAN o una herramienta similar para testear la API y asegurarte de su correcto funcionamiento (opcional).

2. Sigue los pasos del tutorial para el Front que encontrarás en el siguiente enlace: [Tutorial de Frontend](URL_DEL_TUTORIAL_DEL_FRONTEND).

3. Sube el frontend a un hosting, por ejemplo, Netlify o GitHub Pages, siempre y cuando se realice en forma de microservicios.

# Uso del Proyecto y Visualización del Despliegue (desploy)

El trabajo final ha sido completado y se ha subido a la página pythonanywhere.com para su despliegue en producción. A continuación, se detallarán los pasos para ejecutar el proyecto de manera local y se proporcionará un ejemplo de cómo desplegarlo en modo producción, junto con el enlace al despliegue.

## Visualización

Puedes acceder al proyecto desplegado en [este enlace](https://agustinsalum.pythonanywhere.com/).

## Ejecución Local

1. Clona el repositorio:

    ```
    git clone https://github.com/agustinsalum/flying-around-the-world
    ```

2. Accede a la carpeta del proyecto:

    ```
    cd flying-around-the-world
    ```

3. Crea y activa un entorno virtual llamado venv:

    ```
    pip install virtualenv
    ```
    ```
    virtualenv -p python venv
    ```
    ```
    source venv/bin/activate
    ```

4. Instala las dependencias necesarias:

    ```
    pip install -r requirements.txt
    ```

5. Crea un archivo llamado `.env` junto a tu archivo `settings.py`

   ```
   touch .env
   ```

6. Copia el siguiente modelo en tu archivo `.env` e ingresa tus credenciales personales

   ```
   DEBUG=False
   SECRET_KEY=
   DATABASE_NAME=
   DATABASE_USER=
   DATABASE_PASSWORD=
   DATABASE_HOST=
   DATABASE_PORT=
   ```

7. Realiza las migraciones:

    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```

8. Ejecuta el proyecto:

    ```
    python manage.py runserver
    ```

Estos pasos te permitirán ejecutar el proyecto en tu entorno local. Asegúrate de tener Python y pip instalados en tu sistema antes de comenzar.

## Python any where

PythonAnywhere es una plataforma en la nube que ofrece entornos de desarrollo y alojamiento web para aplicaciones escritas en Python. Se debera crear una cuenta y generar una api token, el mismo se encuentra en su perfil con el nombre "API TOKEN". Luego,  

# Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi correo electronico

