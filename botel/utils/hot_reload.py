import os, time
from botel.core import config


def detect_file_changes(file_path):
    last_modified = os.path.getmtime(file_path)
    while True:
        print(os.stat(file_path))
        current_modified = os.path.getmtime(file_path)
        if current_modified != last_modified:
            print("File change detected")
            last_modified = current_modified
        time.sleep(1)


print(config.ROOT_DIR)

detect_file_changes(config.ROOT_DIR)
