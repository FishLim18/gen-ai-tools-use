# tools.py

def generate_sql():
    return {
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
                    },
                },
                "required": ["table_info", "conditions", "select_fields"],
            },
        },
    }

def translate():
    return {
        "type": "function",
        "function": {
            "name": "translations_from_claude",
            "description": "The translations from Claude of a user provided phrase into English to Spanish, French, Japanese, and Arabic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "english": {"type": "string", "description": "Your English translation of the provided content from the user"},
                },
                "required": ["english"],
            },
        },
    }