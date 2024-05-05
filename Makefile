#PORT = 8891
PORT = 8888

#--------
# Lab
#--------
run runl:
	jupyter lab --port $(PORT) --NotebookeApp.token='' --NotebookApp.password=''

	
    #jupyter lab --port $(PORT) --ip "*" --NotebookeApp.token='' --NotebookApp.password=''

