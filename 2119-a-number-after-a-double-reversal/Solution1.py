# https://leetcode.com/problems/a-number-after-a-double-reversal/submissions/1093201740/
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return True if  (num == 0 ) or num % 10 != 0 else False
        
