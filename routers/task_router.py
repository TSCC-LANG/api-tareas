from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

class TaskBase(BaseModel):
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: str
    done: bool = False

class TaskUpdate(BaseModel):
    title: str
    done: bool

class TaskPatch(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

class TaskOut(BaseModel):
    id: int
    title: str
    done: bool

# Endpoints

@router.get("/", response_model=List[TaskOut])
def get_tasks():
    return task_service.list_tasks()

@router.get("/{id}", response_model=TaskOut)
def get_task(id: int):
    try:
        return task_service.get_task(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # Convertimos a dict para pasar al servicio
    return task_service.create_task(task.dict())

@router.put("/{id}", response_model=TaskOut)
def update_task(id: int, task: TaskUpdate):
    try:
        return task_service.update_task(id, task.dict())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id}", response_model=TaskOut)
def patch_task(id: int, task: TaskPatch):
    try:
        # solo envía lo que cambió
        return task_service.partial_update_task(id, task.dict(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    try:
        task_service.delete_task(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
