from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://john:46gDqs4hWwd4uJzb@cluster0.gl0juex.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.tasks_db
tasks_collection = db.tasks

def serialize_task(task):
    task['_id'] = str(task['_id'])
    return task