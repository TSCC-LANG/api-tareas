
from typing import List, Dict
from models.task_model import (
    get_all_tasks,
    get_task_by_id,
    insert_task,
    update_task_data,
    patch_task_data,
    remove_task_data
)

def list_tasks() -> List[Dict]:
    return get_all_tasks()

def get_task(task_id: int) -> Dict:
    task = get_task_by_id(task_id)
    if not task:
        raise ValueError("Tarea no encontrada")
    return task

def create_task(data: Dict) -> Dict:
    if not data.get("title"):
        raise ValueError("El título es obligatorio")
    return insert_task(data)

def update_task(task_id: int, data: Dict) -> Dict:
    updated = update_task_data(task_id, data)
    if not updated:
        raise ValueError("Tarea no encontrada")
    return updated

def partial_update_task(task_id: int, data: Dict) -> Dict:
    updated = patch_task_data(task_id, data)
    if not updated:
        raise ValueError("Tarea no encontrada")
    return updated

def delete_task(task_id: int) -> None:
    success = remove_task_data(task_id)
    if not success:
        raise ValueError("Tarea no encontrada")
