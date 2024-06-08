from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    priority: str  # Priority can be 'Very High', 'High', 'Moderate', 'Low', 'Very Low'
    description: Optional[str]
    status: str

class TaskInDB(Task):
    id: Optional[str]
