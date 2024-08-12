# Import the Ollama client class from the ollama library.
from ollama import Client

class OllamaClient:
    def __init__(self, host, model):
        """
        Initializes an OllamaClient instance.

        Parameters:
            host (str): The hostname or IP address of the Ollama server.
            model (str): The name of the language model to use for chat sessions.
        Returns:
            None
        """
        # Create a new Ollama client instance with the provided host.
        self.client = Client(host=host)
        # Set the model attribute to the provided value.
        self.model = model

    def chat(self, messages, tools):
        """
        Starts a chat session with the Ollama server using the specified language model.

        Parameters:
            messages (str): The messages to send to the Ollama server.
            tools (str): Additional tools or plugins to use during the chat session.
        Returns:
            str: The response from the Ollama server as a result of the chat session.
        """
        # Use the client instance to start the chat session.
        return self.client.chat(model=self.model, messages=messages, tools=tools)
