from flask import Blueprint, request, jsonify
from datetime import datetime
import json
from app.utils.decorators import require_auth

task_bp = Blueprint("tasks", __name__)

import os

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "../storage/data.json")



def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {"data": {"task": []}}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    data = load_data()
    tasks = data["data"]["task"]
    PER_PAGE = 10
    page = request.args.get("page", 1, type=int)

    if page < 1:
        page = 1

    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE

    return jsonify(tasks[start:end])

@task_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    data = load_data()
    task = next((task for task in data['data']['task'] if task['id'] == id), None)
    if task is None:
        return jsonify({'error': 'task not found'}), 404
    return jsonify({'data': task})

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


@task_bp.route("/add/task", methods=["POST"])
@require_auth
def add_task():
    data = load_data()
    req = request.get_json()

    tasks = data["data"]["task"]

    task = {
        "id": get_next_id(tasks),
        "title": req["title"],
        "description": req.get("description", ""),
        "completed": False,
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": None
    }

    tasks.append(task)
    save_data(data)

    return jsonify({"message": "Task created", "task": task}), 201

@task_bp.route('/task/update/<int:id>', methods=['PUT'])
@require_auth
def update_task(id):
    data = load_data()
    task = next((task for task in data['data']['task'] if task['id'] == id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data_from_request = request.get_json()

    if "title" in data_from_request and not data_from_request["title"].strip():
        return jsonify({"error": "Title cannot be empty"}), 400

    if "completed" in data_from_request and not isinstance(data_from_request["completed"], bool):
        return jsonify({"error": "Completed must be true or false"}), 400

    task['title'] = data_from_request.get('title', task['title'])
    task['description'] = data_from_request.get('description', task['description'])
    task['completed'] = data_from_request.get('completed', task['completed'])

    task['updated_at'] = datetime.utcnow().isoformat()
    save_data(data)

    return jsonify({
        'message': 'Task updated successfully',
        'task': task
    }), 200



@task_bp.route('/remove/tasks/<int:id>', methods=['DELETE'])
@require_auth
def delete_person(id):
    data = load_data()
    task = next((task for task in data["data"]["task"] if task['id'] == id), None)
    if id is None:
        return jsonify({'error': 'task not found'}), 404

    data["data"]["task"].remove(task)
    save_data(data)

    return jsonify({'message': 'task deleted', 'task': task})