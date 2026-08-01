class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2== 0:
            return True

        n = len(nums)

        dp = list(nums)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
                
        return dp[-1] >= 0