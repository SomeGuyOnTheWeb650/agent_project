import os

def get_files_info(working_directory, directory="."):
    try:
        
        abs = os.path.abspath(working_directory)
        full = os.path.join(abs, directory)
        norm = os.path.normpath(full)
        valid = os.path.commonpath([abs, norm]) == abs
        if not valid:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(norm) == False:
            return f"smelly"
        
    except Exception:
        return f"early"
    try:    
        iter = os.listdir(norm)
        
        details = ""
        for i in iter:
            p = norm + "/" + i
            details = details + f"  - {i}: file_size={os.path.getsize(p)} bytes, is_dir={os.path.isdir(p)}\n" 

            
        
    except Exception:
        return f"Error: something messed up in creating details strings"
    
    return details

