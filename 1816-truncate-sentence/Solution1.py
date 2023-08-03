# https://leetcode.com/problems/truncate-sentence/submissions/1011254734/
import re
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count = 0
        lastIndex = 0
        it = 0
        for idx, letter in enumerate(s): 
            it += 1
            if letter == " ": 
                count += 1
            if count == k :
                lastIndex = idx
                break 
        return s if it == len(s) else s[:lastIndex]
