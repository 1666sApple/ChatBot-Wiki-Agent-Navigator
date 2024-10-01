from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

def get_wikipedia_tool():
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=256)
    return WikipediaQueryRun(api_wrapper=api_wrapper)