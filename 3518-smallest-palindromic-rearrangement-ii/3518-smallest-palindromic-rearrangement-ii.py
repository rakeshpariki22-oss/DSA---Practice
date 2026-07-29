from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        total_counts = Counter(s)
        
        mid_char = ""
        half_counts = [0] * 26  # Array for fixed-size O(1) alphabet access
        half_len = 0
        
        for char, freq in total_counts.items():
            if freq % 2 != 0:
                mid_char = char
            count = freq // 2
            half_counts[ord(char) - 97] = count
            half_len += count
            
        # Step 2: Compute initial arrangements using basic math
        # Arrangements = half_len! / (c1! * c2! * ...)
        total_arrangements = 1
        current_len = 0
        for count in half_counts:
            for i in range(1, count + 1):
                current_len += 1
                total_arrangements = (total_arrangements * current_len) // i

        # Quick exit if k is out of bounds
        if total_arrangements < k:
            return ""
            
        left_half = []
        rem_len = half_len
        
        # Step 3: Digit-by-digit construction in O(N) time
        for _ in range(half_len):
            for i in range(26):
                count = half_counts[i]
                if count == 0:
                    continue
                
                # Math Trick: Calculate arrangements if we choose character i
                # New arrangements = (Old arrangements * count) // rem_len
                branch_arrangements = (total_arrangements * count) // rem_len
                
                if branch_arrangements >= k:
                    # Target string is in this branch
                    left_half.append(chr(i + 97))
                    half_counts[i] -= 1
                    total_arrangements = branch_arrangements
                    break
                else:
                    # Skip this character branch and subtract from k
                    k -= branch_arrangements
            
            rem_len -= 1
                        
        # Step 4: Assemble the final string
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]
