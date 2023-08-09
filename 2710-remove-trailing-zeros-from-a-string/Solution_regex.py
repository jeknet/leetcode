# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/submissions/1016841943/
import re
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        zeros = re.finditer("0+", num)

        start, end = 0, len(num)

        for match in zeros:
            if match.span()[0] == 0:
                start = match.span()[1]
            if match.span()[1] == end:
                end = match.span()[0]

        return num[start:end]
