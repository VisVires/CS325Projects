n = 63
coins = [1,5,10,25]

def coinCountRecurse(coins, change):
	# set new minCoins
	minCoins = change
	if change in coins:
		return 1
	else:
		# Iterate through all coins
		for i in coins:
			# if coins are less than remaining change
			if i <= change:
				# add minimum coins to numCoins
				numCoins = 1 + coinCountRecurse(coins, change - i)
				# if num coins is less than current minimum, set new minimum
				if numCoins < minCoins:
					minCoins = numCoins
		return minCoins
	

def coinCountMemo(coins, change, memo):
	#set new minCoins
	minCoins = change
	# if change is one of our starting denominations return
	if change in coins:
		memo[change] = 1
		return 1
	# if change has already been calculated return
	elif memo[change] > 0:
		return memo[change]
	else:
		# For each coin check if less than change
		for i in coins:
			if i <= change:
				# recursively find next smallest change
				numCoins = 1 + coinCountDP(coins, change - i, memo)
				# if less than minCoins add to memo
				if numCoins < minCoins:
					minCoins = numCoins
					memo[change] = minCoins
	return minCoins

# Bottom-up DP
def coinCountDP(coins, change, minCoins):
	for cents in range(change+1):
		# Set min
		totalCoins = cents
		# Iterate through each coin that is less than cents
		for c in coins:
			if c <= cents:
				# find the minimum number of coins needed to make cents and place in minCoins list
				if minCoins[cents - c] + 1 < totalCoins:
					totalCoins = minCoins[cents - c] + 1
		minCoins[cents] = totalCoins
	return minCoins[change]

def coinCountGreedy(coins, change, coinsReturned):
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


print (coinCountGreedy(coins, n, []))
print (coinCountDP(coins, n, [0]*(n+1)))
print (coinCountRecurse(coins, n))
print (coinCountDP(coins, n, [0]*(n+1)))		