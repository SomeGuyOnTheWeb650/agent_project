import os, subprocess
def run_python_file(working_directory, file_path, args=None):
    try:
    
        abs = os.path.abspath(working_directory)
        abs_file_path = os.path.join(abs, file_path)
        norm_file_path = os.path.normpath(abs_file_path)
        valid = os.path.commonpath([abs, norm_file_path]) == abs
        if not valid:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(norm_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not norm_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", norm_file_path]
        if args is not None:

            command.extend(args)
        completed = subprocess.run(command, cwd=abs, capture_output=True, timeout=30, text=True)
        
        output = ""
        if completed.returncode != 0:
            output = f"{output} 'Process exited with code {completed.returncode}'"
        if completed.stderr == None and completed.stdout == None:
            output = f"{output} 'No output produced'"
        else:
            output = f"{output} STDOUT: {completed.stdout}  --STDERR: {completed.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"

    return output
    