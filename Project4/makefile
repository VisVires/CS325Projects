CXX = g++
CXXFLAGS = -std=c++0x


TSPSolver = TSPSolver.cpp
TSPSolver += TSPLibFunctions.cpp
TSPSolver += TSPLibFunctions.h
TSPSolver += cristof/tsp.h
TSPSolver += cristof/tsp.cpp
TSPSolver += cristof/cristof.h
TSPSolver += cristof/cristof.cpp

additionalFiles = makefile 


TSPSolver: ${TSPSolver}
	${CXX} ${CXXFLAGS} ${TSPSolver} -o TSPSolver

zip:
	zip TSPSolver ${TSPSolver} ${additionalFiles}

clean:
	rm -f TSPSolver *.o *~
