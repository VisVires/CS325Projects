'''
Project 1 - Maximum Sum Subarray
CS325 
Group 11 - Karen Thrasher, William George, Kyle Livermore
'''

import timeit #Include for timing code
import ast

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
def fileOutputCSV():
	print "File Output CSV"
#Creates array of random numbers
def randomArray():
	print "Random array"


#Algorithm 1 - Enumeration
def a1():
	print "Algorithm 1 - Enumeration"


#Algorithm 2 - Better Enumeration
def a2():
	print "Algorithm 2 - Better Enumeration"


#Algorithm 3 - Divide and Conquer
def a3():
	print "Algorithm 3 - Divide and Conquer"


#Algorithm 4 - Linear-time
def a4():
	print "Algorithm 3 - Divide and Conquer"


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