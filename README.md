# python-microservices

#MICROSERVICES STRUCTURE:
 #code
 #makefile
 #requirements.txt
 #source code
 #test
 #dockerfile
 #IAC

1-create a python environment:ctrl+shift+p or python3 -m venv .venv or virtualenv ~/.venv

2-#sourcing python virtual environment:
vim inside ~/.bashrc and paste the line below at the bottom:
source ~/.venv/bin/activate

3-create empty files:
requirements.txt
Dockerfile
Makefile

4-create a folder mylib as our project library. cd inside this folder and create files __init__.py; logic.py(to keep our source code. we can also use these cmds:
mkdir mylib
touch mylib/__init__.py

5- create a file called main.py for our infrastructure

**********************************************************

1- let's populate the makefile
install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
#check the syntax of the source code
lint:
	#flake8 or #pylint    
test:
	#test
deploy:
	#deploy
#to run 1 command, we type : make install for ex or make lint...
#to run these command at once, we type:
all:install format lint test deploy

2-populate requirements.txt
wikipedia-----------------------wikipedia==1.4.0
pytest--------------------------pytest==8.3.4
pytest-cov----------------------pytest-cov==6.0.0
pylint--------------------------pylint==3.3.4
black---------------------------black==25.1.0
fire----------------------------fire==0.7.0

3- let's edit format code from our makefile and our codes which are the logic.py and main.py files
logic.py:
import wikipedia
def wiki(name="War Goddess", length=1):
    """This is wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
    
main.py:
from mylib.logic import wiki
print(wiki())

==then run make format
python main.py

4- edit lint in makefile and run make lint

-ex of lint failure:
![Screenshot 2025-02-08 231802](https://github.com/user-attachments/assets/c12f563f-fd78-43db-a41b-7e209d34bafa)


if we edit our main.py as below, python main.py will still run successfully, but make lint will fail and procceed to code failure(see screenshot up)
main.py reedited:

from mylib.logic import wiki

result=wiki()
result=result
print(result)

5-edit our test steps and add a build step in makefile
-create a file test_logic.py and add:

from mylib.logic import wiki

def test_wiki():
    assert "god" in wiki()


6- Build a cli using python Fire library 
-create a file : touch cli-fire.py and insert :
#!/usr/bin/env python
import fire
from mylib.logic import wiki

if __name__ == '__main__':
  fire.Fire(wiki)

-save and type:
chmod +x cli-fire.py
python cli-fire.py 
python cli-fire.py --name=God(any name that you want to search in wikipedia)
./cli-fire.py --help
./cli-fire.py --name laura

#ANOTHER CODE

import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)

IF YOU RUN python cli-fire.py --name=LAURA  in the second code, the output will be Hello LAURA

-edit logic.py by adding 
def search_wiki(name):
    """Search Wikipedia for Names"""

    results = wikipedia.search(name)
    return results

-type the code below in cli-fire.py;

import fire
from mylib import logic

if __name__=="__main__":
    fire.Fire(logic)

-run the cmd 
./cli-fire.py --help
./cli-fire.py search_wiki "Barack"

7- let's build our api using fastapi
-edit requirements.txt by adding fastapi and uvicorn and run make install, then pip freeze and copy the version into requirements.txt
-edit the main.py file:

#from mylib.logic import wiki

#result = wiki()
#print(result)
             # ex of a lint failure
# result=wiki()
# result=result
# print(result)

#****************let's build our microservice******************
from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}
#first endpoint
@app.get("/search/{value}")
async def add(value: str) :
    """Page to search in wikipedia"""
    result = search_wiki(value)
    return {"result": result}

		#2nd endpoint
@app.get("/wiki/{name}")
async def wiki(name: str) :
    """retrieve info from ikipedia"""
    result = search_wiki(name)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')

	-save and run python main.py, then open in the browser and do your search
    -also open the browser and add /docs or /wiki/(name you want)

       3rd endpoint
it is phrase/name in themain.py file
also create a file test_main.py for this route
install textblob in the rquirements.txt file
adjust test section in the makefile
add def phrase in the logic.py file   















-
>>>>>>> 39a12bbd0854e273e26bcf0e5cd337c440af1458
