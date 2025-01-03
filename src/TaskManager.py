from datetime import datetime
import json
import os
import file_handler
from Task import Task


class TaskManager:

    def __init__(self, filepath):
        self.filepath = filepath
        file_handler.init_json_file(filepath)

    def _load_tasks(self):
        return [Task.from_dict(task) for task in file_handler.read_json(self.filepath)]

    def _save_task(self, tasks):
        file_handler.write_json(self.filepath, [task.to_dict() for task in tasks])

    def add_task(self, description):
        tasks = self._load_tasks()
        task_id = max((task.id for task in tasks), default=0) +1
        new_task = Task(task_id,description,"todo")
        tasks.append(new_task)
        self._save_task(tasks)
        print(f"Task added successfully (ID: {task_id})")

    def delete_task(self, task_id):
        tasks = self._load_tasks()
        tasks = [task for task in tasks if task_id != task.id]
        self._save_task(tasks)
        print("Task deleted")

    def update_task(self, task_id, description):
        tasks = self._load_tasks()
        task = next((task for task in tasks if task_id == task.id))
        if task:
            task.description = description
            self._save_task(tasks)
            print("Task updated successfully")
            return
        print("Task not found")

    def change_status(self,task_id, status):
        tasks = self._load_tasks()
        task = next((task for task in tasks if task_id == task.id))
        if task:
            task.update_status(status)
            self._save_task(tasks)
            print(f"Task marked as {status}")
            return
        print("Task not found")

    def list_tasks(self, status=None):
        tasks = self._load_tasks()
        if status:
            tasks = [task for task in tasks if task.status == status]

        for task in tasks:
            print(f"ID: {task.id}, Description: {task.description}, Status: {task.status}, Created At: {task.created_at}")















