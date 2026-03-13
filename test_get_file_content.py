from functions.get_file_content import *

print(f"Result for 'lorem.txt' file:\n  -{len(get_file_content("calculator", "lorem.txt"))} truncation: {"truncated at" in get_file_content("calculator", "lorem.txt")}")

print(f"Result for 'main.py' file:\n  -{get_file_content("calculator", "main.py")}")

print(f"Result for 'pkg/calculator.py' file:\n  -{get_file_content("calculator", "pkg/calculator.py")}")

print(f"Result for 'bin/cat' file?:\n  -{get_file_content("calculator", "bin/cat")}")

print(f"Result for 'pkg/does_not_exist.py' file?:\n  -{get_file_content("calculator", "pkg/does_not_exist.py")}")