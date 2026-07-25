class Solution:
    def maxProduct(self, n: int) -> int:
        f,s = 0,0
        while n > 0:
            x = n % 10
            if x > f:
                f,s = x,f
            elif x > s:
                s = x
            n //= 10
        return f*s