'''
Project 2 - Coin Change
CS325 
Group 11 - William George, Karen Thrasher, Kyle Livermore

STUB FOR TESTING
'''

import ast
import sys
import getopt
import csv #Import CSV module
from time import clock
import itertools

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

def main():
	print "Test Case 1:"
	print "All return C=[1,1,1,1] m=4"
	coins = [1,2,4,9]
	n = 15

	print "Dynamic:"
	print (changedp(coins, n))

	print "Greedy:"
	print (changegreedy(coins, n))

	print "Brute Force:"
	print (changeslow(coins, n))

	print"\n"

	print "Test Case 2:"
	coins = [1,3,7,12]
	n = 29

	print "Dynamic:"
	print "Should return C=[0,1,2,1] m=4"
	print (changedp(coins, n))

	print "Greedy:"
	print "Should return C=[2,1,0,2] m=5"
	print (changegreedy(coins, n))

	print "Brute Force:"
	print "Should return C=[0,1,2,1] m=4"
	print (changeslow(coins, n))

	print"\n"

	print "Test Case 3:"
	print "All return C=[0,0,1,2] m=3"
	coins = [1,3,7,12]
	n = 31

	print "Dynamic:"
	print (changedp(coins, n))

	print "Greedy:"
	print (changegreedy(coins, n))

	print "Brute Force:"
	print (changeslow(coins, n))


main()