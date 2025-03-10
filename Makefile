#make install will upgrade pip and install all the packages i have in my requirements.txt file and pip freeze allow me to see all the 
#installed package
#after pip freeze, open your requirements.txt and replace all packages with the packages and version from pip freeze and run
#make install again
install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
#format our codes
format:
	#format code
	black *.py mylib/*.py
#check the syntax of the source code
lint:
	#flake8 or #pylint 
	pylint --disable=R,C *.py mylib/*.py 
#test:
	#test
#	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build image
	docker build -t deploy-fastapi .
run:
	#create container
	docker run -p 127.0.0.1:8080:8080 17844381f791
deploy:
	#deploy
#to run 1 command, we type : make install for ex or make lint...
#to run these command at once, we type:
all:install format lint test deploy
