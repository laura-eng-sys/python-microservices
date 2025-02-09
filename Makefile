install:
	#install commands
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