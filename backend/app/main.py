from fastapi import FastAPI
from pymongo import MongoClient
from .routes import router as task_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your Vue.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)

client = MongoClient("MONGODB_URI")
db = client['task-manager']

@app.get("/")
def read_root():
    return {"message": "Connected to MongoDB Atlas successfully!"}

@app.get("/test-mongo")
def test_mongo():
    # Insert a test document and retrieve it
    db.test_collection.insert_one({"test_key": "test_value"})
    test_doc = db.test_collection.find_one({"test_key": "test_value"})
    return {"MongoDB Test": "Success", "document": test_doc}