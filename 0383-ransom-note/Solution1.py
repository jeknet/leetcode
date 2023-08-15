# https://leetcode.com/problems/ransom-note/submissions/1021567394/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        base = {}

        for letter in magazine:
            if letter not in base:
                base[letter] = 0
            base[letter] += 1

        for letter in ransomNote:
            if letter in base and base[letter]>=1:
                base[letter] -= 1
            else:
                return False
        
        return True
