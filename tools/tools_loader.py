# tools_loader.py
from tools import SeachWikiTools
from tools.tools import generate_sql, translate  # 导入你定义的所有工具

def load_tools(tool_names):
    tools = []
    for name in tool_names:
        if name == 'get_article':
            tools.append(SeachWikiTools.get_article_tool())
        elif name == 'another_tool':
            tools.append(generate_sql())
        elif name == 'yet_another_tool':
            tools.append(translate())
        # 继续添加其他工具的逻辑...
    return tools

def verify_tools(response,tools):
    # 验证工具是否有在response里，并返回结果
    try:
        assistant_message = response['message']
        if assistant_message['tool_calls']:
            dasd = assistant_message['tool_calls']
            if dasd[0]['function']['name'] in tools:
                function_args = dasd[0]['function']['arguments']
                return function_args
    except Exception as e:
        print(e)
        return False
    
def message_append(messages,role,content):
    # 给消息添加角色和内容
    try:
        tool_response = {
          "role": role,
          "content": content
        }
        messages.append(tool_response)
        return messages
    except Exception as e:
        print(e)
        return False