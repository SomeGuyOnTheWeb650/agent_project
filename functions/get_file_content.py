import os
import config
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        
        abs = os.path.abspath(working_directory)
        join = os.path.join(abs, file_path)
        norm = os.path.normpath(join)
        valid = os.path.commonpath([abs, norm]) == abs
        
        
        if not valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(norm):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        f = open(norm)
        contents = f.read(config.MAX_CHARS)
        
        if f.read(1):
            contents += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
             
    except Exception:
        return f"Error: something wacky happened"
        
    return contents
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="returns a string, containing the contents of a particular file, if longer than 10000 characters, truncates at 10000 and adds a truncated message",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path relative to working directory",
            ),
        },
        required=["file_path"]
    ),
)