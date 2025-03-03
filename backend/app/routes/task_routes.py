from fastapi import APIRouter, HTTPException
from app.services.task_service import create_task, get_tasks, get_task_by_id, update_task, delete_task
from app.models.schemas import Task, TaskInResponse

router = APIRouter()

@router.post("/tasks/", status_code=201, response_model=TaskInResponse)
def create_new_task(task: Task):
    return create_task(task)

@router.get("/tasks/", response_model=list[TaskInResponse])
def get_all_tasks():
    return get_tasks()

@router.get("/tasks/{task_id}/", response_model=TaskInResponse)
def get_single_task(task_id: int):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}/", response_model=TaskInResponse)
def update_task_info(task_id: int, task: Task):
    existing_task = get_task_by_id(task_id)
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = update_task(task_id, task)
    return updated_task

@router.delete("/tasks/{task_id}/", status_code=204)
def delete_task_info(task_id: int):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(task_id)
    return None
