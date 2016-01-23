'''
Project 1 - Maximum Sum Subarray
CS325 
Group 11 - Karen Thrasher, William George, Kyle Livermore

TESTING ALGORITHMS
'''
import timeit #Include for timing code
import ast
import random
import sys
import getopt
import csv #Import CSV module
from time import clock
import itertools

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
	#return maxSubarray and sum of Array
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
			return  leftLow, leftHigh, leftSum
		elif (rightSum >= leftSum and rightSum >= midSum):
			return rightLow, rightHigh, rightSum
		else:
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

def main():
	print "Test Array:"
	testArray = randomArray(10,2)
	print testArray[:]

	print "Algorithm 1:"
	resultA1 = a1(testArray)
	print resultA1[:]

	print "Algorithm 2:"
	resultA2 = a2(testArray)
	print resultA2[:]

	print "Algorithm 3:"
	resultA3 = a3(testArray)
	print resultA3[:]

	print "Algorithm 4:"
	resultA4= a4(testArray)
	print resultA4[:]

	print "Known Array:"
	knownArray = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]

	print "Algorithm 1:"
	kresultA1 = a1(knownArray)
	print kresultA1[:]

	print "Algorithm 2:"
	kresultA2 = a2(knownArray)
	print kresultA2[:]

	print "Algorithm 3:"
	kresultA3 = a3(knownArray)
	print kresultA3[:]

	print "Algorithm 4:"
	kresultA4 = a4(knownArray)
	print kresultA4[:]

main()