# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/submissions/1016799815/
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        start, end = 0, 0
        for idx in range(len(num)):
            i = num[idx]
            if i != "0":
                start = idx
                break

        for idx in range(len(num)-1, -1, -1):
            i = num[idx] 
            if i != "0":
                end = idx + 1
                break
              
        return num[start:end]
