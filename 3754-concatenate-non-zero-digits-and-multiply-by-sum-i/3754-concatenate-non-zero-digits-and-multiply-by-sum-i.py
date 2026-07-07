class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        x_str = ""
        digit_sum = 0
        
        for char in s:
            if char != '0':
                x_str += char
                digit_sum += int(char)
                
        x = int(x_str) if x_str else 0
        return x * digit_sum
