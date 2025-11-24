# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import task_router
import time
from datetime import datetime
import uvicorn

app = FastAPI(
    title="API REST Básica de Tareas",
    version="1.0.0",
    description="API para gestión de tareas (CRUD en memoria)"
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

START_TIME = time.time()

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "uptime": time.time() - START_TIME,
        "timestamp": datetime.now().isoformat()
    }

app.include_router(task_router.router)

if __name__ == "__main__":
    # Configuración para iniciar el servidor en el puerto 3027
    print("Iniciando servidor")
    uvicorn.run(app, host="0.0.0.0", port=3027)

