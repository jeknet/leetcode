# https://leetcode.com/problems/number-of-good-pairs/submissions/1011696213/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        indexes = {}

        for idx, num in enumerate(nums):
            if num not in indexes.keys():
                indexes[num] = 0
            indexes[num] += 1

        count = 0

        for rep in indexes.values(): 
            count += self.countPairs(rep) if rep >= 2 else 0 
       
        return count

    def countPairs(self, n): 
        if n == 2:
            return 1
        
        return self.countPairs(n - 1) + n - 1
