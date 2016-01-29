'''
Project 2 - Coin Change
CS325 
Group 11 - William George, Karen Thrasher, Kyle Livermore

'''

n = 63
coins = [1,5,10,21,25]
 
def changeslow(coins, change):
	# set new minCoins
	minCoins = change
	usedCoins = []
	if change in coins:
		return 1
 	else:
 		# Iterate through all coins
 		for i in coins:
 			# if coins are less than remaining change
 			if i <= change:
 				# add minimum coins to numCoins
 				numCoins = 1 + changeslow(coins, change - i)
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
 
 
def main():
	print (changegreedy(coins, n))
	print (changedp(coins, n))
	print (changeslow(coins, n))

main()