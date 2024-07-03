# Proyecto Autos

Este proyecto es una aplicación web Django para gestionar modelos de autos.

## Configuración

1. Clona este repositorio.

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt

3. Aplica las migraciones de la base de datos:
    python manage.py migrate

4. Inicia el servidor de desarrollo:
    python manage.py runserver

Uso
Página de Inicio: Muestra una lista de todos los modelos de autos registrados.

URL: http://127.0.0.1:8000/
Agregar Marca: Permite agregar una nueva marca de auto.

URL: http://127.0.0.1:8000/agregar_marca/
Agregar Modelo: Permite agregar un nuevo modelo de auto asociado a una marca.

URL: http://127.0.0.1:8000/agregar_modelo/
Buscar Modelos: Permite buscar modelos de autos por nombre de modelo o nombre de marca.

URL: http://127.0.0.1:8000/buscar/