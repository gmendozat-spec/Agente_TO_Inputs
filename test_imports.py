import os
import sys

print("Python version:", sys.version)

env_keys = [k for k in os.environ.keys() if any(x in k.upper() for x in ["GEMINI", "GOOGLE", "API", "VERTEX"])]
print("Relevant Env Keys:", env_keys)

for k in env_keys:
    val = os.environ.get(k)
    print(f"  {k}: {'[PRESENT, Length: ' + str(len(val)) + ']' if val else '[EMPTY]'}")

# Check installed modules
modules = ['google.generativeai', 'google.genai', 'google.cloud.aiplatform', 'openai']
for m in modules:
    try:
        __import__(m)
        print(f"Module {m} is installed")
    except ImportError:
        print(f"Module {m} is NOT installed")
