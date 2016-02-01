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

# table based dynamic programming algorithm
def changedp(coins, change):
	# make 0 multidimensional array with dimensions amount x len(coins) 
	minCoins = [[0] * (change + 1) for c in range(len(coins) + 1)]
	coinsUsed = [0] * (change + 1)
	coinList = {}
	for c in coins:
		coinList.setdefault(c, 0)
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
		coinList[coinsUsed[remainder]] = coinList[coinsUsed[remainder]] + 1  
 		finalList.append(coinsUsed[remainder])
 		remainder = remainder - coinsUsed[remainder]
 	# end while
	return minCoins[len(coins)][change], coinList.values()

 # greedy algorithm
def changegreedy(coins, change):
 	coinsReturned = []
 	coinsUsed = 0
 	remainder = change
 	coinList = {}
 	for c in coins:
		coinList.setdefault(c, 0)
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
 				coinList[c] = coinList[c] + 1
 				remainder = remainder - c
 				coinsUsed = coinsUsed + 1
 	return coinsUsed, coinList.values()
'''
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
'''

#Brute Force
#Reference algorithm
	#https://www.youtube.com/watch?v=EScqJEEKC10
#Reference yield
	#http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
#Reference pass
	#http://www.tutorialspoint.com/python/python_pass_statement.htm
def changeslow(available_coins, n, used_coins):
	#If sum equals target - found
	if sum(used_coins) == n:
		yield used_coins 
	#If sum greater than target, pass as cannot be greater than target
	elif sum(used_coins) > n:
		pass
	#If coins available are all used then pass
	elif available_coins ==[]:
		pass
	else:
		#Same coins available, number of coins so far plus first coin available
		#Allows for multiple occurences of same coin in list
		for c in changeslow(available_coins[:], n, used_coins+[available_coins[0]]):
			yield c
		#Remove first coin available and then check remaining
		#Allows to remove first coin in list and check other alternatives
		for c in changeslow(available_coins[1:], n, used_coins):
			yield c

def slow_helper(coins, n):
	solutions = [s for s in changeslow(coins, n, [])]
	#Displays possible solutions:
	#for s in solutions:
	#	print s
	
	#print "Optimal Solution:", min(solutions, key=len)
	#print optimal_sol = min(solutions, key=len)
	#print optimal_length = len(optimal_sol)
	return min(solutions, key=len)

def main():
	print "Test Case 1:"
	print "All return C=[1,1,1,1] m=4"
	blank_coins =[]
	coins = [1,2,4,8]
	n = 15

	print "Dynamic:"
	print (changedp(coins, n))

	print "Greedy:"
	print (changegreedy(coins, n))

	print "Brute Force:"
	optimal_sol = slow_helper(coins, n)
	optimal_len = len(optimal_sol)
	brute_optimal = [optimal_len, optimal_sol]
	print brute_optimal

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
	optimal_sol = slow_helper(coins, n)
	optimal_len = len(optimal_sol)
	brute_optimal = [optimal_len, optimal_sol]
	print brute_optimal

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
	optimal_sol = slow_helper(coins, n)
	optimal_len = len(optimal_sol)
	brute_optimal = [optimal_len, optimal_sol]
	print brute_optimal


main()