'''
Project 4 - TSP
CS325
Group 11 - William George, Karen Thrasher, Kyle Livermore

'''

import sys
import csv
import math
import getopt
from time import clock

def readFile(fileName):
    f = open(fileName, "r")
    map = []
    i=0
    try:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            map.append([])
            for j in range(3):
                map[i].append(int(row[j]))
            i += 1
    except:
        print("Failed to read file")
    f.close()
    return map

def genAdjMatrix(map):
    adjMatrix = []
    for i in range(len(map)):
        adjMatrix.append([])
        for j in range(len(map)):
            dist = math.sqrt(math.pow(map[i][1] - map[j][1], 2) + math.pow(map[i][2] - map[j][2], 2))
            adjMatrix[i].append(int(round(dist)))
    return adjMatrix

def calcTourLen(tour, adjMatrix):
    tourLen = 0
    tourLen += adjMatrix[tour[0]][tour[len(tour)-1]]
    for i in range(len(tour)-1):
        tourLen += adjMatrix[tour[i]][tour[i+1]]
    return tourLen

def outputTourToFile(fileName, tour, tourLen):
    fOut = open(fileName, "w")
    fOut.write(str(tourLen) + "\n")
    for i in tour:
        fOut.write(str(i) + "\n")
    fOut.close()

def main(argv):
    try:
    # parse command line inputs
        opts, args = getopt.getopt(argv, "i:", ["ifile=", "minCoin", "runTimeData", "denominationsTime"] )
    except getopt.GetoptError:
        print("TSPsolver.py -i <inputFile>\n")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("coin.py -i <inputFile>\n")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        else:
            print("coin.py -i <inputFile>\n")
            sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])