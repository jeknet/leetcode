# https://leetcode.com/problems/to-lower-case/submissions/1022671276/
class Solution:
    def toLowerCase(self, s: str) -> str:  
        return "".join([chr(ord(x)+32) if (ord(x) >= 65 and ord(x)<= 90) else x for x in s])
