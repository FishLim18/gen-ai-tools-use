# ollama_client.py

from ollama import Client

class OllamaClient:
    def __init__(self, host, model):
        self.client = Client(host=host)
        self.model = model
    
    def chat(self, messages, tools):
        return self.client.chat(model=self.model, messages=messages, tools=tools)