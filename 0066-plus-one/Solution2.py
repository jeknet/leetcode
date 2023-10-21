# https://leetcode.com/problems/plus-one/submissions/1080576889/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits)-1, -1, -1):
            if digits[index] + 1 <=9:
                digits[index] += 1
                return digits
            else:
               digits[index] = 0
        return [1] + digits 

        
