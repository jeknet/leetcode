# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0

        val = 0
        for l in s:
            val += -1 if l == "L" else 1
            total += 1 if val == 0 else 0
            
        return total
