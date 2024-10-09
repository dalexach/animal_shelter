# Frontend del Refugio de Animales

Este es el frontend para la aplicación del Refugio de Animales, desarrollado con Vue.js.

## Requisitos previos

- Node.js (versión 14 o superior)
- npm (viene con Node.js)

## Configuración del proyecto

1. Clona este repositorio:

```
git clone https://github.com/dalexach/animal_shelter.git
cd frontend
```

2. Instala las dependencias:

```
npm install
```

3. Configura las variables de entorno:
   Crea un archivo `.env` en el directorio raíz y añade la siguiente variable:

```
VUE_APP_API_URL=[http://localhost:8000/api](http://localhost:8000/api)
```

## Compilar y ejecutar para desarrollo

```
npm run serve

La aplicación estará disponible en `http://localhost:8080`.

```

## Compilar y minificar para producción

```
npm run build
```

## Personalizar configuración

Consulta [Configuration Reference](https://cli.vuejs.org/config/) para más información sobre la configuración de Vue CLI.
