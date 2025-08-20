import os
def _read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def _get_file_paths_from_directory(directory):
    return [os.path.join(directory, filename) for filename in os.listdir(directory)]

for i in _get_file_paths_from_directory("data/transcripts/raw"):
    print(_read_file(i))
    break