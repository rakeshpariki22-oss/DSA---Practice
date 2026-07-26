class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = sorted(nums)
        product1 = n[-1]*n[-2]*n[-3]
        product2 =n[0]*n[1]*n[-1]
        return max(product1,product2)