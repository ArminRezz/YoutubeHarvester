import requests

class LMStudioAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_models(self):
        response = requests.get(f"{self.base_url}/v1/models")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def chat_completion(self, messages):
        response = requests.post(f"{self.base_url}/v1/chat/completions", json={"messages": messages})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def completion(self, prompt):
        response = requests.post(f"{self.base_url}/v1/completions", json={"prompt": prompt})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

# Example usage
if __name__ == "__main__":
    lm_studio_api = LMStudioAPI(base_url="http://10.6.146.12:8080")

    # Initialize conversation history
    conversation_history = []

    while True:
        # Collect user message
        user_message = input("Chat: ")
        conversation_history.append({"role": "user", "content": user_message})

        # Send conversation history for chat completion
        chat_response = lm_studio_api.chat_completion(conversation_history)
        print("Response:", chat_response['choices'][0]['message']['content'])

        # Append assistant's response to conversation history
        conversation_history.append({"role": "assistant", "content": chat_response['choices'][0]['message']['content']})

        # Optionally, you can add a termination condition here if needed
        # For example: if user_message.lower() == 'exit': break
