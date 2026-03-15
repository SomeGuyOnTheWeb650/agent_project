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
if args.verbose:

    print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")


func_objects = response.function_calls

if len(func_objects) > 0:

    for ob in func_objects:
        print(f"Calling function: {ob.name}({ob.args})")
else:
    print(response.text)


    



