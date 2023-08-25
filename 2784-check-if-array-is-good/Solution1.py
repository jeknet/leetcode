# https://leetcode.com/problems/check-if-array-is-good/submissions/1031551672/
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        expected = set()
        n = len(nums) - 1
        nCounter = 0

        for num in nums:
            if num == n:
                if nCounter>1:
                    return False
                nCounter += 1
            if num <= n:
                expected.add(num)
        
        return len(expected) == n and nCounter == 2
