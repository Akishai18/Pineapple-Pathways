import requests

# Define your API key
API_KEY = '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'
URL = 'https://api.openai.com/v1/chat/completions'

# Set the headers with your API key
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def chat_with_gpt(messages):
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': messages,
    }
    response = requests.post(URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

def get_content_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
        return content
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

def generate_feedback(user_input):
    system_file_path = "./system_prompt.txt"
    system_prompt = get_content_from_file(system_file_path)

    if system_prompt:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
        response = chat_with_gpt(messages)
        if response:
            return response['choices'][0]['message']['content']
        return None
