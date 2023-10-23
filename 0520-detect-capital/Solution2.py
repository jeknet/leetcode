# https://leetcode.com/problems/detect-capital/submissions/1082475998/
import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if re.search("^[A-Z]{1}[a-z]*$", word):
            return True
        if re.search("^[A-Z]+$", word):
            return True
        if re.search("^[a-z]+$", word):
            return True
        return False
