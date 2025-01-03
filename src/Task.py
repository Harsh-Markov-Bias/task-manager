import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)


class Task:

    def __init__(self, id, description, status, created_at=None, updated_at=None):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def update_description(self, new_description):
        self.description = new_description
        self.updated_at = datetime.now()

    def update_status(self, new_status):
        self.status = new_status
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        return my_dict

    @classmethod
    def from_dict(cls, task_dict):
        required_keys = {"id", "description", "status", "created_at", "updated_at"}

        missing_keys = required_keys - task_dict.keys()
        if missing_keys:
            raise ValueError(f"The following keys are missing {missing_keys}")

        for key in required_keys:
            if task_dict.get(key) is None:
                logging.warning(f"The {key} contains none value")
                raise ValueError(f"The {key} contains none value")
        try:
            created_at = datetime.strptime(task_dict["created_at"], "%Y-%m-%d %H:%M:%S")
            updated_at = datetime.strptime(task_dict["updated_at"], "%Y-%m-%d %H:%M:%S")
        except ValueError as ve:
            raise ValueError("Invalid datetime format. Use 'YYYY-MM-DD HH:MM:SS'") from ve

        return cls(
            id=task_dict["id"],
            description = task_dict["description"],
            status=task_dict["status"],
            created_at=created_at,
            updated_at=updated_at
        )








