# https://leetcode.com/problems/calculate-money-in-leetcode-bank/submissions/1115263384/
class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = 1
        prev = 0
        for i in range(n): 
            total += monday if i % 7 == 0 else prev 
            prev += 1
            if i % 7 == 0:
                monday += 1
                prev = monday


        return total
        
