from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from .models import Task, TaskInDB
from .priority_queue import PriorityQueue
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
mongodb_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongodb_uri)
db = client['task-manager']
tasks_collection = db['tasks']
task_queue = PriorityQueue()

def get_priority_value(priority: str) -> int:
    priority_order = {
        "Very High": 1,
        "High": 2,
        "Moderate": 3,
        "Low": 4,
        "Very Low": 5
    }
    return priority_order.get(priority, 6)

@router.post("/tasks/", response_model=TaskInDB)
def create_task(task: Task):
    task_id = tasks_collection.insert_one(task.dict()).inserted_id
    task_data = tasks_collection.find_one({"_id": task_id})
    task_data['id'] = str(task_data['_id'])
    task_queue.push(task_data, get_priority_value(task_data['priority']))
    return TaskInDB(**task_data)

@router.get("/tasks/", response_model=list[TaskInDB])
def get_tasks():
    tasks = list(tasks_collection.find())
    for task in tasks:
        task['id'] = str(task['_id'])
    return tasks

@router.get("/tasks/sorted", response_model=list[TaskInDB])
def get_sorted_tasks():
    sorted_tasks = []
    while not task_queue.is_empty():
        sorted_tasks.append(task_queue.pop())
    return sorted_tasks

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}

@router.put("/tasks/{task_id}", response_model=TaskInDB)
def update_task(task_id: str, task: Task):
    result = tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": task.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    task_data = tasks_collection.find_one({"_id": ObjectId(task_id)})
    task_data['id'] = str(task_data['_id'])
    return TaskInDB(**task_data)
