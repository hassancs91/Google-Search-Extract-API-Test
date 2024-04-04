from SimplerLLM.tools.serp import search_with_serper_api
from SimplerLLM.tools.generic_loader import load_content
from fastapi import FastAPI


app = FastAPI()

@app.get("/search")
def search(query: str,num_results: int = 10):
    results = search_with_serper_api(query, num_results=num_results)
    return results


@app.get("/load_content")
def load_content_frpm_url(url: str):
    content_loaded = load_content(url)
    return content_loaded


