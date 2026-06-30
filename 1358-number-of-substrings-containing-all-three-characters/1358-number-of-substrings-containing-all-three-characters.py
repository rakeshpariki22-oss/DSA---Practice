class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = rigth = total =0
        freq =[0] * 3

        while rigth < len(s):
            freq[ord(s[rigth]) - ord("a")] +=1
            while self._has_all_chars(freq):
                total += len(s) - rigth
                freq[ord(s[left]) - ord("a")] -=1
                left +=1 
            rigth +=1
        return total

    def _has_all_chars(self,freq:list)-> bool:
        return all(f > 0 for f in freq)

