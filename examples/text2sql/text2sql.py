import os
import json
import sqlite3
from ollama import Client
from datetime import datetime, timedelta

ollama_host = os.environ['OLLAMA_HOST']
#ollama_host = os.environ['OLLAMA_HOST']
ollama_model = 'mistral:7b'
db='examples/text2sql/demo_users.db'

# Initialize Ollama client
client = Client(host=ollama_host)

def get_print_db_info(sql_query):

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    print("\nSample data from the users table:")
    for row in rows:
        print(row)

    conn.close()

# Database connection function
def get_db_connection():
    """Create and return a connection to a SQLite database"""
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn

def execute_sql(sql_query):
    """Execute SQL query and return results"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        results = [dict(row) for row in cursor.fetchall()]
        print(results)
        return results
    except sqlite3.Error as e:
        return f"Database Error: {e}"
    finally:
        conn.close()

def generate_sql(table_info, conditions, select_fields="*"):
    """
    Generate SQL query
    :param table_info: table information
    :param conditions: conditions of WHERE clause
    :param select_fields: fields to select, default is all fields
    :return: generated SQL query string
    """
    return f"SELECT {select_fields} FROM users WHERE {conditions}"

def format_results(results, fields=None):
    """
    Format query results
    :param results: list of results returned by the query
    :param fields: list of fields to display, if None, all fields will be displayed
    :return: formatted result string
    """
    if isinstance(results, str):  # If the result is an error message
        return results

    if not results:
        return "No matching record found."

    if fields:
        formatted = [", ".join(str(row.get(field, "N/A")) for field in fields) for row in results]
    else:
        formatted = [json.dumps(row, ensure_ascii=False, indent=2) for row in results]

    return "\n".join(formatted)

def run_text2sql_conversation(user_prompt):
    """
    Run text2sql conversation
    :param user_prompt: query entered by the user
    :return: query results
    """
#    get_print_db_info("SELECT email,last_login FROM users WHERE name = 'Alice'")

    table_info = "users(id INTEGER, name TEXT, age INTEGER, email TEXT, registration_date DATE, last_login DATETIME)"

    messages = [
        {
            "role": "system",
            "content": f"You are a SQL assistant. Use the generate_sql function to create SQL queries based on user requests. Available tables: {table_info}. Accurately understand user needs, including the specific fields they want to query."
        },
        {
            "role": "user",
            "content": user_prompt,
        }
    ]

    tools = [
        {
            "type": "function",
            "function": {
                "name": "generate_sql",
                "description": "Generate SQL queries based on user requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "table_info": {
                            "type": "string",
                            "description": "Table structure information",
                        },
                        "conditions": {
                            "type": "string",
                            "description": "Specific query conditions for the WHERE clause, this is not the must field",
                        },
                        "select_fields": {
                            "type": "string",
                            "description": "Fields to select, separated by commas",
                        }
                    },
                    "required": ["table_info","conditions" ,"select_fields"],
                },
            },
        }
    ]

    try:
        response = client.chat(
            model= ollama_model,
            messages=messages,
            tools=tools
        )
        print (response)
        assistant_message = response['message']

        if assistant_message['tool_calls']:
            dasd = assistant_message['tool_calls']

            if dasd[0]['function']['name'] == "generate_sql":
#                qwer = dasd[0]['function']['arguments']
#                print(f'Arguments: {qwer}')
                function_args = dasd[0]['function']['arguments']
                sql_query = generate_sql(
                function_args["table_info"],
                function_args["conditions"],
                function_args["select_fields"]
                    )
                print (sql_query)
#                get_print_db_info(sql_query)
                results = execute_sql(sql_query)
                print(results)
                formatted_results = format_results(results, function_args["select_fields"].split(", ") if function_args["select_fields"] != "*" else None)
                return f"Generated SQL query: {sql_query}\n\nResult:\n{formatted_results}"
        else:
            return "Unable to generate SQL query. Please try rephrasing your question."

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main function
if __name__ == "__main__":
    print("Welcome to the Text2SQL system!")
    print("You can ask questions about user tables in natural language.")
    print("Type 'quit' to exit the program.")

    while True:
        user_input = input("\nPlease enter your query (or 'quit' to exit):")
        if user_input.lower() == 'quit':
            print("Thanks for using, bye!")
            break

        result = run_text2sql_conversation(user_input)
        print("\n" + "="*50)
        print(result)
        print("="*50)