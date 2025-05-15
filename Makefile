	CURRENT_DIR = $(shell pwd)
	PROJET_DIR = $(CURRENT_DIR)/projet

	all : 
		pip3 install python-sat
		pip3 install python-constraint
		export PYTHONPATH=$(PROJET_DIR):$$PYTHONPATH ; \
		python3 $(PROJET_DIR)/etape1/Etape1.py > log ; \
		python3 $(PROJET_DIR)/etape2/Etape2.py >> log ; \
		python3 $(PROJET_DIR)/etape3/Etape3.py >> log ; \
		python3 $(PROJET_DIR)/etape4/Etape4.py >> log ; \
		python3 $(PROJET_DIR)/etape5/Etape5.py >> log ; \
		python3 $(PROJET_DIR)/outils/Lieu.py  >> log; \
		python3 $(PROJET_DIR)/outils/Fils.py >> log ; \
		python3 $(PROJET_DIR)/outils/GrapheDeLieux.py  >> log; \
		python3 $(PROJET_DIR)/solvers/SolverAStar.py >> log ; \
		python3 $(PROJET_DIR)/solvers/SolverCSP.py  >> log; \
		python3 $(PROJET_DIR)/solvers/SolverHC.py >> log ; \
		python3 $(PROJET_DIR)/solvers/SolverSAT.py >> log ; \
		python3 $(PROJET_DIR)/solvers/SolverTabou.py >> log

	clear :
		\rm log



