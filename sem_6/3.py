def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for x in coins:
            if x <= i:
                dp[i] = min(dp[i], dp[i - x] + 1)
    if dp[amount] == amount + 1:
        return -1
    return dp[amount]
