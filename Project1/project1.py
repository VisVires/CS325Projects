'''
Project 1 - Maximum Sum Subarray
CS325 
Group 11 - Karen Thrasher, William George, Kyle Livermore
'''

import timeit #Include for timing code
import ast
import random
import csv #Import CSV module

#File input
def fileInput(fileName):
	f = open(fileName, "r")
	i = 0
	array = []
	for line in f:
		array.append( ast.literal_eval(line))
	f.close()
	return array


#File output for grading
def fileOutput(fileName, startingArrays, MaxArrays):
	f = open(fileName, "w")
	for i in range(len(startingArrays)):
		f.write(str(startingArrays[i]) + "\n")
		f.write(str(MaxArrays[i]) + "\n")
		f.write(str(sum(MaxArrays[i])) + "\n\n")
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
	print "File Output CSV"


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
	return maxArray


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
	return maxArray


#Algorithm 3 - Divide and Conquer
def a3():
	print "Algorithm 3 - Divide and Conquer"


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
	return maxArray


def main():

	fileInput()

	randomArray()

	a1()
	a2()
	a3()
	a4()

	fileOutput()

main()

'''
Sample timing code:
timer = timeit.Timer(stmt='fibIterative(500000)', setup='from __main__ import fibIterative')
print timer.timeit(number=10)
#Reference: http://www.dreamincode.net/forums/topic/288071-timeit-module/
'''