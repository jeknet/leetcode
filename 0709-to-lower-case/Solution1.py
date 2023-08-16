# https://leetcode.com/problems/to-lower-case/submissions/1022671276/
class Solution:
    def toLowerCase(self, s: str) -> str:  
        diff = ord('a') - ord('A')
        return "".join([chr(ord(x)+diff) if (ord(x) >= ord('A') and ord(x)<= ord('Z')) else x for x in s])
