# https://leetcode.com/problems/second-largest-digit-in-a-string/submissions/1072805730/
class Solution:
    def secondHighest(self, s: str) -> int:
        first, second = -1, -1

        for digit in s:
            if digit.isdigit():
                if int(digit) >= first:
                    second = second if int(digit) == first else first
                    first = int(digit)
                elif int(digit) > second:
                    second = int(digit)

        return second 

        
