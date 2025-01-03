import file_handler as fh
from Task import Task

class Taskmanager2:

    def __init__(self, filepath):
        self.filepath = filepath
        fh.init_json_file(filepath)

    def _load_task(self):

        task_dicts = fh.read_json(self.filepath)
        tasks = []
        for task_dict in task_dicts:
            task = Task.from_dict(task_dict)
            tasks.append(task)

        return tasks
        # or use => return [Task.from_dict(task) for task in file_handler.read_json(self.filepath)]

    def _save_task(self, tasks):
        task_dicts_list = []
        for task in tasks:
            task_dict = task.to_dict()
            task_dicts_list.append(task_dict)

        fh.write_json(self.filepath, task_dicts_list)

    def add_task(self, description):
        tasks = self._load_task()
        task_id = max((task.id for task in tasks), default=0)+1
        new_task = Task(task_id, description, "todo")
        tasks.append(new_task)
        self._save_task(tasks)
        print(f"Task {task_id} is added")

    def delete_task(self, task_id):
        tasks = self._load_task()
        tasks_list = []
        for task in tasks:
            if task.id != task_id:
                tasks_list.append(task)
        self._save_task(tasks_list)
        print(f"Task {task_id} is deleted")

        # or  tasks = [task for task in tasks if task_id != task.id]

    def update_task(self, task_id, new_description):
        tasks = self._load_task()
        task_list = []
        for task in tasks:
            if task.id == task_id:
                task.description = new_description

            self._save_task(tasks)

    def change_status(self,task_id, new_status):
        tasks = self._load_task()
        task = next((task for task in tasks if task.id == task_id))

        if task:
            task.update_status(new_status)
            self._save_task(tasks)
            print("Updated")
            return
        print("task not found")

    def list_tasks(self, status=None):
        tasks= self._load_task()
        try:
            if status:
                tasks = [task for task in tasks if task.status == status]

        except ValueError as e:
            print(e)

        for task in tasks:
            print(f"ID: {task.id}, Description: {task.description}, Status: {task.status}, Created At: {task.created_at}")

