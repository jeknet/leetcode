# https://leetcode.com/problems/sum-multiples/submissions/1003756805/?envType=list&envId=rdbn6opm

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        responseSet = set()
        total = 0
        
        for x in range(1, n+1):
            if x not in responseSet:
                self.addAndMark(responseSet, x, n)
        
        return sum(responseSet)


    def addAndMark(self, allSet, val, target):
        if val % 3 == 0 or val % 5 == 0 or val % 7 == 0:  
            allSet.update([x * val for x in range(1, target//val  + 1)]) 
 
