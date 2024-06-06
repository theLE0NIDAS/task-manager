from fastapi import FastAPI
from pymongo import MongoClient
from .routes import router as task_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Add CORS middleware for Vue.js dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes from routes.py
app.include_router(task_router)

# MongoDB connection
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client['task-manager']

# Root endpoint (health check)
@app.get("/")
def read_root():
    return {"message": "Connected to MongoDB Atlas successfully!"}

# Test MongoDB endpoint
@app.get("/test-mongo")
def test_mongo():
    # Insert a test document and retrieve it
    test_collection = db.test_collection
    test_collection.insert_one({"test_key": "test_value"})
    test_doc = test_collection.find_one({"test_key": "test_value"})
    
    # Remove the MongoDB ObjectId before returning the document
    test_doc["_id"] = str(test_doc["_id"])
    
    return {"MongoDB Test": "Success", "document": test_doc}
