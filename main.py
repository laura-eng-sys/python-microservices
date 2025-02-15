# from mylib.logic import wiki

# result = wiki()
# print(result)
# ex of a lint failure
# result=wiki()
# result=result
# print(result)

# ****************let's build our microservice******************
from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrase as wikiphrases

# home page of our api app
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}

    # 1st endpoint


@app.get("/search/{value}")
async def add(value: str):
    """Page to search in wikipedia"""
    result = search_wiki(value)
    return {"result": result}

    # 2nd endpoint


@app.get("/wiki/{name}")
async def wiki(name: str):
    """retrieve info from wikipedia"""
    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """retrieve wikipedia page and return phrases"""

    result = wikiphrases(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
