# https://leetcode.com/problems/plus-one/submissions/1080574220/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.addOneToIndex(digits, len(digits)-1)

    def addOneToIndex(self, digits, index):
        if index == -1:
            return [1] + digits
            
        if digits[index] + 1 > 9:
            digits[index] = 0
            return self.addOneToIndex(digits, index-1)
        digits[index] += 1
        return digits

        
