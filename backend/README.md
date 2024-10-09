# Backend del Refugio de Animales

Este es el backend para la aplicación del Refugio de Animales, desarrollado con Django.

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- virtualenv (recomendado)

## Configuración del entorno

1. Clona este repositorio:

```
git clone https://github.com/dalexach/animal_shelter.git
cd backend
```

2. Crea un entorno virtual:

```
python -m venv venv
```

3. Activa el entorno virtual:

- En Windows:

```
venv\Scripts\activate
```

- En macOS y Linux:

```
source venv/bin/activate
```

4. Instala las dependencias:

```
pip install -r requirements.txt
```

5. Configura las variables de entorno:
   Crea un archivo `.env` en el directorio raíz y añade las siguientes variables:

```
DEBUG=True
SECRET_KEY=tu_clave_secreta
DATABASE_URL=tu_url_de_base_de_datos
```

## Ejecutar migraciones

Ten en cuenta que debes tener creada la base de datos en local y corriendo en background.

```
python manage.py migrate
```

## Crear un superusuario (opcional)

```
python manage.py createsuperuser
```

## Ejecutar el servidor de desarrollo

```
El servidor estará disponible en `http://localhost:8000`.

```

## Creación de usuario desde consola en el servidor

Para crear un usuario por consola:

```
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
User = get_user_model()
nuevo_superusuario = User.objects.create(
    username='margarita',
    email='margarita@example.com',
    password=make_password('Margarita123'),
    is_active=True,
    is_staff=False,
    is_superuser=False
)
```
