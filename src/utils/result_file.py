import os
import tempfile
from pathlib import Path
import json

def write_list_of_lists_to_file(list_of_lists) -> str:
    try:
        os.makedirs(tempfile.gettempdir(), exist_ok=True)
        file_path = os.path.join(tempfile.gettempdir(), "data.json")
        Path(file_path).write_text(json.dumps(list_of_lists))
        return file_path
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")