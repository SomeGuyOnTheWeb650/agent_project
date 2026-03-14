import os

def write_file(working_directory, file_path, content):
    try:
        
        abs = os.path.abspath(working_directory)
        full = os.path.join(abs, file_path)
        norm = os.path.normpath(full)
        valid = os.path.commonpath([abs, norm]) == abs
        
        if not valid:
            return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
        
        if os.path.isdir(norm):
            return f"Error: Cannot write to '{file_path}' as it is a directory"
        
        parent = os.path.dirname(norm)
        os.makedirs(parent, exist_ok=True)
        
        opened = open(norm, "w")
        opened = content
    except Exception:
        return "Something wacky"
    return f"Successfully wrote to '{norm}' ({len(content)} characters written)"
