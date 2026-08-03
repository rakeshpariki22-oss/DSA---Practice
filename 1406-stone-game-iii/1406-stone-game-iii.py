class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            take = stoneValue[i]
            dp[i] = take - dp[i + 1]
            if i + 1 < n:
                take += stoneValue[i + 1]
                dp[i] = max(dp[i], take - dp[i + 2])
            if i + 2 < n:
                take += stoneValue[i + 2]
                dp[i] = max(dp[i], take - dp[i + 3])
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"