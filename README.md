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

2-#sourcing python virtual environment: vim inside ~/.bashrc and paste the line below at the bottom: source ~/.venv/bin/activate

3-create empty files: requirements.txt Dockerfile Makefile

4-create a folder mylib as our project library. cd inside this folder and create files init.py; logic.py(to keep our source code. we can also use these cmds: mkdir mylib touch mylib/init.py

5- create a file called main.py for our infrastructure
**********************************************************
1- let's populate the makefile