# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/submissions/1016863797/
import re
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        start = re.search("^0+", num)
        end = re.search("0+$", num)
 
        start = start.span()[1] if start != None else 0
        end = end.span()[0] if end != None else len(num)
         
        return num[start:end]
