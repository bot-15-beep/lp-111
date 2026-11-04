def knapsack(W, weights, profits, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):

            if weights[i-1] <= w:
                dp[i][w] = max(
                    profits[i-1] + dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

weights = [2, 3, 4, 5]
profits = [3, 4, 5, 6]

W = 5
n = len(weights)

print("Maximum Profit:", knapsack(W, weights, profits, n))
