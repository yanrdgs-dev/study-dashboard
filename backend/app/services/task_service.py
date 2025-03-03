import sqlite3
from app.db.database import get_db
from app.models.schemas import Task, TaskInResponse

def create_task(task: Task):
    task_data = task.model_dump()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO tasks (title, description, done)
                   VALUES (?, ?, ?)
                   """, (task.title, task.description, task.done))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return {"id": task_id, "title": task_data["title"], "description": task_data["description"], "done": task_data["done"]}


def get_tasks():
    conn = get_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")  # Garanta que 'id' seja selecionado
        tasks = cursor.fetchall()  # Isso agora irá trazer os IDs também
        
        return [
            TaskInResponse(
                id=task[0],  # ID da tarefa
                title=task[1],  # Título da tarefa
                description=task[2],  # Descrição da tarefa
                done=task[3]  # Estado da tarefa
            ) for task in tasks
        ]

def get_task_by_id(task_id: int):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    if task:
        return TaskInResponse(**dict(task))
    return None

def update_task(task_id: int, task: Task):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
                   UPDATE tasks SET title = ?, description = ?, done = ?
                   WHERE id = ?
                   """, (task.title, task.description, task.done, task_id))
    conn.commit()
    cursor.execute("SELECT id, title, description, done FROM tasks WHERE id = ?", (task_id,))
    updated_task = cursor.fetchone()
    conn.close()
    if updated_task:
        updated_task_dict = {
            "id": updated_task[0],
            "title": updated_task[1],
            "description": updated_task[2],
            "done": updated_task[3]
        }
        return TaskInResponse(**updated_task_dict)
    return None

def delete_task(task_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()