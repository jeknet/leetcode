# https://leetcode.com/problems/roman-to-integer/submissions/1088516744/
class Solution:
    vals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}
    def romanToInt(self, s: str) -> int:
        response = 0
        temp = 0

        for val in s:
            curr = self.vals[val]

            if temp == 0:
                temp = curr
            elif temp < curr:
                response += curr - temp
                temp = 0
            elif temp > curr:
                response += temp
                temp = curr
            else:
                temp += curr
        
        return response + temp
