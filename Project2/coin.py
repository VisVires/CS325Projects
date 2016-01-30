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
 
# slow recursive algorithm 
def changeslow(coins, change):
	# set new minCoins
	minCoins = change
	finalList = []
	if change in coins:
		return 1
	else:
	# Iterate through all coins
 		for c in coins:
 			# if coins are less than remaining change
 			if c <= change:
 				# add minimum coins to numCoins
 				numCoins = 1 + changeslow(coins, change - c)
 				# if num coins is less than current minimum, set new minimum
 				if numCoins < minCoins:
 					minCoins = numCoins
 	return minCoins
 	
 
 # Bottom-up DP
def changedp(coins, change):
	minCoins = [0] * (change + 1)
	coinsUsed = [0] * (change + 1)
	coin = 1
 	for amount in range(change + 1):
 		# Set min
		totalCoins = amount
 		# Iterate through each coin that is less than amount
 		for c in coins:
 			if c <= amount:
 				# find the minimum number of coins needed to make amount and place in minCoins list
 				if minCoins[amount - c] + 1 < totalCoins:
 					totalCoins = minCoins[amount - c] + 1
 					coin = c
 		# end for
 		minCoins[amount] = totalCoins
 		# print minCoins
 		coinsUsed[amount] = coin
 	# end for
 	finalList = []
 	remainder = change
 	# move backwards through array to get used coins for finalList
 	while remainder > 0:
 		finalList.append(coinsUsed[remainder])
 		remainder = remainder - coinsUsed[remainder]
 	# end while
 	return minCoins[change], finalList
		
# table based dynamic programming algorithm
def changedp2(coins, change):
	# make 0 multidimensional array with dimensions amount x len(coins) 
	minCoins = [[0] * (change + 1) for c in range(len(coins) + 1)]
	coinsUsed = [0] * (change + 1)
	# preset each value for first row as inf
	for amount in range(1, change + 1):
		minCoins[0][amount] = float('inf')
	# end for
	
	# iterate through coins for each amount
	for c in range(1, len(coins) + 1):
		for amount in range(1, change + 1):
			# check if coin denomination is less than amount
			if coins[c - 1] <= amount:
				low = minCoins[c][amount-coins[c - 1]]
			if minCoins[c-1][amount] <= 1 + low:
				minCoins[c][amount] = minCoins[c-1][amount]
			else:
				minCoins[c][amount] = 1 + low
				coinsUsed[amount] = coins[c-1]
		# end for
	# end for
	finalList = []
 	remainder = change
 	# move backwards through array to get used coins for finalList
 	while remainder > 0:
 		finalList.append(coinsUsed[remainder])
 		remainder = remainder - coinsUsed[remainder]
 	# end while
	return minCoins[len(coins)][change], finalList

# greedy algorithm
def changegreedy(coins, change):
 	coinsReturned = []
 	coinsUsed = 0
 	remainder = change
 	# check if coin denomination exists in array
 	if change in coins:
 		coinsReturned.append(change)
 		coinsUsed = 1
 		return coinsUsed, coinsReturned
 	else:
 		# sort list in descending order
 		coinSort = sorted(coins, reverse=True)
 		# iterate through sorted list
 		for c in coinSort:
 			# while coin is less than remainder subtract coin 
 			# add to returned array
 			while c <= remainder:
 				coinsReturned.append(c)
 				remainder = remainder - c
 				coinsUsed = coinsUsed + 1
 	return coinsUsed, coinsReturned


def runProblemsFromFile(inputFile):
	f = open(inputFile + ".txt", "r")
	array = []
	for line in f:
		if "\r" in line:
			index = line.index("\r")
			line = line[0:index]
		try:
			temp = ast.literal_eval(line)
			if len(temp) > 0:
				array.append(temp)
		except:
			print("Failed to read line in file: " + line)
	f.close()

	output = open(inputFile + "change.txt", "w")
	if len(array) % 2 == 1:
		array  = array[:len(array) - 1]
	for i in range(0, len(array), 2):
		if array[i + 1] > 50 or len(array[i]) > 10:
			output.write("Time required to solve with brute force is too great\n"
						 "thus this case was skipped for the brute force algorithm")
		else:
			coins = changeslow(array[i], array[i + 1])
			output.write(str(coins) + "\n") #Needs to be changed to the array of coins when the algorithm is fixed
			output.write(str(coins) + "\n")
		#Run greedy algorithm
		numCoinsGreedy, coinsGreedy = changegreedy(array[i], array[i+1])
		output.write(str(coinsGreedy) + "\n")
		output.write(str(numCoinsGreedy) + "\n")

		#Run dpAlgorithm
		numCoinsDP, coinsDP = changedp(array[i], array[i+1])
		output.write(str(coinsDP) + "\n")
		output.write(str(numCoinsDP) + "\n")

	output.close()


def runTimeDataCollect():
	repeatMeasurements = 10
	AForSlow = [10, 20, 40, 80, 160, 200, 350, 500, 650, 800, 1000, 1500]
	AForSlow = list(itertools.chain.from_iterable(itertools.repeat(x,repeatMeasurements) for x in nForA1))
	AForGreedy = [20, 40, 80, 160, 200, 350, 500, 650, 800, 1000, 2000, 3000]
	AForGreedy = list(itertools.chain.from_iterable(itertools.repeat(x,repeatMeasurements) for x in nForA2))
	AForDP = [10, 25, 63, 156, 391, 977, 2442, 6104, 15259, 38147, 95368, 238419 ]
	AForDP = list(itertools.chain.from_iterable(itertools.repeat(x,repeatMeasurements) for x in nForA3))
	AForDP2 = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
	AForDP2 = list(itertools.chain.from_iterable(itertools.repeat(x,repeatMeasurements) for x in nForA4))

	timeForSlow = []
	timeForGreedy = []
	timeForDP = []
	timeForDP2 = []

 	print("Collecting data for problem #7.")
	VFour = [1, 5, 10, 25, 50]
	print("Running Brute Force Algorithm")
 	for i in range(len(AForSlow)):
		print(i)
		start = clock()
		changeslow(VFour, AForSlow[i])
		timeForSlow.append(clock() - start)
	print("Running Greedy Algorithm")
 	for i in range(len(AForGreedy)):
		print(i)
		start = clock()
		changegreedy(VFour, AForSlow[i])
		timeForGreedy.append(clock() - start)
	print("Running DP Algorithm")
 	for i in range(len(AForDP)):
		print(i)
		start = clock()
		changedp(VFour, AForSlow[i])
		timeForDP.append(clock() - start)
	#Write time data to file
	of = open('runTime.csv', mode)
	# set delimiter as Excel delimiter
	writer = csv.writer(of)
	# place arrays in CSV file
	writer.writerow("Slow")
	writer.writerow(AForSlow)
	writer.writerow(timeForSlow)
	writer.writerow("Greedy")
	writer.writerow(AForGreedy)
	writer.writerow(timeForGreedy)
	writer.writerow("DP")
	writer.writerow(AForDP)
	writer.writerow(timeForDP)
	of.close
	print ("File Output to CSV")

def _minCoinDataHelper(V, start, stop, step, fileName):
	problem = []
	for i in range((start - stop)/step + 1):
		numCoinsGreedy, coinsGreedy = changegreedy(VFour, i * step + start)
		numCoinsDP, coinsDP = changedp(VFour, i * step + start)
		problem.append([])
		problem[i].append(i * step + start)
		problem[i].append(coinsGreedy)
		problem[i].append(coinsDP)
	#Write time data to file
	of = open(fileName, mode)
	# set delimiter as Excel delimiter
	writer = csv.writer(of)
	# place arrays in CSV file
	writer.writerheader(["A","Greedy","DP"])
	writer.writerows(problem)
	of.close()

def _minCoinDataHelperWithSlow(V, start, stop, step, fileName):
	problem = []
	for i in range((start - stop)/step + 1):
		numCoinsSlow, coinsSlow = changeslow(VFour, i * step + start)
		numCoinsGreedy, coinsGreedy = changegreedy(VFour, i * step + start)
		numCoinsDP, coinsDP = changedp(VFour, i * step + start)
		problem.append([])
		problem[i].append(i * step + start)
		problem[i].append(coinsSlow)
		problem[i].append(coinsGreedy)
		problem[i].append(coinsDP)
	#Write time data to file
	of = open(fileName, mode)
	# set delimiter as Excel delimiter
	writer = csv.writer(of)
	# place arrays in CSV file
	writer.writerheader(["A", "Slow ","Greedy","DP"])
	writer.writerows(problem)
	of.close()

def runMinCoinDataCollect():
	VFour = [1, 5, 10, 25, 50]
	VFive1 = [1 ,2, 6, 12, 24, 48, 60]
	VFive2 = [1, 6, 13, 37, 150]
	VSix = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

	#Problem4
	_minCoinDataHelper(VFour, 2010, 2200, 5, "problem4.csv")
	_minCoinDataHelperWithSlow(VFour, 50, 200, 1, "problem4small.csv")

	#Problem 5a
	_minCoinDataHelper(VFive1, 2010, 2200, 5, "problem5a.csv")
	_minCoinDataHelperWithSlow(VFive1, 50, 200, 1, "problem5asmall.csv")

	#Problem 5b
	_minCoinDataHelper(VFive2, 2010, 2200, 5, "problem5b.csv")
	_minCoinDataHelperWithSlow(VFive2, 50, 200, 1, "problem5bsmall.csv")

	#Problem 6
	_minCoinDataHelper(VSix, 2010, 2200, 5, "problem6.csv")
	_minCoinDataHelperWithSlow(VSix, 50, 200, 1, "problem6small.csv")

def main(argv):
	#print (changegreedy(coins, n))
	#print (changedp(coins, n))
	#print (changedp2(coins, n))
	#print (changeslow(coins, n))
	try:
		# parse command line inputs
		opts, args = getopt.getopt(argv, "i:", ["ifile=", "minCoin", "runTimeData"] )
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
		else:
			print("coin.py -i <inputFile>\n")
			sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])