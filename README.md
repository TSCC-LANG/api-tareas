# API REST de Tareas (FastAPI + Arquitectura por Capas)

Esta API REST implementa un CRUD básico de tareas ("tasks") utilizando FastAPI, con una arquitectura organizada en tres capas principales:

1. Routers (Controladores / Endpoints HTTP)
2. Services (Lógica de negocio)
3. Models (Acceso a datos en memoria)

A diferencia del ejemplo de referencia, este proyecto **no utiliza base de datos**. Los datos se almacenan en una lista en memoria (`memo`) para cumplir con los requisitos de la práctica.

## Descripción de Componentes

- **main.py**: Punto de entrada de la aplicación. Inicializa FastAPI, configura CORS y define el endpoint de sistema `/health`.
- **routers/**: Define los endpoints HTTP que exponen la funcionalidad de la API.
    - `task_router.py`
- **services/**: Implementa la lógica de negocio, separando responsabilidades del controlador.
    - `task_service.py`
- **models/**: Simula la persistencia de datos utilizando una lista en memoria.
    - `task_model.py`

## Routers (Controladores / Vistas HTTP)

**Responsabilidades:**
- Definir endpoints (GET, POST, PUT, PATCH, DELETE).
- Recibir solicitudes HTTP (req).
- Devolver respuestas HTTP (res) con códigos apropiados (200, 201, 204, 404).
- Validar el formato de entrada usando esquemas Pydantic (`TaskCreate`, `TaskUpdate`, etc.).
- Llaman a los servicios.
- **No contienen lógica de negocio.**

```python
@router.post("/", response_model=TaskOut, status_code=201)
def create_task(task: TaskCreate):
    return task_service.create_task(task.dict())
