# main.py
# from TaskManager import TaskManager
from TaskManager2 import Taskmanager2
from util import parse_arguments
if __name__ == "__main__":

    manager = Taskmanager2("tasks.json")
    command, args = parse_arguments()

    if command == "add" and len(args) == 1:
        manager.add_task(args[0])
    elif command == "update" and len(args) == 2:
        manager.update_task(int(args[0]), args[1])
    elif command == "delete" and len(args) == 1:
        manager.delete_task(int(args[0]))
    elif command == "mark-in-progress" and len(args) == 2:
        manager.change_status(int(args[0]), "in-progress")
    elif command == "mark-done" and len(args) == 2:
        manager.change_status(int(args[0]), "done")
    elif command == "list":
        status = args[0] if args else None
        manager.list_tasks(status)
    elif command == "list" and len(args) == 1:
        manager.list_tasks(args[0])
    else:
        print("Invalid command or arguments")
