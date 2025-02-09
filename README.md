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



























-
>>>>>>> 39a12bbd0854e273e26bcf0e5cd337c440af1458
