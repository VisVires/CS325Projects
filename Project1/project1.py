'''
Project 1 - Maximum Sum Subarray
CS325 
Group 11 - Karen Thrasher, William George, Kyle Livermore
'''

import timeit #Include for timing code
import ast
import random
import sys
import getopt
import csv #Import CSV module
from time import clock

#File input
def fileInput(fileName):
	f = open(fileName, "r")
	i = 0
	array = []
	for line in f:
		try:
			array.append( ast.literal_eval(line))
		except:
			print("Failed to read line in file: " + line)
	f.close()
	return array


#File output for grading
def fileOutput(fileName, startingArrays, MaxArrays):
	f = open(fileName, "w")
	for i in range(len(MaxArrays)):
		f.write(str(startingArrays[int(i/4)]) + "\n")
		f.write(str(MaxArrays[i]) + "\n")
		sumArray = [int(j) for j in MaxArrays[i]]
		f.write(str(sum(sumArray)) + "\n\n")
	f.close()


#File output of data for analysis
def fileOutputCSV(startingArrays, maxArrays):
	# set output file as write file
	of = open('output.csv', 'wb') 
	# set delimiter as Excel delimiter
	writer = csv.writer(of)
	# place arrays in CSV file
	writer.writerows(startingArrays)
	writer.writerows(maxArrays)
	of.close
	print ("File Output CSV")


#Creates array of random numbers
def randomArray(n, seed = 0):
	# set seed
	if seed != 0:
		random.seed(seed)
	randArray = []
	# build random array
	for i in range(n):
		randArray.append(random.randrange(-100,100))
	return randArray

#Algorithm 1 - Enumeration
def a1(array):
	currentSum = 0
	currentSumStart= 0
	maxSum = float("-inf")
	maxSumStart = 0
	maxSumFinish = 0
	#outer loop advance i
	for i in range(len(array)):
		currentSumStart = i
		if currentSum > maxSum:
			maxSum = currentSum
			maxSumStart = i
			maxSumFinish = i
		# set range to array length - i - 1
		# inner loop advance j
		for j in range(len(array) - i - 1):
			#set current sum to sum of elements from i to j
			currentSum = sum(array[i:j+i+2])
			# check if > max sum and reset max sum to current sum
			# set max sub-array start and finish
			if currentSum > maxSum:
				maxSum = currentSum
				maxSumStart = currentSumStart
				maxSumFinish = j+i+1
	maxArray = array[maxSumStart : maxSumFinish + 1]
	return maxArray, maxSum


#Algorithm 2 - Better Enumeration
def a2(array):
	currentSum = 0
	currentSumStart= 0
	maxSum = float("-inf")
	maxSumStart = 0
	maxSumFinish = 0
	# outer loop advance i
	for i in range(len(array)):
		currentSum = array[i]
		currentSumStart = i
		if currentSum > maxSum:
			maxSum = currentSum
			maxSumStart = i
			maxSumFinish = i
		# inner loop advance j
		for j in range(len(array) - i - 1):
			# add j+1 to current sum
			currentSum += array[j+i+1]
			# check if current sum is greater than maxSum
			# Set start and finish if new max sub-array
			if currentSum > maxSum:
				maxSum = currentSum
				maxSumStart = currentSumStart
				maxSumFinish = j+i+1
	maxArray = array[maxSumStart : maxSumFinish + 1]
	return maxArray, maxSum



#Algorithm 3 - Divide and Conquer
def a3(array):
	if (len(array) == 0):
		return 0
	start = 0
	end = len(array)-1
	low, high, maxSum = maxDivAndConq(array, start, end)
	return array[low:high+1] , maxSum

def findMaxArr(A, left, mid, right):
	# Find Left Max
	leftSum = float('-inf')
	currSum = 0
	maxLeft = maxRight = 0
	for i in range(mid, left -1, -1):
		currSum = currSum + A[i]
		if currSum > leftSum:
			leftSum = currSum
			maxLeft = i
	# Find Right Max
	rightSum = float('-inf')
	currSum = 0
	for j in range(mid + 1, right + 1, 1):
		currSum = currSum + A[j]
		if currSum > rightSum:
			rightSum = currSum
			maxRight = j
	return (maxLeft, maxRight, leftSum + rightSum)

def maxDivAndConq(A, low, high):
	# base case
	if (high == low):
		return (low, high, A[low])
	else:
		# find mid element
		mid = int((low + high) / 2)
		# get left right and prefix+suffix subarrays
		leftLow, leftHigh, leftSum = maxDivAndConq(A, low, mid)
		rightLow, rightHigh, rightSum = maxDivAndConq(A, mid + 1, high)
		midLow, midHigh, midSum = findMaxArr(A, low, mid, high)
		# find greatest subarray
		if (leftSum >= rightSum and leftSum >= midSum):
			# print "left" 
			# print leftLow, leftHigh, leftSum
			return  leftLow, leftHigh, leftSum
		elif (rightSum >= leftSum and rightSum >= midSum):
			# print "right" 
			# print rightLow, rightHigh, rightSum
			return rightLow, rightHigh, rightSum
		else:
			# print "middle" 
			# print midLow, midHigh, midSum
			return midLow, midHigh, midSum

#Algorithm 4 - Linear-time
def a4(array):
	maxSum = 0
	maxStartIndex = 0
	maxEndIndex = 0
	maxCurrent = 0
	startIndex = 0
	endIndex = 0
	for i in range(len(array)):
		maxCurrent = maxCurrent + array[i]
		if maxCurrent < 0:
			maxCurrent = 0
			startIndex = i+1
			endIndex = i+1
		else:
			endIndex = i
			if maxCurrent > maxSum:
				maxSum = maxCurrent
				maxStartIndex = startIndex
				maxEndIndex = endIndex
	maxArray = array[maxStartIndex : maxEndIndex + 1]
	return maxArray, maxSum


def main(argv):
	inputFile = ""
	outputFile = ""
	try:
		opts, args = getopt.getopt(argv, "i:o:", ["ifile=", "ofile=", "runTimeData"] )
	except getopt.GetoptError:
		print("project1.py -i <inputFile> -o <outputFile> --runTimeData\n"
              "program must be run with either input and output files or the option --runTimeData, runtime data an\n"
                  "optional parameter that outputs a csv with algoritm runtime data.")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("project1.py -i <inputFile> -o <outputFile> --runTimeData\n"
              "program must be run with either input and output files or the option --runTimeData, runtime data an\n"
                  "optional parameter that outputs a csv with algoritm runtime data.")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputFile = arg
		elif opt in ("-o", "--ofile"):
			outputFile = arg
		elif opt in ("--runTimeData"):
			#Run each algorithm on the counterpart list of n 10x collecting time data and output time data to a .csv
			nForA1 = [20, 40, 80, 160, 200, 350, 500, 650, 800, 1000]
			nForA2 = [20, 40, 80, 160, 200, 350, 500, 650, 800, 1000]
			nForA3 = [20, 40, 80, 160, 200, 350, 500, 650, 800, 1000]
			nForA4 = [20, 40, 80, 160, 200, 350, 500, 650, 800, 1000]
			timeForA1 = []
			timeForA2 = []
			timeForA3 = []
			timeForA4 = []

			for i in range(len(nForA1)):
				print(i)
				timeForA1.append([])
				for j in range(10):
					start = clock()
					a1(randomArray(nForA1[i]))
					timeForA1[i].append(clock() - start)
			print(timeForA1)

			for i in range(len(nForA2)):
				print(i)
				timeForA2.append([])
				for j in range(10):
					start = clock()
					a2(randomArray(nForA2[i]))
					timeForA2[i].append(clock() - start)
			print(timeForA2)

			for i in range(len(nForA3)):
				print(i)
				timeForA3.append([])
				for j in range(10):
					start = clock()
					a3(randomArray(nForA3[i]))
					timeForA3[i].append(clock() - start)
			print(timeForA3)

			for i in range(len(nForA4)):
				print(i)
				timeForA4.append([])
				for j in range(10):
					start = clock()
					a4(randomArray(nForA4[i]))
					timeForA4[i].append(clock() - start)
			print(timeForA4)


	if inputFile == "" or outputFile == "":
		print(inputFile + ", " + outputFile)
		print("project1.py -i <inputFile> -o <outputFile> --runTimeData\n"
              "program must be run with either input and output files or the option --runTimeData, runtime data an\n"
                  "optional parameter that outputs a csv with algoritm runtime data.")
	else:
		#run each algorithm here
		answers = []
		arraysFromFile = fileInput(inputFile)
		for i in arraysFromFile:
			array, sum = a1(i)
			answers.append(array)
			array, sum = a2(i)
			answers.append(array)
			array, sum = a3(i)
			answers.append(array)
			array, sum = a4(i)
			answers.append(array)

		fileOutput(outputFile, arraysFromFile, answers)

if __name__ == "__main__":
	main(sys.argv[1:])

'''
Sample timing code:
timer = timeit.Timer(stmt='fibIterative(500000)', setup='from __main__ import fibIterative')
print timer.timeit(number=10)
#Reference: http://www.dreamincode.net/forums/topic/288071-timeit-module/
'''