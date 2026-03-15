from google.genai import types
from functions import get_files_info, get_file_content, write_file, run_python_file
available_functions = types.Tool(
    function_declarations=[get_files_info.schema_get_files_info],
)