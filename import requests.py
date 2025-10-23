import requests
import json
import time

API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b"
API_KEY = "YOUR_HUGGINGFACE_API_KEY"
INPUT_FILE = "input_prompts.txt"
timestamp = time.strftime("%Y%m%d_%H%M")
OUTPUT_FILE = f"responses_gemma_{timestamp}.json"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

responses = []

with open(INPUT_FILE, "r", encoding="utf-8") as infile:
    prompts = [line.strip() for line in infile if line.strip()]

for prompt in prompts:
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200
        }
    }
    resp = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    output = resp.json()
    responses.append({
        "prompt": prompt,
        "response": output
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    json.dump(responses, outfile, indent=2)
