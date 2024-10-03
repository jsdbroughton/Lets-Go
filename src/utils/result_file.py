import os
import tempfile

def write_list_of_lists_to_file(list_of_lists) -> str:
    os.makedirs(tempfile.gettempdir(), exist_ok=True)
    file_path = os.path.join(tempfile.gettempdir(), "data.txt")
    try:
        with open(file_path, 'w') as file:
            for inner_list in list_of_lists:
                # Convert all elements to strings and join with commas
                line = ','.join(map(str, inner_list))
                file.write(line + '\n')
        print(f"Data successfully written to {file_path}")
        return file_path
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")