from fastapi import FastAPI
import uvicorn
from devops_lib.logic import search_wiki
from devops_lib.logic import wiki as wikiget
from devops_lib.logic import phrase as wikiphrase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wiki page"""
    result = wikiget(name)
    return {"result": result}

@app.get("/phrase/{name}")
async def phrase(name: str):

    result = wikiphrase(name)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
