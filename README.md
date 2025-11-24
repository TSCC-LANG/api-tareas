# API REST de Tareas

Esta API REST implementa un sistema básico de gestión de tareas ("ToDo List") utilizando **FastAPI**. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre recursos de tareas.

**Características principales:**
* **Almacenamiento en Memoria:** No requiere instalación de bases de datos (MySQL/PostgreSQL). Los datos se guardan temporalmente en una lista en el servidor mientras este se encuentre activo.
* **Arquitectura Modular:** Organizada internamente en capas (Routers, Services, Models) para facilitar el mantenimiento.
* **Documentación Automática:** Incluye interfaz interactiva con Swagger UI.

## Funcionalidad Disponible

La API expone los siguientes endpoints para administrar las tareas:

* **Listar tareas:** `GET /tasks` - Obtiene todas las tareas registradas.
* **Obtener tarea:** `GET /tasks/{id}` - Busca una tarea específica por su ID.
* **Crear tarea:** `POST /tasks` - Agrega una nueva tarea (requiere título).
* **Actualizar completa:** `PUT /tasks/{id}` - Reemplaza toda la información de una tarea.
* **Actualizar parcial:** `PATCH /tasks/{id}` - Modifica solo ciertos campos (ej. marcar como terminada).
* **Eliminar:** `DELETE /tasks/{id}` - Borra una tarea del sistema.
* **Estado del servicio:** `GET /health` - Muestra el tiempo de actividad (uptime) y estado del servidor.

## Guía de Ejecución

Sigue estos pasos para poner en marcha el servidor en el puerto **3027**.

### 1. Preparar el entorno

Es recomendable crear un entorno virtual de Python:

```bash
python3 -m venv venv
source venv/bin/activate 
```

2. Instalar dependencias

```bash
pip install fastapi uvicorn 
```

3. Iniciar el servidor
El archivo principal ya está configurado para usar el puerto 3027 automáticamente. Ejecuta el siguiente comando:

```bash
python main.py
```
(Alternativamente, se puede usar uvicorn main:app --host 0.0.0.0 --port 3027).

Cómo probar los servicios
Una vez que el servidor esté corriendo ("Application startup complete"), puedes probar la API de las siguientes formas:

1. Documentación Interactiva (Swagger UI) Ingresa a la siguiente URL en tu navegador para probar los endpoints directamente sin escribir código:

http://jquiroz:3027/docs

2. Verificación de Estado Para comprobar que el sistema está operativo:

http://jquiroz:3027/health
