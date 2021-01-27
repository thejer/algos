def coinChange(umbrellas, people) -> int:
    dp = [-1] * (people + 1)
    dp[0] = 0

    for i in range(people + 1):
        if dp[i] != -1:
            for u in umbrellas:
                if i + u < people + 1:
                    dp[i + u] = min(dp[i + u], dp[i] + 1) if dp[i + u] != -1 else dp[i] + 1

    return dp[people]