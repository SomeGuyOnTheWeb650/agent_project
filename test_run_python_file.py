from functions.run_python_file import *
working_dir = "calculator"
file_path_test_cases = ["main.py", "main.py", "tests.py", "../main.py", "nonexistent.py", "lorem.txt"]
args = ["3 + 5"]

def test_suite():
    results = []
    
    for i, case in enumerate(file_path_test_cases):
        
        if i == 1:
            
            results.append(run_python_file(working_dir, case, args))
        else:
            results.append(run_python_file(working_dir, case))

    
    print(f"Result for each test case:")
    for result in results:
        print(f"  --{result}")

test_suite()