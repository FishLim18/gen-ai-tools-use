# main.py
import os
import json
from utils import OllamaClient
from utils import OpenAIClient
from tools.tools_loader import load_tools,verify_tools,message_append
from tools import SeachWikiTools


def wiki_search(client):
    # 根据需要加载工具
    tool_names = ['get_article']  # 你可以在这里配置需要的工具名
    tools = load_tools(tool_names)
    messages = [{"role": "user", "content": "Please answer the question within 20 words. who won the 2024 Masters Tournament?"}]
#    message_append(messages=messages,role="user",content="who won the 2024 Masters Tournament?")
    response = client.chat(messages=messages, tools=tools)
#    print(response)
    messages = message_append(messages=messages,role="assistant",content=response['message']['content'])
    tool_action = SeachWikiTools()
    wikisearch = tool_action.get_article(verify_tools(response,tool_names)['search_term'])

    response = client.chat(messages=message_append(messages=messages,role="user",content=wikisearch), tools=tools)
#    print (response)
    print("Ollama's final answer:")
    print(response['message']['content'])

def wiki_search_openai(client):
    # 根据需要加载工具
    tool_names = ['get_article']  # 你可以在这里配置需要的工具名
    tools = load_tools(tool_names)
    messages = [{"role": "system", "content": "Please answer the question within 20 words."}]
    message_append(messages=messages,role="user",content="who won the 2024 Masters Tournament?")
    response = client.chat(messages=messages,tools=tools,)
    # print(response)

    tool_call = response.choices[0].message.tool_calls[0]
    print(tool_call)
    arguments = json.loads(tool_call.function.arguments)
    print(arguments)
    search_term = arguments.get('search_term')
    messages = message_append(messages=messages,role="assistant",content=search_term)

    tool_action = SeachWikiTools()
    wikisearch = tool_action.get_article(search_term)
    messages = message_append(messages=messages,role="user",content=wikisearch)

    response = client.chat(messages=messages,tools=tools,)
    # print (response)
    print("OpenAI's final answer:")
    print(response.choices[0].message.content)


def main():
    # 加载环境变量，获取Ollama的地址和模型名称
    # ollama_host = os.environ['OLLAMA_HOST']
    # ollama_model = 'llama3.1:8b'
    # client = OllamaClient(host=ollama_host,model=ollama_model)

    # wiki_search(client)

    client = OpenAIClient(model="gpt-4o-mini")
    wiki_search_openai(client)

    
if __name__ == "__main__":
    main()
