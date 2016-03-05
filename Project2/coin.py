'''
Project 2 - Coin Change
CS325 
Group 11 - William George, Karen Thrasher, Kyle Livermore

'''

import ast
import sys
import getopt
import csv #Import CSV module
from time import clock
import itertools
from stub import changeslow
from stub import changegreedy
from stub import changedp

def stringTrimmer(coinsString):
	index = coinsString.index("[")
	backIndex = coinsString.index("]") + 1
	return coinsString[index:backIndex]

def runProblemsFromFile(inputFile):
	f = open(inputFile + ".txt", "r")
	array = []
	i = 0
	for line in f:
		if "\r" in line:
			index = line.index("\r")
			line = line[0:index]
		if i % 2 == 0:
			try:
				temp = ast.literal_eval(line)
				if len(temp) > 0:
					array.append(temp)
			except:
				print("Failed to read line in file: " + line)
		else:
			try:
				array.append(int(line))
			except:
				print("Failed to read line in file: " + line)
		i +=1
	f.close()
	print(array)
	output = open(inputFile + "change.txt", "w")
	if len(array) % 2 == 1:
		array  = array[:len(array) - 1]
	for i in range(0, len(array), 2):

		if array[i + 1] > 150 or len(array[i]) > 10:
			output.write("Time required to solve with brute force is too great\n"
						 "thus this case was skipped for the brute force algorithm")
		else:
			coins, slowCoinsUsed = changeslow(array[i], array[i + 1])
			output.write(str(slowCoinsUsed) + "\n")
			output.write(str(coins) + "\n")
		#Run greedy algorithm
		numCoinsGreedy, coinsGreedy = changegreedy(array[i], array[i+1])
		coinsGreedy = stringTrimmer(str(coinsGreedy))
		output.write(coinsGreedy + "\n")
		output.write(str(numCoinsGreedy) + "\n")

		#Run dpAlgorithm
		numCoinsDP, coinsDP = changedp(array[i], array[i+1])
		coinsDP = stringTrimmer(str(coinsDP))
		output.write(coinsDP + "\n")
		output.write(str(numCoinsDP) + "\n")

	output.close()


def runDenominationsTimeCollect():
	V = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
	dataOut = []
	k = 0
	for j in list(range(3, len(V)+1)):
		print("Size of v: " + str(j))
		Vcurrent = V[:j]
		A = 100
		dataOut.append([])
		dataOut[k].append(len(Vcurrent))
		dataOut[k].append(A)
		sumGreedy = 0
		sumDP = 0
		sumSlow = 0
		for i in range(10):
			print(i)
			start = clock()
			changegreedy(Vcurrent, A)
			sumGreedy += clock() - start
			start = clock()
			changedp(Vcurrent, A)
			sumDP += clock() - start
			if(A <= 110 and len(Vcurrent) < 16):
				start = clock()
				changeslow(Vcurrent, A)
				sumSlow += clock() - start
		sumGreedy = sumGreedy / 10
		sumDP = sumDP / 10
		sumSlow = sumSlow / 10
		dataOut[k].append(sumGreedy)
		dataOut[k].append(sumDP)
		dataOut[k].append(sumSlow)
		k += 1
	of = open('VtoTime.csv', "w")
	# set delimiter as Excel delimiter
	writer = csv.writer(of)
	# place arrays in CSV file
	writer.writerow(["V", "A", "Greedy", "DP", "Slow"])
	writer.writerows(dataOut)
	of.close()
	print ("File Output to CSV")

def runTimeDataCollect():
	#repeatMeasurements = 10
	#AForSlow = [10, 17, 25, 37, 50, 67, 75, 89, 100, 113, 125, 150]
	#AForSlow = list(itertools.chain.from_iterable(itertools.repeat(x,repeatMeasurements) for x in AForSlow))
	#AForGreedy = list(range(1,20001))
	#AForGreedy =  [200, 350, 500, 650, 800, 1000, 2000, 3000, 6000, 10000, 20000, 50000]
	#AForGreedy = list(itertools.chain.from_iterable(itertools.repeat(x,repeatMeasurements) for x in AForGreedy))
	#AForDP = [200, 350, 500, 650, 800, 1000, 2000, 3000, 6000, 10000, 20000, 50000 ]
	#AForDP = list(range(1,20001))
	#AForDP = list(itertools.chain.from_iterable(itertools.repeat(x,repeatMeasurements) for x in AForDP))
	AForAll = list(range(1,2000))

	timeForSlow = []
	timeForGreedy = []
	timeForDP = []
	dataOut = []

	print("Collecting data for problem #7.")
	VFour = [1, 5, 7, 13, 17, 23, 31, 41, 47, 59]

	for i in list(range(len(AForAll))):
		print(i)
		dataOut.append([])
		dataOut[i].append(AForAll[i])
		start = clock()
		changegreedy(VFour, AForAll[i])
		dataOut[i].append(clock() - start)
		start = clock()
		changedp(VFour, AForAll[i])
		dataOut[i].append(clock() - start)

		if(AForAll[i] <= 150 ):
			start = clock()
			changeslow(VFour, AForAll[i])
			dataOut[i].append(clock() - start)


	#print("Running Brute Force Algorithm")
	#for i in range(len(AForSlow)):
	#	print(i)
	#	start = clock()
	#	changeslow(VFour, AForSlow[i])
	#	timeForSlow.append(clock() - start)
	#print("Running Greedy Algorithm")
	#print(AForGreedy)
	#for i in range(len(AForGreedy)):
	#	print(i)
	#	start = clock()
	#	changegreedy(VFour, AForGreedy[i])
	#	timeForGreedy.append(clock() - start)
	#print("Running DP Algorithm")
	#for i in range(len(AForDP)):
	#	print(i)
	#	start = clock()
	#	changedp(VFour, AForDP[i])
	#	timeForDP.append(clock() - start)
	#Write time data to file
	of = open('runTime.csv', "w")
	# set delimiter as Excel delimiter
	writer = csv.writer(of)
	# place arrays in CSV file
	#writer.writerow("Slow")
	#writer.writerow(AForSlow)
	#writer.writerow(timeForSlow)
	#writer.writerow("Greedy")
	#writer.writerow(AForGreedy)
	#writer.writerow(timeForGreedy)
	#writer.writerow("DP")
	#writer.writerow(AForDP)
	#writer.writerow(timeForDP)
	#writer.writerow("Coins used")
	#writer.writerow(VFour)
	writer.writerow(["A", "Greedy", "DP", "Slow"])
	writer.writerows(dataOut)
	of.close()
	print ("File Output to CSV")

def _minCoinDataHelper(V, start, stop, step, fileName):
	problem = []
	for i in range(int((stop - start)/step) + 1):
		print(i)
		numCoinsGreedy, coinsGreedy = changegreedy(V, i * step + start)
		numCoinsDP, coinsDP = changedp(V, i * step + start)
		problem.append([])
		problem[i].append(i * step + start)
		problem[i].append(numCoinsGreedy)
		problem[i].append(numCoinsDP)
	#Write time data to file
	of = open(fileName, "w")
	# set delimiter as Excel delimiter
	writer = csv.writer(of)
	# place arrays in CSV file
	writer.writerow(["A","Greedy","DP"])
	writer.writerows(problem)
	of.close()

def _minCoinDataHelperWithSlow(V, start, stop, step, fileName):
	problem = []
	j = 0
	for i in range(int((stop - start)/step) + 1):
		print(i)
		numCoinsSlow, coinsSlow = changeslow(V, i * step + start)
		numCoinsGreedy, coinsGreedy = changegreedy(V, i * step + start)
		numCoinsDP, coinsDP = changedp(V, i * step + start)
		problem.append([])
		problem[j].append(i * step + start)

		problem[j].append(numCoinsGreedy)
		problem[j].append(numCoinsDP)
		problem[j].append(numCoinsSlow)
		j += 1
	#Write time data to file
	of = open(fileName, "w")
	# set delimiter as Excel delimiter
	writer = csv.writer(of)
	# place arrays in CSV file
	writer.writerow(["A", "Greedy", "DP", "Slow"])
	writer.writerows(problem)
	of.close()

def runMinCoinDataCollect():
	VFour = [1, 5, 10, 25, 50]
	VFive1 = [1 ,2, 6, 12, 24, 48, 60]
	VFive2 = [1, 6, 13, 37, 150]
	VSix = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

	#Problem4
	print("Problem 4")
	_minCoinDataHelper(VFour, 2010, 2200, 5, "problem4.csv")
	_minCoinDataHelperWithSlow(VFour, 1, 150, 1, "problem4small.csv")

	#Problem 5a
	print("Problem 5a")
	_minCoinDataHelper(VFive1, 2010, 2200, 5, "problem5a.csv")
	_minCoinDataHelperWithSlow(VFive1, 1, 150, 1, "problem5asmall.csv")

	#Problem 5b
	print("Problem 5b")
	_minCoinDataHelper(VFive2, 2010, 2200, 5, "problem5b.csv")
	_minCoinDataHelperWithSlow(VFive2, 1, 300, 1, "problem5bsmall.csv")

	#Problem 6
	print("Problem 6")
	_minCoinDataHelper(VSix, 2010, 2200, 5, "problem6.csv")
	_minCoinDataHelperWithSlow(VSix, 1, 75, 1, "problem6small.csv")

def main(argv):
	#print (changegreedy(coins, n))
	#print (changedp(coins, n))
	#print (changedp2(coins, n))
	#print (changeslow(coins, n))
	try:
		# parse command line inputs
		opts, args = getopt.getopt(argv, "i:", ["ifile=", "minCoin", "runTimeData", "denominationsTime"] )
	except getopt.GetoptError:
		print("coin.py -i <inputFile>\n")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("coin.py -i <inputFile>\n")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputFile = arg
			runProblemsFromFile(inputFile)
		elif opt in ("--runTimeData"):
			#Run the run time cases and output data files
			runTimeDataCollect()
		elif opt in ("--minCoin"):
			runMinCoinDataCollect()
		elif opt in ("--denominationsTime"):
			runDenominationsTimeCollect()
		else:
			print("coin.py -i <inputFile>\n")
			sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])