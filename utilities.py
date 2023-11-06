def get_file_extension(filename):
    return filename.split(".")[-1]

def uniform_file_types(file_paths):
    file_type = get_file_extension(file_paths[0])
    for file_path in file_paths:
        if get_file_extension(file_path) != file_type:
            return None
    
    return file_type