# https://leetcode.com/problems/faulty-keyboard/submissions/1018013644/
class Solution:
    def finalString(self, s: str) -> str:
        res = ""

        for letter in s:
            if letter != "i":
                res = res + letter
            else:
                res = res[::-1]

        return res
