import os
from google.genai import types
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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites the contents of the file, file_path, with contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="A string with the location of a particular file",
            ),
            "contents": types.Schema(
                type=types.Type.STRING,
                description="A string containing the message that will overwrite the current contents of file_path"
            )
        },
        required=["file_path", "contents"]
    ),
)