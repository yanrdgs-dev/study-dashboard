from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str | None = None
    done: bool = False

class TaskInResponse(Task):
    id: int
    title: str
    description: str | None = None
    done: bool = False