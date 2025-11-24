
from typing import List, Dict, Optional

# Usaremos la lista memo para almacenar las tareas sin usar una DB
memo: List[Dict] = []
_last_id = 0

def get_all_tasks() -> List[Dict]:
    return memo

def get_task_by_id(task_id: int) -> Optional[Dict]:
    for task in memo:
        if task["id"] == task_id:
            return task
    return None

def insert_task(task_data: Dict) -> Dict:
    global _last_id
    _last_id += 1
    new_task = {
        "id": _last_id,
        "title": task_data["title"],
        "done": task_data.get("done", False)
    }
    memo.append(new_task)
    return new_task

def update_task_data(task_id: int, task_data: Dict) -> Optional[Dict]:
    # Usado para PUT (Reemplazo completo)
    task = get_task_by_id(task_id)
    if task:
        task["title"] = task_data["title"]
        task["done"] = task_data["done"]
        return task
    return None

def patch_task_data(task_id: int, task_data: Dict) -> Optional[Dict]:
    # Usado para PATCH (Actualización parcial)
    task = get_task_by_id(task_id)
    if task:
        if "title" in task_data and task_data["title"] is not None:
            task["title"] = task_data["title"]
        if "done" in task_data and task_data["done"] is not None:
            task["done"] = task_data["done"]
        return task
    return None

def remove_task_data(task_id: int) -> bool:
    task = get_task_by_id(task_id)
    if task:
        memo.remove(task)
        return True
    return False
