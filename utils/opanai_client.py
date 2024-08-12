# Import the OpenAI library
from openai import OpenAI

# Define a class to interact with the OpenAI API
class OpenAIClient:

    # Initialize the client and specify the model to use
    def __init__(self, model):
        """
        Initializes the OpenAIClient instance.
        Args:
            model (str): The name of the AI model to use for chat completions.
        """
        self.client = OpenAI()  # Create an instance of the OpenAI client
        self.model = model  # Store the specified model
        
    # Perform a chat completion using the specified model
    def chat(self, messages, tools):
        """
        Sends a chat message to the OpenAI API and receives a completion.
        Args:
            messages (list): A list of messages to send to the API.
            tools (dict): Additional metadata to include with the request.
        Returns:
            The result of the chat completion, as returned by the API.
        """
        return self.client.chat.completions.create(model=self.model, messages=messages, tools=tools)
