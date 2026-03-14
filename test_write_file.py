from functions.write_file import *
test_case = ["lorem.txt", "pkg/morelorem.txt", "/tmp/temp.txt"]
work_dir = "calculator"
contents = ["wait, this isn't lorem ipsum", "lorem ipsum dolor sit amet", "this should not be allowed"]
def main():
    results = []
    
    for case, content in zip(test_case, contents):
        
        results.append(write_file(work_dir, case, content))
        
    
    
    print(f"Results for all test calls:")
    for result in results:
        print(f"  --{result}")


main()

