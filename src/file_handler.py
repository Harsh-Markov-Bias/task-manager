import json
import os


def init_json_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'r') as file:
            json.dump([], file)


def read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def write_json(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

