import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
class SearchTool:
    def __init__(self):
        self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def run_search(self, ticker):
        query = f"Why's {ticker} stock high today? also give me news about {ticker} for last 7 days."
        print(f"--- Searching: {query} ---")
        
        response = self.tavily_client.search(query)
        return self._format_results(response.get('results', []))

    def _format_results(self, results):

        cleaned_output = ''

        for i, item in enumerate(results):
            cleaned_output += f"Source {i}: {item.get('title')} \n"
            cleaned_output += f"URL: {item.get('url')}\n"
            cleaned_output += f"Content: {item.get('content')}\n"
            cleaned_output += "-" * 30 + "\n" # Separator line

        return cleaned_output  


