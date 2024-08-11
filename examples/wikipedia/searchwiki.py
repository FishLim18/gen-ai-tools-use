import os
import json
from ollama import Client
import wikipedia

ollama_host = os.environ['OLLAMA_HOST']
#ollama_host = os.environ['OLLAMA_HOST']
ollama_model = 'llama3.1:8b'

# Initialize Ollama client
client = Client(host=ollama_host)

def get_article(search_term):
    results = wikipedia.search(search_term)
    first_result = results[0]
    page = wikipedia.page(first_result, auto_suggest=False)
    return page.content

#article = get_article("Superman")
#print(article[:500]) # article is very long, so let's just print a preview

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_article",
            "description": "A tool to retrieve an up to date Wikipedia article.",
            "parameters": {
                "type": "object",
                "properties": {
                    "search_term": {
                        "type": "string",
                        "description": "The search term to find a wikipedia article by title"
                    }
                },
                "required": ["search_term"],
            },
        },
    }
]

messages = [
    {
        "role": "user",
        "content": "who won the 2024 Masters Tournament?"
    }
]


try:
    response = client.chat(
        model= ollama_model,
        messages=messages,
        tools=tools
    )
    print (response)
#    print (messages)
    messages.append({"role": "assistant", "content": response['message']['content']})
#    print (messages)
    assistant_message = response['message']
    if assistant_message['tool_calls']:
            dasd = assistant_message['tool_calls']
            if dasd[0]['function']['name'] == "get_article":
                function_args = dasd[0]['function']['arguments']
                wikisearch= get_article(function_args['search_term'])
#                 print (wikisearch)
                print (messages)
                tool_response = {
                  "role": "user",
                  "content": wikisearch
                }

                messages.append(tool_response)
                response = client.chat(
                    model= ollama_model,
                    messages=messages,
                    tools=tools
                )
                print (response)
                print("Ollama's final answer:")
                print(response['message']['content'])

except Exception as e:
        print (e)



#messages.append({"role": "assistant", "content": response['message']['tool_calls'][0]['arguments']['search_term']})