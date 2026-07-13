class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        digits = "123456789"
        for length in range(1,10):
            for i in range(10 - length):
                num = int(digits[i : i + length])

                if low <= num <= high:
                    res.append(num)
        return res