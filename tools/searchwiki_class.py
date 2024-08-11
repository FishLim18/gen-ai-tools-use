import wikipedia

class SeachWikiTools:
    def __init__(self):
        pass
        
    def get_article(self,search_term):
        results = wikipedia.search(search_term)
        first_result = results[0]
        page = wikipedia.page(first_result, auto_suggest=False)
        return page.content
    
    @classmethod
    def get_article_tool(cls):
        return {
            "type": "function",
            "function": {
                "name": "get_article",
                "description": "A tool to retrieve an up to date Wikipedia article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_term": {
                            "type": "string",
                            "description": "The search term to find a wikipedia article by title",
                        }
                    },
                    "required": ["search_term"],
                },
            },
        }