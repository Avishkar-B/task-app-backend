from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from pymongo import MongoClient
from datetime import datetime
from schemas import TaskCreate, TaskUpdate, TaskResponse
from models import tasks_collection, serialize_task
from bson.objectid import ObjectId

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/tasks/create', methods=['POST'])
def create_task():
    try:
        task_data = TaskCreate(**request.get_json())
        task = task_data.dict(exclude_unset=True)
        tasks_collection.insert_one(task)
        return jsonify({'messafe': "Task hase been successfully created" })
    except ValidationError as e:
        return jsonify({'error': e.errors()})
    
@api_routes.route('/tasks/fetch', methods=['GET'])
def fetch_all_tasks():
    try:
        tasks = list(tasks_collection.find({}))
        tasks = [serialize_task(task) for task in tasks]
        return jsonify(tasks)
    except:
        return jsonify({'error': 'An Error occured when fethcing the tasks'})

@api_routes.route('/tasks/update/<task_id>',methods=['POST'])
def update_task(task_id):
    try:
        print(task_id)
        data = request.get_json()
        task_data = TaskUpdate(**data)
        
        update_fields = task_data.model_dump(exclude_unset=True)
        
        result = tasks_collection.update_one(
            {"_id": ObjectId(task_id)}, {'$set': update_fields}
        )
        
        if result.matched_count > 0:
            return jsonify({"message" : "task has been updated"})
        else:
            return jsonify({"message" : "could not find task"})
    except:
        print()
        return jsonify({'message' : 'error during task updation'})
    
@api_routes.route('/tasks/delete/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    
    if result.deleted_count > 0:
        return jsonify({"message": 'successfully deleted task'})
    else:
        return jsonify({"message": 'couldnt find'})