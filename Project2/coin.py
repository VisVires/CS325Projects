n = 63
coins = [1,5,10,25]
 
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
 	
 
# def coinCountMemo(coins, change, memo):
#  	#set new minCoins
#  	minCoins = change
#  	# if change is one of our starting denominations return
#  	if change in coins:
#  		memo[change] = 1
#  		return 1
#  	# if change has already been calculated return
#  	elif memo[change] > 0:
#  		return memo[change]
#  	else:
#  		# For each coin check if less than change
#  		for i in coins:
#  			if i <= change:
#  				# recursively find next smallest change
#  				numCoins = 1 + coinCountDP(coins, change - i, memo)
# 				# if less than minCoins add to memo
#  				if numCoins < minCoins:
#  					minCoins = numCoins
#  					memo[change] = minCoins
#  	return minCoins
 
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
 		coinsUsed[amount] = coin
 	# end for
 	finalList = []
 	remainder = change
 	while remainder > 0:
 		print coinsUsed[remainder]
 		finalList.append(coinsUsed[remainder])
 		remainder = remainder - coinsUsed[remainder]
 	return minCoins[change], finalList
 
def changegreedy(coins, change):
 	coinsReturned = []
 	coinsUsed = 0
 	if change in coins:
 		coinsReturned.append(change)
 		coinsUsed = 1
 		return coinsUsed, coinsReturned
 	else:
 		coinSort = sorted(coins, reverse=True)
 		for c in coinSort:
 			while change > 0 and c <= change:
 				coinsReturned.append(c)
 				change = change - c
 				coinsUsed = coinsUsed + 1
 	return coinsUsed, coinsReturned
 
 
print (changegreedy(coins, n))
print (changedp(coins, n))
print (changeslow(coins, n))