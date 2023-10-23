# https://leetcode.com/problems/detect-capital/submissions/1082466391/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        firstCapital = self.isCapital(word[0])
        counter = 1 if firstCapital else 0
        size = len(word)
        
        for letter in word[1:]:
            if self.isCapital(letter):
                if not firstCapital:
                    return False
                counter += 1
        
        if counter == 0 or firstCapital and counter == 1:
            return True 
        else:
            return counter == size 

    def isCapital(self, letter):
        return letter >= 'A' and letter <= 'Z'
        
