# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/submissions/1010628356/
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1Index = (0,0)
        w2Index = (0,0)
  
        while w1Index and w2Index:
            resp1 = self.getLetter(word1, w1Index)
            resp2 = self.getLetter(word2, w2Index)
              
            w1Index, l1 = resp1 if resp1 else (None, None)
            w2Index, l2 = resp2 if resp2 else (None, None)

            if l1 != l2:
                return False 

        return True

    def getLetter(self, words: List[str], location):
        wordI, letterI = location 
        if len(words) > wordI:
            if len(words[wordI]) > letterI:
                pass
            else:
                if len(words) > wordI + 1:
                    wordI += 1
                    letterI = 0
                else: 
                    return None
        else: 
            return None
   
        letter = words[wordI][letterI]
        
        return ((wordI, letterI+1), letter)
