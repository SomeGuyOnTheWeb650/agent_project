import os, argparse
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
response = client.models.generate_content(
    model= "gemini-2.5-flash", 
    contents= messages, 
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    ),
)
if response.usage_metadata == None:
    raise RuntimeError("prompt didn't run correctly")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response token: {response.usage_metadata.candidates_token_count}")

func_objects = response.function_calls
func_results = []
if len(func_objects) > 0:

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
        


else:
    print(response.text)


    



