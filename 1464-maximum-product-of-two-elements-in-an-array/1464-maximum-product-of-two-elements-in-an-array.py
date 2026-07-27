class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                ans = max(ans,(nums[i] - 1) * (nums[j] - 1))
        return ans