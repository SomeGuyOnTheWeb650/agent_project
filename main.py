import os, argparse, sys
from dotenv import load_dotenv
from google.genai import types
from prompts import system_prompt
from call_function import *
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("api_key wasn't found, check that .env is working correctly")
from google import genai
client = genai.Client(api_key=api_key)
for i in range(20):
    response = client.models.generate_content(
        model= "gemini-2.5-flash", 
        contents= messages, 
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt,
        ),
    )
# possibly change scope below
    if response.usage_metadata == None:
        raise RuntimeError("prompt didn't run correctly")
    
    if len(response.candidates) > 0:
        for mess in response.candidates:
            messages.append(mess.content)

    func_objects = response.function_calls
    func_results = []
    
    if func_objects:

        for ob in func_objects:
            function_call_result = call_function(ob, args.verbose)
            if len(function_call_result.parts) == 0:
                raise Exception("Error: Empty parts list")
            if function_call_result.parts[0].function_response == None:
                raise Exception("Error: .part.functionresponse == None")
            if function_call_result.parts[0].function_response.response == None:
                raise Exception("Error: function_call_result.parts[0].function_response == None")
            func_results.append(function_call_result.parts[0]) 
            if args.verbose:
                
                print(f"-> {function_call_result.parts[0].function_response.response}")
        messages.append(types.Content(role="user", parts=func_results))
        if i == 19:
            print("Possible Error: Reached maximum established prompts: 20")
            sys.exit(1)
    
    

    else:
        print(response.text)
        break


    



