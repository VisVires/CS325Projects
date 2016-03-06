CXX = g++
CXXFLAGS = -std=c++0x


TSPSolver = TSPSolver.cpp
TSPSolver += TSPLibFunctions.cpp
TSPSolver += TSPLibFunctions.h


additionalFiles = makefile 


TSPSolver: ${TSPSolver}
	${CXX} ${CXXFLAGS} ${TSPSolver} -o TSPSolver

zip:
	zip TSPSolver ${TSPSolver} ${additionalFiles}

clean:
	rm -f TSPSolver *.o *~
