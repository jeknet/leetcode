# https://leetcode.com/problems/truncate-sentence/submissions/1011334972/
import re
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        if k <= 0:
            return ""

        matches = re.finditer("\s", s)
        
        matchCount = 0
        for item in matches:
            matchCount += 1
            if matchCount == k:
                return s[:item.span()[0]]
        
        return s
