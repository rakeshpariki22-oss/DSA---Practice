class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        last = {}

        for i ,c in enumerate(s):last[c] = i
        res= []

        for i,c in enumerate(s):
            if c in res:continue
            while res and c < res[-1] and i < last[res[-1]]:
                res.pop()
            res.append(c)

        return "".join(res)

        