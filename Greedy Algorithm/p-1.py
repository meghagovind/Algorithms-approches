#Problem:
# 1. Given coins [1¢, 5¢, 10¢, 25¢] and an amount (e.g., 36¢), find the minimum number of coins needed.

# Greedy Approach: Always pick the largest possible coin first.
# Algorithm Steps:
# Sort coins in descending order → [25¢, 10¢, 5¢, 1¢].
# While amount > 0:
# Take the largest coin ≤ remaining amount.
# Subtract its value from the amount.
# Count the coin.
# Repeat until amount = 0.

def coinChange(coins, amount):
    coins.sort(reverse = True)
    result = []
    for i in coins:
        while(amount >= i):
            amount -= i
            result.append(i)
    if(amount == 0):
        return result
print(coinChange([25,10,1,5], 36))



