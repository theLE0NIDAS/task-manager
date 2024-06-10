from pydantic import BaseModel
from typing import Optional, List

class Task(BaseModel):
    title: str
    priority: str  # Priority can be 'Very High', 'High', 'Moderate', 'Low', 'Very Low'
    description: Optional[str]
    status: str

class TaskInDB(Task):
    id: Optional[str]


class TaskWithDependencies(BaseModel):
    title: str
    priority: str  # Priority can be 'Very High', 'High', 'Moderate', 'Low', 'Very Low'
    description: Optional[str]
    status: str
    depends_on: List[str] = []  # List of task IDs this task depends on

class TaskInDBWithDependencies(TaskWithDependencies):
    id: Optional[str]